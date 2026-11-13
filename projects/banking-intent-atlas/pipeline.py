"""Train, calibrate and evaluate two locked NLP routing pipelines on BANKING77."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import argparse, csv, importlib.metadata as md, json, re, sqlite3, time, unicodedata
import joblib
import numpy as np
import pandas as pd
from scipy.optimize import minimize_scalar
from scipy.special import logsumexp, softmax
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, log_loss
from sklearn.model_selection import train_test_split
from threadpoolctl import threadpool_limits

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'outputs'; OUT.mkdir(exist_ok=True)
MODELS=ROOT/'models'; MODELS.mkdir(exist_ok=True)
SEED=1729
PROBES=[
 'What is the weather in Tokyo tomorrow?', 'Book a table for four at an Italian restaurant.',
 'How do I reset my television remote?', 'Write a poem about autumn leaves.',
 'My dog will not eat its food.', 'Can you help me plan a hiking trip?',
 'What is the capital of Peru?', 'I need to reschedule my dentist appointment.',
 'How do I change the oil in my car?', 'The movie subtitles are not displaying.',
 'Explain photosynthesis to a child.', 'Which train goes to the airport?'
]
def now(): return datetime.now(timezone.utc).isoformat()
def dump(name,obj): (OUT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False),encoding='utf-8')
def digest(p): return sha256(p.read_bytes()).hexdigest()
def fingerprint(text):
    return sha256(''.join(c for c in unicodedata.normalize('NFKC',text).casefold() if c.isalnum()).encode()).hexdigest()
def wilson(k,n):
    if n==0:return [None,None]
    z=1.959963984540054; p=k/n; den=1+z*z/n
    center=(p+z*z/(2*n))/den; half=z*np.sqrt(p*(1-p)/n+z*z/(4*n*n))/den
    return [float(max(0,center-half)),float(min(1,center+half))]
def prepare():
    assert not (OUT/'policy_lock.json').exists(), 'Do not silently replace a locked experiment.'
    frames=[]
    for part,expected in [('train',10003),('test',3080)]:
        df=pd.read_csv(ROOT/f'data/raw/{part}.csv',keep_default_na=False)
        assert set(df.columns)=={'text','category'} and len(df)==expected
        assert df.text.str.strip().ne('').all() and df.category.str.strip().ne('').all()
        df['row_id']=[f'{part}_{i:05d}' for i in range(len(df))]
        df['source_split']=part; df['fingerprint']=df.text.map(fingerprint)
        frames.append(df)
    train,test=frames
    conflicts=set(train.groupby('fingerprint').category.nunique().loc[lambda x:x>1].index)
    overlaps=set(train.fingerprint)&set(test.fingerprint)
    eligible=train[~train.fingerprint.isin(conflicts|overlaps)].drop_duplicates('fingerprint',keep='first').copy()
    fit,other=train_test_split(eligible,test_size=.30,random_state=SEED,stratify=eligible.category)
    calibration,policy=train_test_split(other,test_size=.50,random_state=SEED,stratify=other.category)
    groups=[]
    for name,frame in [('fit',fit),('calibration',calibration),('policy',policy),('test',test)]:
        frame=frame.copy(); frame['split']=name; groups.append(frame)
    all_rows=pd.concat(groups,ignore_index=True)
    for i,a in enumerate(groups):
        for b in groups[i+1:]: assert not set(a.fingerprint)&set(b.fingerprint)
    counts={g.iloc[0]['split']:len(g) for g in groups}
    labels=sorted(train.category.unique().tolist()); assert len(labels)==77 and set(labels)==set(test.category)
    all_rows.to_csv(OUT/'split_manifest.csv',index=False,columns=['row_id','source_split','split','category','fingerprint'])
    conn=sqlite3.connect(ROOT/'data/atlas.sqlite')
    all_rows[['row_id','source_split','split','category','fingerprint','text']].to_sql('queries',conn,index=False,if_exists='fail')
    conn.execute('CREATE UNIQUE INDEX query_id ON queries(row_id)'); conn.commit(); conn.close()
    dump('data_audit.json',{'timestamp_utc':now(),'raw_train':len(train),'raw_test':len(test),'intents':len(labels),
      'train_test_overlap_fingerprints':len(overlaps),'training_rows_overlapping_test':int(train.fingerprint.isin(overlaps).sum()),
      'conflicting_training_fingerprints':len(conflicts),'training_rows_removed_total':len(train)-len(eligible),
      'test_duplicate_rows':int(test.fingerprint.duplicated().sum()),
      'test_conflicting_fingerprints':int((test.groupby('fingerprint').category.nunique()>1).sum()),
      'partition_counts':counts,'per_class_counts':all_rows.groupby(['split','category']).size().unstack(fill_value=0).to_dict(orient='index'),
      'normalization':'NFKC/casefold/alphanumeric exact fingerprint; no semantic deduplication.',
      'split_disjoint':True,'protocol_sha256':digest(ROOT/'PROTOCOL.md'),'manifest_sha256':digest(OUT/'split_manifest.csv')})
    dump('labels.json',labels)
    print(json.dumps({'prepared':counts,'removed_train':len(train)-len(eligible),'test_duplicate_rows':int(test.fingerprint.duplicated().sum())}),flush=True)

class Encoder:
    def __init__(self):
        from tokenizers import Tokenizer
        import onnxruntime as ort
        self.tokenizer=Tokenizer.from_file(str(ROOT/'data/models/tokenizer.json'))
        self.tokenizer.enable_truncation(max_length=256)
        self.tokenizer.enable_padding(pad_id=0,pad_token='[PAD]')
        options=ort.SessionOptions(); options.intra_op_num_threads=4; options.inter_op_num_threads=1
        self.session=ort.InferenceSession(str(ROOT/'data/models/model.onnx'),sess_options=options,providers=['CPUExecutionProvider'])
        self.inputs=[i.name for i in self.session.get_inputs()]
    def encode(self,texts,progress=False):
        result=[]; truncated=0
        for start in range(0,len(texts),32):
            encoded=self.tokenizer.encode_batch(texts[start:start+32])
            fields={'input_ids':np.array([e.ids for e in encoded],dtype=np.int64),
                    'attention_mask':np.array([e.attention_mask for e in encoded],dtype=np.int64),
                    'token_type_ids':np.array([e.type_ids for e in encoded],dtype=np.int64)}
            tokens=self.session.run(None,{k:fields[k] for k in self.inputs})[0]
            mask=fields['attention_mask'][...,None]
            pooled=(tokens*mask).sum(axis=1)/np.maximum(mask.sum(axis=1),1)
            pooled/=np.maximum(np.linalg.norm(pooled,axis=1,keepdims=True),1e-12)
            result.append(pooled.astype(np.float32))
            truncated+=sum(sum(e.attention_mask)>=256 for e in encoded)
            if progress and start%1024==0: print(f'Encoded {min(start+32,len(texts))}/{len(texts)} queries',flush=True)
        self.at_limit=truncated
        return np.vstack(result)

def rows():
    conn=sqlite3.connect(ROOT/'data/atlas.sqlite'); df=pd.read_sql('SELECT * FROM queries ORDER BY row_id',conn); conn.close(); return df
def get_embeddings(df):
    path=ROOT/'data/embeddings.npy'; meta=ROOT/'data/embeddings_manifest.json'
    identity=sha256('\n'.join(df.row_id+':'+df.fingerprint).encode()).hexdigest()
    if path.exists():
        m=json.loads(meta.read_text()); assert m['row_identity']==identity and m['model_sha256']==digest(ROOT/'data/models/model.onnx')
        return np.load(path)
    enc=Encoder(); t=time.perf_counter(); values=enc.encode(df.text.tolist(),progress=True)
    np.save(path,values)
    meta.write_text(json.dumps({'row_identity':identity,'shape':list(values.shape),'model_sha256':digest(ROOT/'data/models/model.onnx'),'elapsed_seconds':time.perf_counter()-t,'rows_at_256_token_limit':enc.at_limit,'pooling':'attention-mask mean then L2 normalization','provider':'CPUExecutionProvider','threads':4},indent=2))
    return values
def calibrate(logits,y):
    opt=minimize_scalar(lambda lt:float(np.mean(logsumexp(logits/np.exp(lt),axis=1)-(logits/np.exp(lt))[np.arange(len(y)),y])),bounds=(-3,3),method='bounded')
    assert opt.success; return float(np.exp(opt.x))
def metrics(y,p):
    pred=p.argmax(axis=1); correct=pred==y; conf=p.max(axis=1)
    bins=[]
    for i in range(10):
        m=(conf>=i/10)&((conf<(i+1)/10) if i<9 else (conf<=1))
        if m.sum(): bins.append({'lo':i/10,'hi':(i+1)/10,'n':int(m.sum()),'confidence':float(conf[m].mean()),'accuracy':float(correct[m].mean())})
    return {'n':len(y),'correct':int(correct.sum()),'accuracy':float(correct.mean()),'accuracy_ci95':wilson(int(correct.sum()),len(y)),
     'macro_f1':float(f1_score(y,pred,labels=list(range(77)),average='macro',zero_division=0)),
     'top3':float(np.mean([yi in choices for yi,choices in zip(y,np.argsort(p,axis=1)[:,-3:])])),
     'nll':float(log_loss(y,p,labels=list(range(77)))),'ece10':sum(b['n']*abs(b['confidence']-b['accuracy']) for b in bins)/len(y),'reliability_bins':bins}
def policy_curve(y,p):
    pred=p.argmax(axis=1); conf=p.max(axis=1); result=[]
    for threshold in np.arange(100)/100:
        mask=conf>=threshold; n=int(mask.sum()); err=int((pred[mask]!=y[mask]).sum())
        interval=wilson(err,n)
        result.append({'threshold':float(threshold),'accepted':n,'errors':err,'coverage':n/len(y),'error_rate':err/n if n else None,'error_ci95':interval,'eligible':bool(n>=200 and interval[1]<=.05) if n else False})
    return result
def train():
    assert not (OUT/'policy_lock.json').exists(), 'Policy already locked; use a new experiment directory for changes.'
    df=rows(); labels=json.loads((OUT/'labels.json').read_text()); lookup={l:i for i,l in enumerate(labels)}
    idx={s:np.where(df.split.to_numpy()==s)[0] for s in ['fit','calibration','policy','test']}
    y=df.category.map(lookup).to_numpy()
    vectorizer=TfidfVectorizer(ngram_range=(1,2),min_df=2,max_features=30000,sublinear_tf=True)
    vectorizer.fit(df.iloc[idx['fit']].text)
    lexical=vectorizer.transform(df.text); semantic=get_embeddings(df)
    assert semantic.shape==(len(df),384) and np.isfinite(semantic).all()
    assert np.max(np.abs(np.linalg.norm(semantic,axis=1)-1))<1e-4
    joblib.dump(vectorizer,MODELS/'vectorizer.joblib')
    result={}; locked={}; logit_cache={}
    for name,x in [('lexical',lexical),('semantic',semantic)]:
        model=LogisticRegression(C=4,solver='lbfgs',max_iter=1000,random_state=SEED)
        t=time.perf_counter()
        with threadpool_limits(limits=4): model.fit(x[idx['fit']],y[idx['fit']])
        elapsed=time.perf_counter()-t
        assert np.array_equal(model.classes_,np.arange(77)) and int(model.n_iter_.max())<1000
        cal_logits=model.decision_function(x[idx['calibration']]); temperature=calibrate(cal_logits,y[idx['calibration']])
        policy_logits=model.decision_function(x[idx['policy']]); policy_p=softmax(policy_logits/temperature,axis=1)
        curve=policy_curve(y[idx['policy']],policy_p); eligible=[r for r in curve if r['eligible']]
        choice=max(eligible,key=lambda r:(r['coverage'],r['threshold'])) if eligible else {'threshold':1.01,'accepted':0,'errors':0,'coverage':0,'error_rate':None,'error_ci95':[None,None],'eligible':False}
        locked[name]={'temperature':temperature,'threshold':choice['threshold'],'policy':choice,'policy_metrics':metrics(y[idx['policy']],policy_p)}
        result[name]={'training_seconds':elapsed,'iterations':int(model.n_iter_.max()),'features':x.shape[1],
          'calibration_raw':metrics(y[idx['calibration']],softmax(cal_logits,axis=1)),
          'calibration_after':metrics(y[idx['calibration']],softmax(cal_logits/temperature,axis=1)),
          'policy_curve':curve}
        logit_cache[name]=model.decision_function(x[idx['test']])
        joblib.dump(model,MODELS/f'{name}.joblib')
        print(name,'policy coverage',choice['coverage'],'threshold',choice['threshold'],flush=True)
    selected=max(locked,key=lambda k:(locked[k]['policy']['coverage'],locked[k]['policy_metrics']['macro_f1']))
    lock={'locked_utc':now(),'protocol_sha256':digest(ROOT/'PROTOCOL.md'),'manifest_sha256':digest(OUT/'split_manifest.csv'),'selected_before_test':selected,'models':locked,'majority_class':int(np.bincount(y[idx['fit']]).argmax()),'test_scoring_performed':False}
    dump('training.json',result); dump('policy_lock.json',lock)
    np.savez_compressed(OUT/'test_logits.npz',**logit_cache)
    dump('environment.json',{'python':__import__('sys').version,'packages':{p:md.version(p) for p in ['numpy','pandas','scipy','scikit-learn','onnxruntime','tokenizers','matplotlib','reportlab','pypdf','joblib']}})
    (ROOT/'requirements.txt').write_text('\n'.join(f'{p}=={md.version(p)}' for p in ['numpy','pandas','scipy','scikit-learn','onnxruntime','tokenizers','matplotlib','reportlab','pypdf','joblib'])+'\n')
    print('Policy locked before final evaluation:',selected,flush=True)

def evaluate():
    assert not (OUT/'metrics.json').exists(), 'Retain the first evaluation; no silent test reruns.'
    lock=json.loads((OUT/'policy_lock.json').read_text()); assert lock['protocol_sha256']==digest(ROOT/'PROTOCOL.md')
    df=rows(); test=df[df.split=='test'].copy(); labels=json.loads((OUT/'labels.json').read_text()); lookup={l:i for i,l in enumerate(labels)}
    y=test.category.map(lookup).to_numpy(); logits=np.load(OUT/'test_logits.npz'); all_records=[]; result={}; probs={}
    for name in ['lexical','semantic']:
        p=softmax(logits[name]/lock['models'][name]['temperature'],axis=1); probs[name]=p
        pred=p.argmax(axis=1); confidence=p.max(axis=1); threshold=lock['models'][name]['threshold']; accepted=confidence>=threshold
        m=metrics(y,p); n=int(accepted.sum()); e=int((pred[accepted]!=y[accepted]).sum())
        m['referral']={'threshold':threshold,'accepted':n,'errors':e,'correct':n-e,'coverage':n/len(y),'reviewed':len(y)-n,'error_rate':e/n if n else None,'error_ci95':wilson(e,n)}
        m['curve']=policy_curve(y,p); result[name]=m
        ranks=np.argsort(p,axis=1)[:,-3:][:,::-1]
        for k,(_,row) in enumerate(test.iterrows()):
            all_records.append({'row_id':row.row_id,'model':name,'truth':row.category,'prediction':labels[pred[k]],'confidence':float(confidence[k]),'correct':int(pred[k]==y[k]),'accepted':int(accepted[k]),'runner_up':labels[ranks[k,1]],'runner_up_probability':float(p[k,ranks[k,1]]),'third':labels[ranks[k,2]],'third_probability':float(p[k,ranks[k,2]]),'fingerprint':row.fingerprint})
    predictions=pd.DataFrame(all_records); predictions.to_csv(OUT/'predictions.csv',index=False,float_format='%.12g')
    conn=sqlite3.connect(ROOT/'data/atlas.sqlite'); predictions.to_sql('predictions',conn,index=False,if_exists='fail'); conn.execute('CREATE UNIQUE INDEX prediction_id ON predictions(row_id,model)'); conn.commit(); conn.close()
    majority=np.full(len(y),lock['majority_class']); result['majority']={'n':len(y),'correct':int((majority==y).sum()),'accuracy':float((majority==y).mean()),'macro_f1':float(f1_score(y,majority,labels=list(range(77)),average='macro',zero_division=0))}
    rng=np.random.default_rng(SEED+1); difference=(probs['semantic'].argmax(axis=1)==y).astype(int)-(probs['lexical'].argmax(axis=1)==y).astype(int)
    boot=np.array([difference[rng.integers(0,len(y),len(y))].mean() for _ in range(2000)])
    enc=Encoder(); xp=enc.encode(PROBES); vectorizer=joblib.load(MODELS/'vectorizer.joblib'); probes=[]
    for name,x in [('lexical',vectorizer.transform(PROBES)),('semantic',xp)]:
        model=joblib.load(MODELS/f'{name}.joblib'); p=softmax(model.decision_function(x)/lock['models'][name]['temperature'],axis=1)
        for text,prob in zip(PROBES,p):probes.append({'text':text,'model':name,'prediction':labels[int(prob.argmax())],'confidence':float(prob.max()),'accepted':bool(prob.max()>=lock['models'][name]['threshold'])})
    dump('ood_probes.json',probes)
    result.update({'evaluated_utc':now(),'policy_lock_sha256':digest(OUT/'policy_lock.json'),'protocol_sha256':digest(ROOT/'PROTOCOL.md'),'selected_before_test':lock['selected_before_test'],
      'paired_accuracy_difference':{'semantic_minus_lexical':float(difference.mean()),'bootstrap_ci95':np.quantile(boot,[.025,.975]).tolist(),'replicates':2000,'seed':SEED+1,'unit':'same held-out query rows'},
      'ood_probe_acceptance':{name:sum(p['accepted'] for p in probes if p['model']==name) for name in ['lexical','semantic']},'ood_probe_n':len(PROBES)})
    dump('metrics.json',result)
    selected=lock['selected_before_test']; selected_rows=predictions[predictions.model==selected]
    errors=selected_rows[selected_rows.correct==0].groupby(['truth','prediction']).size().sort_values(ascending=False).head(12)
    errors.rename('count').reset_index().to_csv(OUT/'confusion_pairs.csv',index=False)
    print(json.dumps({'selected':selected,'lexical':{k:result['lexical'][k] for k in ['accuracy','macro_f1','referral']},'semantic':{k:result['semantic'][k] for k in ['accuracy','macro_f1','referral']},'ood_probe_acceptance':result['ood_probe_acceptance']}),flush=True)

def predict(text):
    lock=json.loads((OUT/'policy_lock.json').read_text()); name=lock['selected_before_test']; labels=json.loads((OUT/'labels.json').read_text())
    x=Encoder().encode([text]) if name=='semantic' else joblib.load(MODELS/'vectorizer.joblib').transform([text])
    model=joblib.load(MODELS/f'{name}.joblib'); p=softmax(model.decision_function(x)/lock['models'][name]['temperature'],axis=1)[0]
    order=np.argsort(p)[-3:][::-1]
    print(json.dumps({'model':name,'top3':[{'intent':labels[i],'confidence':float(p[i])} for i in order],
      'policy':'suggest intent' if p.max()>=lock['models'][name]['threshold'] else 'defer to a person',
      'limit':'Offline in-domain benchmark; confidence does not establish that the query is banking-related. No action is executed.'},indent=2))
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('stage',choices=['prepare','train','evaluate','predict']);parser.add_argument('--text')
    args=parser.parse_args()
    if args.stage=='predict': assert args.text; predict(args.text)
    else: globals()[args.stage]()

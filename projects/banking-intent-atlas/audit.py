"""Independent standard-library and SQLite verification; does not import the pipeline."""
from pathlib import Path
from collections import Counter, defaultdict
from hashlib import sha256
from datetime import datetime, timezone
import csv, json, math, sqlite3, unittest

ROOT=Path(__file__).resolve().parent; OUT=ROOT/'outputs'
def read(name): return json.loads((OUT/name).read_text(encoding='utf-8'))
def interval(errors,n):
    z=1.959963984540054
    if not n:return [None,None]
    p=errors/n; mid=(p+z*z/(2*n))/(1+z*z/n)
    radius=z*math.sqrt((p*(1-p)+z*z/(4*n))/n)/(1+z*z/n)
    return [max(0,mid-radius),min(1,mid+radius)]
def calculate(records,threshold):
    total=len(records); right=sum(r['truth']==r['prediction'] for r in records)
    accepted=[r for r in records if float(r['confidence'])>=threshold]
    bad=sum(r['truth']!=r['prediction'] for r in accepted)
    classes=sorted({r['truth'] for r in records}); values=[]
    for c in classes:
        tp=sum(r['truth']==c and r['prediction']==c for r in records)
        fp=sum(r['truth']!=c and r['prediction']==c for r in records)
        fn=sum(r['truth']==c and r['prediction']!=c for r in records)
        values.append(2*tp/(2*tp+fp+fn) if tp+fp+fn else 0)
    return {'n':total,'correct':right,'accuracy':right/total,'macro_f1':sum(values)/len(values),'accepted':len(accepted),'errors':bad,'coverage':len(accepted)/total,'error_ci95':interval(bad,len(accepted))}
def main():
    rows=list(csv.DictReader((OUT/'predictions.csv').open(encoding='utf-8',newline='')))
    split=list(csv.DictReader((OUT/'split_manifest.csv').open(encoding='utf-8',newline='')))
    metrics=read('metrics.json'); lock=read('policy_lock.json'); quality=read('data_audit.json')
    checks={}; models={}
    checks['policy_lock_hash_unchanged']=sha256((OUT/'policy_lock.json').read_bytes()).hexdigest()==metrics['policy_lock_sha256']
    checks['protocol_hash_unchanged']=sha256((ROOT/'PROTOCOL.md').read_bytes()).hexdigest()==lock['protocol_sha256']==metrics['protocol_sha256']
    checks['split_hash_unchanged']=sha256((OUT/'split_manifest.csv').read_bytes()).hexdigest()==lock['manifest_sha256']
    checks['policy_locked_before_test_scoring']=datetime.fromisoformat(lock['locked_utc'])<datetime.fromisoformat(metrics['evaluated_utc'])
    checks['predictions_unique']=len({(r['row_id'],r['model']) for r in rows})==len(rows)==6160
    sets={s:{r['fingerprint'] for r in split if r['split']==s} for s in ['fit','calibration','policy','test']}
    checks['split_fingerprints_disjoint']=all(not sets[a]&sets[b] for i,a in enumerate(sets) for b in list(sets)[i+1:])
    checks['recorded_correctness_matches_labels']=all(int(r['correct'])==int(r['truth']==r['prediction']) for r in rows)
    conn=sqlite3.connect(ROOT/'data/atlas.sqlite')
    sql=conn.execute('SELECT model, COUNT(*), SUM(correct), SUM(accepted), SUM(CASE WHEN accepted=1 AND correct=0 THEN 1 ELSE 0 END) FROM predictions GROUP BY model').fetchall()
    sql={r[0]:list(r[1:]) for r in sql}
    checks['sqlite_join_preserves_rows']=conn.execute('SELECT COUNT(*) FROM predictions p JOIN queries q USING(row_id)').fetchone()[0]==6160
    checks['sqlite_only_official_test']=conn.execute("SELECT COUNT(*) FROM predictions p JOIN queries q USING(row_id) WHERE q.split!='test'").fetchone()[0]==0
    conn.close()
    for name in ['lexical','semantic']:
        records=[r for r in rows if r['model']==name]; threshold=lock['models'][name]['threshold']; x=calculate(records,threshold); m=metrics[name]
        for key in ['n','correct','accuracy','macro_f1']:checks[name+'_'+key]=abs(x[key]-m[key])<1e-10
        for key in ['accepted','errors','coverage']:checks[name+'_'+key]=abs(x[key]-m['referral'][key])<1e-10
        checks[name+'_bounds']=all(abs(a-b)<1e-10 for a,b in zip(x['error_ci95'],m['referral']['error_ci95']))
        checks[name+'_sqlite']=sql[name]==[x['n'],x['correct'],x['accepted'],x['errors']]
        checks[name+'_acceptance_flags']=all(int(r['accepted'])==int(float(r['confidence'])>=threshold) for r in records)
        checks[name+'_empty_high_threshold']=calculate(records,1.01)['accepted']==0
        checks[name+'_full_coverage_zero_threshold']=calculate(records,0)['accepted']==3080
        groups=defaultdict(list)
        for r in records:groups[r['fingerprint']].append(r)
        sensitivity=[g[0] for g in groups.values() if len({r['truth'] for r in g})==1]
        x['posthoc_unique_unambiguous_test_sensitivity']=calculate(sensitivity,threshold)
        models[name]=x
    selected=max(lock['models'],key=lambda name:(lock['models'][name]['policy']['coverage'],lock['models'][name]['policy_metrics']['macro_f1']))
    checks['selection_uses_policy_only']=selected==lock['selected_before_test']==metrics['selected_before_test']
    checks['all_input_hashes_match']=all(sha256((ROOT/s['path']).read_bytes()).hexdigest()==s['sha256'] for s in read('source_manifest.json')['sources'])
    report={'checked_utc':datetime.now(timezone.utc).isoformat(),'checks':checks,'models':models,'pass':all(checks.values()),
      'method':'Independent CSV counts, manual per-class F1/Wilson formula, SQL aggregate/join checks and source/version hashes. Does not import pipeline.py.',
      'additional_sensitivity':'Post hoc diagnostic only: remove conflicting-label test fingerprints and deduplicate remaining test text. Main benchmark and model/threshold selection unchanged.',
      'limits':['Exact-normalized duplicates guarded; semantic near-duplicates may remain.','Row-level intervals and bootstrap do not model latent customer grouping or pretraining contamination.','The 12 OOD probes are synthetic and not representative.']}
    (OUT/'independent_audit.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps({'pass':report['pass'],'checks':len(checks),'models':models},indent=2))
    assert report['pass'], 'Preserve the failed audit and investigate before publication.'
if __name__=='__main__':main()

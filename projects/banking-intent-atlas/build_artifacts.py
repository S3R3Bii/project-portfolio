"""Build the visual paper and a compact, inspectable evidence explorer."""
from pathlib import Path
from datetime import datetime
from hashlib import sha256
import csv, html, json, re, sqlite3, textwrap
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image as PILImage
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak, Preformatted
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT

ROOT=Path(__file__).resolve().parent; O=ROOT/'outputs'; WEB=ROOT/'showcase'; WEB.mkdir(exist_ok=True)
FIG=O/'figures'; FIG.mkdir(exist_ok=True)
M=json.loads((O/'metrics.json').read_text()); L=json.loads((O/'policy_lock.json').read_text()); A=json.loads((O/'data_audit.json').read_text()); V=json.loads((O/'independent_audit.json').read_text())
assert V['pass']
LABELS=json.loads((O/'labels.json').read_text()); P=list(csv.DictReader((O/'predictions.csv').open(encoding='utf-8',newline='')))
BLUE='#28748c'; RUST='#b45137'; NAVY='#132e42'; GRAY='#60727b'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'axes.labelcolor':NAVY,'text.color':NAVY,'axes.edgecolor':'#9fadb2','savefig.facecolor':'white'})
def save(fig,name):
    fig.savefig(FIG/f'{name}.png',dpi=145,bbox_inches='tight'); fig.savefig(FIG/f'{name}.svg',bbox_inches='tight')
    PILImage.open(FIG/f'{name}.png').convert('RGB').save(WEB/f'{name}.webp',quality=88,method=6)
    plt.close(fig)
def charts():
    fig,ax=plt.subplots(figsize=(8.1,3.7))
    for name,label,color in [('lexical','TF-IDF + logistic regression',RUST),('semantic','Frozen MiniLM + logistic regression',BLUE)]:
        c=[x for x in M[name]['curve'] if x['accepted']>=100]
        ax.plot([x['coverage']*100 for x in c],[x['error_rate']*100 for x in c],color=color,lw=2.3,label=label)
        f=M[name]['referral']; ax.scatter([100*f['coverage']],[100*f['error_rate']],s=85,color=color,zorder=5,edgecolors='white',linewidths=1)
        ax.annotate(f"Frozen policy: {f['coverage']:.1%} coverage\n{f['errors']}/{f['accepted']} errors",(100*f['coverage'],100*f['error_rate']),xytext=(-112,32 if name=='semantic' else 55),textcoords='offset points',fontsize=8.5,arrowprops={'arrowstyle':'-','color':color},color=color,bbox={'facecolor':'white','edgecolor':'none','alpha':.85,'pad':2})
    ax.axhline(5,color=GRAY,ls='--',lw=1,label='Illustrative 5% error target')
    ax.set(xlim=(0,102),ylim=(0,15),xlabel='Queries accepted for intent suggestion (%)',ylabel='Error among accepted queries (%)',title='More coverage means less human review - and more risk')
    ax.grid(alpha=.15);ax.legend(loc='upper left',frameon=False,fontsize=8);fig.tight_layout();save(fig,'risk_coverage')
    fig,ax=plt.subplots(figsize=(8.1,3.6));ax.set_axis_off()
    boxes=[(.01,.61,.25,.25,'10,003 training rows\n62 removed by text audit'),(.36,.61,.25,.25,'9,941 eligible rows\nstratified, seed 1729'),(.71,.61,.27,.25,'3,080 official test rows\nseparate; scored last')]
    for x,y,w,h,t in boxes:ax.add_patch(plt.Rectangle((x,y),w,h,facecolor='#e9f1f3',edgecolor=BLUE,lw=1.3));ax.text(x+w/2,y+h/2,t,ha='center',va='center',fontsize=10)
    ax.annotate('',(.35,.735),(.27,.735),arrowprops={'arrowstyle':'->','color':BLUE})
    for x,n,label in [(.01,6958,'Fit vocabulary / models'),(.34,1491,'Calibrate probabilities'),(.67,1492,'Choose policy / model')]:
        ax.add_patch(plt.Rectangle((x,.10),.30,.28,facecolor='white',edgecolor=BLUE,lw=1.3));ax.text(x+.15,.24,f'{n:,}\n{label}',ha='center',va='center',fontsize=10)
    for x in [.16,.49,.82]:ax.annotate('',(x,.39),(.49,.60),arrowprops={'arrowstyle':'->','color':GRAY,'lw':.9})
    ax.text(.5,.015,'No exact-normalized text fingerprint crosses these partitions.',ha='center',fontsize=9,color=GRAY)
    fig.tight_layout();save(fig,'data_flow')
    fig,ax=plt.subplots(figsize=(8.1,3.35))
    names=['Training-majority reference','TF-IDF + logistic regression','Frozen MiniLM + logistic regression']; vals=[M[k]['accuracy']*100 for k in ['majority','lexical','semantic']]
    ax.barh(np.arange(3),vals,color=['#bdc8cc',RUST,BLUE],height=.5)
    for i,k in enumerate(['lexical','semantic'],1):
        low,high=M[k]['accuracy_ci95'];val=vals[i];ax.errorbar(val,i,xerr=[[val-low*100],[high*100-val]],color=NAVY,capsize=3,lw=1)
    for i,v in enumerate(vals):ax.text(v+1.1,i,f'{v:.1f}%',va='center',fontsize=11)
    ax.set(yticks=np.arange(3),yticklabels=names,xlim=(0,104),xlabel='Correct top-1 intent (%)',title='Same final test: 3,080 queries across 77 intents');ax.invert_yaxis();ax.grid(axis='x',alpha=.15);fig.tight_layout();save(fig,'model_comparison')
    fig,ax=plt.subplots(figsize=(8.1,3.7))
    for name,label,color in [('lexical','TF-IDF',RUST),('semantic','MiniLM',BLUE)]:
        bins=M[name]['reliability_bins'];ax.plot([x['confidence'] for x in bins],[x['accuracy'] for x in bins],'-o',color=color,label=label,ms=4)
    ax.plot([0,1],[0,1],'--',color=GRAY,lw=1,label='Perfect-bin calibration reference')
    ax.set(xlim=(0,1),ylim=(0,1),xlabel='Mean calibrated top-1 confidence',ylabel='Observed top-1 accuracy',title='Reliability on the final test (10 equal-width bins)');ax.grid(alpha=.15);ax.legend(frameon=False,fontsize=8);fig.tight_layout();save(fig,'reliability')
    pairs=list(csv.DictReader((O/'confusion_pairs.csv').open()))[:6]
    fig,ax=plt.subplots(figsize=(8.1,3.8));ys=np.arange(len(pairs))
    labels=['\n'.join(textwrap.wrap(r['truth'].replace('_',' ')+' -> '+r['prediction'].replace('_',' '),47)) for r in pairs]
    ax.barh(ys,[int(r['count']) for r in pairs],color=RUST,height=.58);ax.set(yticks=ys,yticklabels=labels,xlim=(0,7),xlabel='Misclassified queries',title='The remaining errors often cross nearby intent boundaries')
    ax.invert_yaxis();ax.tick_params(axis='y',labelsize=8);ax.grid(axis='x',alpha=.15);fig.tight_layout();save(fig,'confusion_pairs')

def paper():
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='TitleAtlas',fontName='Helvetica-Bold',fontSize=27,leading=31,textColor=colors.HexColor(NAVY),spaceAfter=14))
    styles.add(ParagraphStyle(name='HAtlas',fontName='Helvetica-Bold',fontSize=18,leading=22,textColor=colors.HexColor(NAVY),spaceAfter=12))
    styles.add(ParagraphStyle(name='BodyAtlas',fontName='Helvetica',fontSize=10,leading=14,spaceAfter=9,textColor=colors.HexColor(NAVY)))
    styles.add(ParagraphStyle(name='CaptionAtlas',fontName='Helvetica',fontSize=8,leading=11,spaceAfter=10,textColor=colors.HexColor(GRAY)))
    styles.add(ParagraphStyle(name='CodeAtlas',fontName='Courier',fontSize=8,leading=12,spaceAfter=10))
    story=[]; narrative=[]
    def para(text,kind='BodyAtlas'):
        narrative.append(re.sub('<[^>]+>','',text));story.append(Paragraph(text,styles[kind]))
    def title(text):para(text,'HAtlas')
    def fig(name,caption,width=498):
        path=FIG/f'{name}.png';w,h=PILImage.open(path).size;story.append(Image(str(path),width=width,height=width*h/w));para(caption,'CaptionAtlas')
    def table(rows,widths):
        body=[[Paragraph(str(c),styles['CaptionAtlas']) for c in row] for row in rows]
        t=Table(body,colWidths=widths,hAlign='LEFT');t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e9f1f3')),('LINEBELOW',(0,0),(-1,0),.7,colors.HexColor(BLUE)),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),1),('LINEBELOW',(0,1),(-1,-1),.3,colors.HexColor('#dbe4e7'))]));story.append(t);story.append(Spacer(1,10))
    def page():story.append(PageBreak())
    para('BANKING INTENT ATLAS','CaptionAtlas');para('Knowing when an NLP router<br/>should defer','TitleAtlas')
    para('James N. Jean IV | Independent portfolio engineering study | November 13, 2026<br/>Substantial ChatGPT Codex assistance; local CPU inference; no paid inference service.','CaptionAtlas')
    para('<b>Executive summary.</b> A fixed pretrained sentence encoder improved top-1 banking-intent accuracy from <b>86.8% to 91.7%</b> on 3,080 official BANKING77 test queries. Both classifiers were trained on the same 6,958-row fitting partition. A separate policy split selected the encoder pipeline before test scoring. [1, 2]')
    para('At its frozen 0.66 confidence threshold, the selected pipeline accepted <b>2,755 queries (89.4%)</b> and referred 325 for human review. It made 96 errors among accepted queries: <b>3.5%</b>, with a 95% Wilson interval of <b>2.9%-4.2%</b>. This is offline benchmark evidence, not a deployment guarantee.')
    fig('risk_coverage','Figure 1. Test-set coverage/error curves are descriptive. Filled points are policies frozen on a separate split. The 5% line is an illustrative design target; thresholds were not retuned on this curve.')
    para('<b>Recommendation.</b> Use the encoder pipeline as the stronger candidate for a supervised intent-suggestion pilot. Retain human review and a separate domain check: it confidently accepted 2 of 12 synthetic non-banking probes. No banking action should be automated from this study.')
    page(); title('1. Keep the evidence streams separate')
    para('BANKING77 provides English online-banking queries labeled with 77 intents. Its official training/test split supplies a useful constrained benchmark, but it has no customer identifiers, timestamps or live operational outcomes. This study preserves all official test rows for its primary comparison. [1]')
    fig('data_flow','Figure 2. The three lower boxes partition the 9,941 eligible training rows. The official test set is a separate cohort, not the next stage of that training funnel.')
    table([['Audit item','Observed result'],['Official source rows','10,003 training; 3,080 test'],['Training rows removed','62 in total; including 29 rows sharing a normalized text fingerprint with test'],['Other training exclusions','Conflicting-label fingerprint groups removed; remaining duplicate fingerprints retain their first row'],['Final partitions','6,958 fitting / 1,491 calibration / 1,492 policy / 3,080 test'],['Test duplicates','4 repeated normalized-text rows; 1 conflicting-label fingerprint group'],['Independent verification','35 source, partition, count, F1, interval, threshold and SQL checks passed']],[170,328])
    para('The fingerprint uses NFKC normalization, case-folding and alphanumeric characters. It removes exact-normalized overlap, not semantic paraphrases. A post hoc sensitivity check deduplicated test text and removed conflicting-label groups: 3,075 queries remained, with 91.74% encoder accuracy versus the primary 91.72%. This diagnostic did not change the model or policy.')
    page(); title('2. Compare two complete, fixed pipelines')
    fig('model_comparison','Figure 3. Full-test top-1 accuracy; error bars are 95% Wilson intervals over query rows. The majority-class reference is selected from the fitting split.')
    table([['Pipeline','Accuracy','Macro-F1','Top-3 recall','Test NLL'],['TF-IDF + logistic',f"{M['lexical']['accuracy']:.2%}",f"{M['lexical']['macro_f1']:.4f}",f"{M['lexical']['top3']:.2%}",f"{M['lexical']['nll']:.4f}"],['Frozen MiniLM + logistic',f"{M['semantic']['accuracy']:.2%}",f"{M['semantic']['macro_f1']:.4f}",f"{M['semantic']['top3']:.2%}",f"{M['semantic']['nll']:.4f}"]],[174,81,81,81,81])
    diff=M['paired_accuracy_difference'];lo,hi=diff['bootstrap_ci95']
    para(f"The encoder advantage was <b>{diff['semantic_minus_lexical']*100:.2f} percentage points</b>; a paired 2,000-resample query bootstrap gave a 95% interval of <b>{lo*100:.2f}-{hi*100:.2f} points</b>. The interval conditions on these two trained pipelines and the fixed test set; it does not include training-seed variation or future customer drift.")
    para('<b>Lexical representation.</b> TF-IDF uses word unigrams/bigrams, sublinear term frequency, min_df=2, up to 30,000 features and L2 normalization. The vocabulary and IDF are learned only from the fitting split. Negation and other stopwords are retained.')
    para('<b>Semantic representation.</b> The author-published all-MiniLM-L6-v2 ONNX model maps each query to a 384-dimensional vector. Attention-mask mean pooling and L2 normalization follow the model card. No query reached the 256-wordpiece limit. The encoder is frozen; only the downstream classifier is trained. [2]')
    para('Both classifiers use L2 logistic regression with C=4, lbfgs and a 1,000-iteration cap; both converged before the cap. These are fixed engineering settings, not tuned optima. Equal C does not imply equal effective regularization across feature spaces.')
    page(); title('3. Turn confidence into a review policy')
    para('A single temperature per model minimizes negative log likelihood on the 1,491-row calibration split. The separate 1,492-row policy split considers confidence cutoffs from 0.00 to 0.99. An eligible cutoff must accept at least 200 queries and have a two-sided 95% Wilson upper error bound at or below 5%. Among eligible cutoffs, choose greatest coverage. [3]')
    table([['Frozen policy','TF-IDF','MiniLM'],['Temperature',f"{L['models']['lexical']['temperature']:.4f}",f"{L['models']['semantic']['temperature']:.4f}"],['Confidence cutoff','0.88','0.66'],['Policy-split coverage','67.7%','89.7%'],['Test accepted / errors','2,151 / 54','2,755 / 96'],['Test referred to review','929 (30.2%)','325 (10.6%)'],['Accepted error, 95% interval','2.51% (1.93%-3.26%)','3.48% (2.86%-4.24%)']],[218,140,140])
    fig('reliability','Figure 4. Final-test reliability after temperature calibration. Ten equal-width bins; sparse low-confidence bins can fluctuate. ECE is 0.0143 for TF-IDF and 0.0129 for MiniLM, not a universal confidence guarantee.')
    para('The encoder offers more coverage at its own qualifying threshold, while the lexical policy has fewer accepted errors. This is a workload/risk tradeoff, not a claim that the encoder dominates every operating point. The policy-split bound is a selection heuristic; the independent test evaluates the frozen choice.')
    page(); title('4. Inspect failures, including confident ones')
    fig('confusion_pairs','Figure 5. Six most frequent wrong-label pairs for the selected encoder over all 3,080 test queries. Similar banking concepts remain separable labels in this benchmark.')
    para('Errors such as card arrival versus delivery estimate and declined transfer versus declined card payment show why a useful system should expose alternatives instead of treating the top label as ground truth. The explorer retains top-three alternatives and distinguishes accepted mistakes from referred cases.')
    probes=json.loads((O/'ood_probes.json').read_text());bad=[p for p in probes if p['model']=='semantic' and p['accepted']]
    table([['Synthetic out-of-domain probe','Predicted intent','Confidence']]+[[html.escape(p['text']),p['prediction'].replace('_',' '),f"{p['confidence']:.1%}"] for p in bad],[235,190,73])
    para('All 12 non-banking probes were declared before evaluation. The lexical policy accepted none; the encoder accepted the two above. This tiny authored challenge set is not an estimate of real-world out-of-domain error. It demonstrates a concrete failure of relying on maximum class probability as a domain detector.')
    para('<b>Practical implication.</b> A proposed pilot needs an explicit supported-intent/domain gate, a human escalation path and monitoring of novel requests. Building and validating such a gate is a next experiment, not a feature claimed by this release.')
    page(); title('5. Engineering that can be inspected')
    para('The project runs locally in Python. Pinned public-source URLs and SHA-256 hashes identify the dataset, tokenizer and ONNX weights. The source manifest, split manifest, protocol and policy lock preserve the order of decisions. No external model API receives query text.')
    story.append(Preformatted('python fetch_sources.py\npython pipeline.py prepare\npython pipeline.py train\npython pipeline.py evaluate\npython audit.py\npython build_artifacts.py\npython pipeline.py predict --text "My card has not arrived yet"',styles['CodeAtlas']))
    para('A SQLite database contains one query record per retained source row and one prediction per query/model. Unique indexes and explicit joins make the test grain inspectable. Public prediction CSVs contain IDs, labels, probabilities and text fingerprints; the small browser example set is drawn from the licensed benchmark.')
    table([['Independent check','Result'],['Source and version hashes','All retained input files, protocol, split and policy hashes matched'],['Split isolation','No normalized text fingerprint crossed fit, calibration, policy or test'],['Metric reconstruction','Manual class-wise F1, correctness counts and Wilson bounds agree with saved results'],['SQL reconciliation','6,160 model/query predictions; joins preserve rows and include official test only'],['Threshold boundaries','0 accepts all 3,080 queries; 1.01 accepts none for each pipeline'],['Saved artifacts','The browser replays saved decisions; the local CLI performs fresh inference']],[185,313])
    para('The encoder computed 13,021 query vectors in 22.5 seconds in this run, using ONNX Runtime CPU execution with four intra-op threads. This is a single local execution observation, not a controlled speed comparison or service-level guarantee. Package versions are pinned in requirements.txt and recorded in environment.json.')
    para('James defined the portfolio objective; ChatGPT Codex substantially assisted protocol design, implementation, execution, verification, writing and presentation. This is new independent portfolio work, not prior professional NLP tenure.')
    page(); title('6. Limits and the next defensible experiment')
    para('<b>What the evidence establishes.</b> Two executed pipelines, a separately selected referral policy, and independently checked outcomes on a fixed 77-intent English benchmark. The selected encoder is a stronger candidate for a supervised pilot under the stated illustrative error target.')
    para('<b>What remains unverified.</b> New customers, different institutions, multilingual messages, evolving intent definitions, adversarial inputs, semantically repeated customers, privacy-sensitive production text and deployment costs. No temporal or customer-group holdout is possible with the provided fields. Exact-normalized deduplication does not remove all paraphrases. The fixed pretrained encoder may have encountered related material during pretraining; this cannot be ruled out from the model card.')
    para('<b>Statistical limits.</b> The test contains four repeated normalized-text rows and one conflicting-label group. A deduplicated/unambiguous sensitivity check is reported separately. Row-level intervals condition on the benchmark and may understate uncertainty from latent grouping. The calibration diagnostic and authored OOD probes do not establish universal reliability or safety.')
    para('<b>Next experiment.</b> Obtain a permitted, genuinely new institution/time-period sample; define intended intents and unknown categories before annotation; compare the frozen baseline with an explicit domain-rejection model. Measure accepted-intent error, unknown-query rejection and human review time prospectively. Set tolerances with the team that bears the error cost. Do not infer cost savings from benchmark coverage alone.')
    title('Sources and reproducibility')
    para('[1] Casanueva, I., Temcinas, T., Gerz, D., Henderson, M., and Vulic, I. (2020). Efficient Intent Detection with Dual Sentence Encoders. NLP4ConvAI. BANKING77 dataset, CC BY 4.0.<br/><link href="https://aclanthology.org/2020.nlp4convai-1.5/">aclanthology.org/2020.nlp4convai-1.5/</link><br/><link href="https://github.com/PolyAI-LDN/task-specific-datasets">github.com/PolyAI-LDN/task-specific-datasets</link>','CaptionAtlas')
    para('[2] Sentence Transformers. all-MiniLM-L6-v2 model card and ONNX weights, Apache-2.0. Pinned revision and file hashes are retained in source_manifest.json.<br/><link href="https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2">huggingface.co/sentence-transformers/all-MiniLM-L6-v2</link>','CaptionAtlas')
    para('[3] Guo, C., Pleiss, G., Sun, Y., and Weinberger, K. Q. (2017). On Calibration of Modern Neural Networks. ICML. Temperature-scaling motivation; this implementation fits only one scalar per pipeline.<br/><link href="https://proceedings.mlr.press/v70/guo17a.html">proceedings.mlr.press/v70/guo17a.html</link>','CaptionAtlas')
    para('Primary project evidence: PROTOCOL.md; source_manifest.json; split_manifest.csv; policy_lock.json; predictions.csv; metrics.json; independent_audit.json; queries.sql. Source code and reproducibility instructions are included in the portfolio repository.','CaptionAtlas')
    def footer(canvas,doc):
        canvas.setStrokeColor(colors.HexColor('#dbe4e7'));canvas.line(45,37,567,37);canvas.setFont('Helvetica',8);canvas.setFillColor(colors.HexColor(GRAY));canvas.drawString(45,24,'BANKING INTENT ATLAS  /  Independent, AI-assisted benchmark study');canvas.drawRightString(567,24,str(doc.page))
    SimpleDocTemplate(str(WEB/'Banking_Intent_Atlas.pdf'),pagesize=(612,792),rightMargin=57,leftMargin=57,topMargin=45,bottomMargin=52,title='Banking Intent Atlas: Knowing when an NLP router should defer',author='James N. Jean IV; AI-assisted implementation').build(story,onFirstPage=footer,onLaterPages=footer)
    (O/'paper_text.md').write_text('\n\n'.join(narrative),encoding='utf-8')

def web_data():
    conn=sqlite3.connect(ROOT/'data/atlas.sqlite'); texts=dict(conn.execute("SELECT row_id,text FROM queries WHERE split='test'"));conn.close()
    byid={r['row_id']:{} for r in P}
    label_index={s:i for i,s in enumerate(LABELS)}
    for r in P:byid[r['row_id']][r['model']]=r
    compact=[]
    for rid,models in sorted(byid.items()):
        a,b=models['lexical'],models['semantic']
        compact.append([int(rid.split('_')[1]),label_index[a['truth']],label_index[a['prediction']],round(float(a['confidence']),8),label_index[b['prediction']],round(float(b['confidence']),8)])
    selected=[]
    for mode in ['accepted_error','referred','correct']:
        candidates=[r for r in P if r['model']=='semantic' and ((mode=='accepted_error' and r['accepted']=='1' and r['correct']=='0') or (mode=='referred' and r['accepted']=='0') or (mode=='correct' and r['correct']=='1'))]
        candidates.sort(key=lambda r:(-float(r['confidence']),r['row_id']))
        for r in candidates[:8]:
            text=texts[r['row_id']]
            if re.search(r'\b\d{5,}\b|[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}|https?://',text):continue
            selected.append({'kind':mode,'text':text,'truth':r['truth'],'prediction':r['prediction'],'confidence':float(r['confidence']),'runner_up':r['runner_up'],'runner_up_probability':float(r['runner_up_probability']),'third':r['third'],'third_probability':float(r['third_probability'])})
    obj={'labels':LABELS,'rows':compact,'examples':selected,'frozen':{k:L['models'][k]['threshold'] for k in ['lexical','semantic']},'selected':L['selected_before_test'],'metrics':{k:{x:M[k][x] for x in ['accuracy','macro_f1','top3','referral']} for k in ['lexical','semantic']},'ood_probes':json.loads((O/'ood_probes.json').read_text())}
    (WEB/'evidence.json').write_text(json.dumps(obj,separators=(',',':')),encoding='utf-8')
    manifest={p.name:{'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()} for p in WEB.iterdir() if p.is_file()}
    (O/'presentation_manifest.json').write_text(json.dumps(manifest,indent=2))

if __name__=='__main__':
    charts();paper();web_data()
    print(json.dumps({'paper':str(WEB/'Banking_Intent_Atlas.pdf'),'web_bytes':sum(p.stat().st_size for p in WEB.iterdir() if p.is_file())}))

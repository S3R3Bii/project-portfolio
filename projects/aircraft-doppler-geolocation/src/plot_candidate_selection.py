"""Explain ranking from anonymized frozen predictions; no fitting or selection by reference."""
from pathlib import Path
import os
os.environ.setdefault('MPLCONFIGDIR','/tmp/mpl_candidate_selection')
import numpy as np,pandas as pd
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
P=Path(__file__).resolve().parent
DATA=P/'public' if (P/'public').exists() else P.parent/'data'
OUT=P/'figures' if (P/'public').exists() else P.parent/'figures'
OUT.mkdir(exist_ok=True)
D=pd.read_csv(DATA/'top_candidate_prediction_comparison.csv')
plt.rcParams.update({'font.family':'DejaVu Serif','font.size':9,'axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'white','axes.facecolor':'white'})
ink='#252c30';red='#A84B32';blue='#356579';olive='#998652';grey='#babbb5';gap='#eeeae3'
fig,axes=plt.subplots(3,2,figsize=(9.15,8.25),gridspec_kw={'height_ratios':[1.13,1.55,.95]},layout='constrained')
for col,(model,title) in enumerate([('constant','Constant emitted spacing'),('bounded_3pct_drift','Up to 3% emitted-spacing drift')]):
 d=D[D.source_model==model];summary=d.groupby(['rank','label'],as_index=False).candidate_rms_hz.first().sort_values('rank');bar,curve,res=axes[:,col]
 bar.set_title(title,fontweight='bold',pad=14)
 yy=np.arange(len(summary));bars=bar.barh(yy,summary.candidate_rms_hz,color=[red,blue,olive,grey,grey],height=.58)
 bar.set_yticks(yy,[f"{int(r['rank'])}   {r['label']}"for _,r in summary.iterrows()]);bar.invert_yaxis();bar.set_xlim(0,.175);bar.set_xlabel('Best curve RMS (Hz)  ·  lower is better');bar.set_xticks([0,.05,.10,.15]);bar.grid(axis='x',alpha=.12);bar.set_axisbelow(True)
 for i,(_,r) in enumerate(summary.iterrows()):bar.text(r.candidate_rms_hz+.003,i,f"{r.candidate_rms_hz:.4f}",va='center',fontsize=9)
 first=d[d['rank']==1];curve.scatter(first.elapsed_s,first.measured_spacing_hz,s=11,color=ink,label='Measured audio',zorder=5)
 for rank,color,style in [(1,red,'-'),(2,blue,'--'),(3,olive,':')]:
  q=d[d['rank']==rank];label=q.label.iloc[0]
  for j,clip in enumerate([1,2]):
   c=q[q.clip_index==clip];curve.plot(c.elapsed_s,c.predicted_spacing_hz,color=color,ls=style,lw=1.7 if rank==1 else 1.4,label=f'{rank}  {label}'if j==0 else None)
   res.plot(c.elapsed_s,c.residual_hz,color=color,ls=style,lw=1.5 if rank==1 else 1.2)
 for a in [curve,res]:a.axvspan(69.84,85,color=gap,zorder=-5);a.grid(axis='y',alpha=.12);a.set_xlim(0,160.465)
 curve.set_ylim(18.3,26.8);curve.set_ylabel('Common spacing (Hz)');curve.tick_params(labelbottom=False);curve.legend(loc='lower left',frameon=False,fontsize=8,ncol=2);curve.text(77.42,26.65,'missing\naudio',ha='center',va='top',fontsize=7.4,color='#65655f')
 res.axhline(0,color=ink,lw=.7);res.set_ylim(-.52,.52);res.set_ylabel('Prediction − measurement (Hz)',fontsize=8);res.set_xlabel('Elapsed reception time (s)');res.set_xticks([0,40,80,120,160])
 margin=summary.iloc[1].candidate_rms_hz-summary.iloc[0].candidate_rms_hz
 res.text(.03,.94,f'RMS advantage over runner-up: {margin:.4f} Hz',transform=res.transAxes,va='top',fontsize=7.9)
for ext in ['pdf','png']:fig.savefig(OUT/f'candidate_selection.{ext}',dpi=300,bbox_inches='tight')
plt.close(fig)
print('Saved candidate_selection.pdf/png. Rows and curves are frozen search outputs, not new fits.')

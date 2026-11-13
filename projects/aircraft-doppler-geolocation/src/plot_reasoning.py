"""Figure 4 and star-key revisions, using only anonymous retained score data.
Grid sketches are conceptual, not maps or confidence regions.
"""
from pathlib import Path
import os,json,shutil
os.environ['MPLCONFIGDIR']='/tmp/mpl_reasoning'
import numpy as np,pandas as pd
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon,Rectangle
from matplotlib.lines import Line2D
P=Path(__file__).resolve().parents[1];BASE=P;D=pd.read_csv(P/'data/corrected_candidate_scores.csv');S=json.load(open(P/'data/corrected_search_summary.json'));O=P/'figures';O.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Serif','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'white','axes.facecolor':'white'})
blue='#356579';red='#A84B32';grey='#9c9c94';ink='#252c30';pale='#EDF2F2'
def save(fig,name):
 fig.tight_layout()
 for ext in ['pdf','png']:
  f=O/f'{name}.{ext}';fig.savefig(f,dpi=260,bbox_inches='tight')

 plt.close(fig)
# Funnel and spatial lane: every count is read from the preserved public summary.
fig=plt.figure(figsize=(8.3,5.5));ax=fig.add_axes([.025,.02,.95,.95]);ax.set(xlim=(0,10),ylim=(0,10));ax.axis('off')
ax.text(0,9.95,'KNOWN INPUTS',fontsize=9,color=blue,va='top');ax.text(0,9.5,'Measured sound + capture-time metadata',fontsize=11,va='top')
ax.text(0,9.08,'Date/time prior; capture-clock offset ±2 s',fontsize=8.2,color='#5d6365',va='top')
ax.text(6.25,9.95,'UNKNOWNS IN THE SEARCH',fontsize=9,color=red,va='top');ax.text(6.25,9.5,'Aircraft + observer position',fontsize=11,va='top');ax.text(6.25,9.08,'No supplied identity or coordinate priors',fontsize=8.2,color='#5d6365',va='top')
ax.plot([0,10],[8.72,8.72],color='#c9d0d1',lw=.8)
rows=[(f"{S['archive_files']:,}",'Daily archive trajectories'),(f"{S['coarse_aircraft']:,}",'Airborne tracks in source-time window'),(f"{S['coarse_covered_aircraft']:,}",'At least one covered coarse geometry'),(f"{S['selected_for_refinement']:,}",'Refined: union of four top-200 lists'),('358 / source model','Ranked after full-curve refinement')]
widths=[5.8,5.4,4.9,4.35,3.8];ys=[8.05,6.95,5.85,4.75,3.65]
for i,((count,lab),width,y)in enumerate(zip(rows,widths,ys)):
 center=2.98;x0=center-width/2;x1=center+width/2;bottom=width-.28;ax.add_patch(Polygon([[x0,y+.4],[x1,y+.4],[center+bottom/2,y-.4],[center-bottom/2,y-.4]],closed=True,facecolor=pale if i<4 else '#E3ECEE',edgecolor=blue,lw=.8));ax.text(center,y+.11,count,ha='center',va='center',fontsize=14 if i<4 else 12,color=blue);ax.text(center,y-.20,lab,ha='center',va='center',fontsize=8.5)
 if i<4:ax.annotate('',xy=(center,y-.67),xytext=(center,y-.43),arrowprops={'arrowstyle':'->','color':grey,'lw':.9})
ax.text(2.98,2.93,'359 covered in either model; 357 in both',ha='center',fontsize=8,color='#5d6365')
# Nongeographic grid illustrations explain spatial refinement, not empirical posteriors.
ax.text(6.2,8.25,'SPATIAL SEARCH (schematic)',fontsize=9,color=blue)
def grid(x,y,cell,n,marked):
 for i in range(n):
  for j in range(n):ax.add_patch(Rectangle((x+i*cell,y+j*cell),cell,cell,facecolor='#D6E1E4'if(i,j)in marked else'white',edgecolor='#9eb4bb',lw=.45))
grid(6.3,6.5,.22,5,[(2,2),(3,2)]);ax.text(7.65,7.15,'Each path segment',fontsize=10);ax.text(7.65,6.78,'±12 km domain\n1 km coarse cells',fontsize=9,va='top');ax.annotate('',xy=(6.85,5.93),xytext=(6.85,6.37),arrowprops={'arrowstyle':'->','color':grey})
grid(6.3,4.65,.16,7,[(2,3),(3,3),(4,3)]);ax.text(7.65,5.3,'Selected modes',fontsize=10);ax.text(7.65,4.92,'250 m → 100 m\nrefinement steps',fontsize=9,va='top');ax.annotate('',xy=(6.85,4.1),xytext=(6.85,4.49),arrowprops={'arrowstyle':'->','color':grey})
ax.scatter([6.48,7.08],[3.60,3.60],s=[72,55],facecolor=[red,'white'],edgecolor=red,zorder=4);ax.plot([6.48,7.08],[3.6,3.6],color=grey,ls=':',lw=1);ax.text(7.65,3.85,'Post-freeze spatial check',fontsize=10);ax.text(7.65,3.45,'Alternative ≈2.5 km away\nNo confidence radius',fontsize=8.8,va='top')
ax.plot([0,10],[2.52,2.52],color='#c9d0d1',lw=.8)
ax.text(.05,2.14,'FREEZE SCORES',fontsize=9,color=blue);ax.text(3.2,2.14,'THEN COMPARE WITH THE SUPPLIED REFERENCE',fontsize=9,color=blue)
ax.text(.05,1.69,'Same RMS winner\nin both source models',fontsize=11,va='top');ax.annotate('',xy=(3.05,1.30),xytext=(2.48,1.30),arrowprops={'arrowstyle':'->','color':blue,'lw':1.2})
ax.text(3.2,1.69,'Matches A-27, the supplied aircraft',fontsize=11,va='top',color=red);ax.text(3.2,1.25,'RMS rank 1 / 358; pixel ranks 2 / 358 and 5 / 358',fontsize=9,va='top');ax.text(3.2,.88,'Observer estimates: 56.5 m / 79.1 m from approximate reference',fontsize=8.9,va='top')
ax.text(0,.20,'References were already known to investigators. This is post-disclosure analysis, not a new blind test.',fontsize=8.4,color='#5d6365')
for ext in ['pdf','png']:
 f=O/f'flow_counts.{ext}';fig.savefig(f,dpi=260,bbox_inches='tight');

plt.close(fig)
# Explicit star keys for every star-bearing figure.
toptypes=D.type.value_counts().head(6).index.tolist();colors=['#356579','#A84B32','#998652','#6D6692','#5B8771','#A36F7C'];cm=dict(zip(toptypes,colors));cm['Unknown']='#292b2c';star=Line2D([],[],marker='*',markersize=11,markerfacecolor=red,markeredgecolor=ink,linestyle='None',label='A-27: supplied reference aircraft')
fig,axes=plt.subplots(1,2,figsize=(9,4.15),sharey=True)
for ax,prefix,title in zip(axes,['constant','drift3'],['Constant emitted spacing','Up to 3% emitted-spacing drift']):
 for typ in toptypes+['Unknown','Other types']:
  q=D[D.type==typ]if typ!='Other types'else D[~D.type.isin(toptypes+['Unknown'])];ax.scatter(q[prefix+'_rms_score'],q[prefix+'_brightness_score'],s=18,color=cm.get(typ,'#b4b5b1'),alpha=.7,label=typ,linewidths=0)
 q=D[D.label=='A-27'].iloc[0];ax.scatter(q[prefix+'_rms_score'],q[prefix+'_brightness_score'],s=115,marker='*',facecolor=red,edgecolor=ink,zorder=5);ax.legend(handles=[star],loc='upper right',frameon=False,fontsize=7.2);ax.text(.97,.875,'RMS rank 1; pixel rank '+str(int(q[prefix+'_brightness_rank'])),transform=ax.transAxes,ha='right',va='top',fontsize=8);ax.set(xscale='log',xlabel='Curve RMS error (Hz, lower is better)',title=title);ax.grid(alpha=.12)
axes[0].set_ylabel('Profiled spectral contrast (dB, higher is better)');handles,labels=axes[1].get_legend_handles_labels();fig.legend(handles,labels,loc='lower center',ncol=4,frameon=False,fontsize=8,bbox_to_anchor=(.5,-.09));save(fig,'score_scatter')
vc=D.type.value_counts();order=list(vc.head(9).index)+['Other'];ns=[int(vc[x])for x in order[:-1]]+[int(vc.iloc[9:].sum())];fig,axes=plt.subplots(1,2,figsize=(8.7,4.1),gridspec_kw={'width_ratios':[1,1.5]});yy=np.arange(len(order));axes[0].barh(yy,ns,color=[cm.get(x,grey)for x in order]);axes[0].set_yticks(yy,order);axes[0].invert_yaxis();axes[0].set_xlabel('Selected aircraft');axes[0].set_title('Archive-reported type codes')
for i,n in enumerate(ns):axes[0].text(n+.5,i,str(n),va='center',fontsize=8)
for i,typ in enumerate(order):
 q=D[D.type==typ]if typ!='Other'else D[~D.type.isin(order[:-1])];vals=q.drift3_rms_score.dropna().values;axes[1].scatter(vals,np.full(len(vals),i)+np.linspace(-.17,.17,len(vals)),s=11,color=cm.get(typ,grey),alpha=.7)
idx=order.index('P28A')if'P28A'in order else order.index('Other');target=D[D.label=='A-27'].iloc[0];axes[1].scatter(target.drift3_rms_score,idx,marker='*',s=120,color=red,edgecolor=ink,zorder=5);axes[1].set_yticks(yy,order);axes[1].invert_yaxis();axes[1].set_xscale('log');axes[1].set_xlabel('Curve RMS with drift (Hz)');axes[1].set_title('Type does not uniquely determine the curve');axes[1].grid(axis='x',alpha=.13);fig.legend(handles=[star],loc='lower center',bbox_to_anchor=(.5,-.06),frameon=False,fontsize=9);save(fig,'type_comparison')
print('Updated funnel and two explicitly keyed star plots. No numerical fitting performed.')

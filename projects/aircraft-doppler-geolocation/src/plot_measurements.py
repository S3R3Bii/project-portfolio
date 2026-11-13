"""Regenerate an actual measured curve and an anonymous all-candidate plot."""
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
P=Path(__file__).resolve().parents[1];(P/'figures').mkdir(exist_ok=True)
a=pd.read_csv(P/'data/measured_curve.csv')
fig,ax=plt.subplots(figsize=(8,4))
for clip in [1,2]:
    q=a[a.clip_index.eq(clip)];ax.plot(q.elapsed_s,q.common_spacing_hz,'o-',ms=3,color='#a54a2e')
ax.axvspan(69.84,85,color='#e9e7e2');ax.set_xlabel('Elapsed reception time (s)');ax.set_ylabel('Measured common harmonic spacing (Hz)');fig.tight_layout();fig.savefig(P/'figures/reproduced_measured_curve.png',dpi=200)
s=pd.read_csv(P/'data/corrected_candidate_scores.csv');types=list(s.type.value_counts().head(6).index);colors={t:plt.get_cmap('tab10')(i)for i,t in enumerate(types)}
fig,axs=plt.subplots(1,2,figsize=(10,4),sharey=True)
for ax,prefix in zip(axs,['constant','drift3']):
    for typ,q in s.groupby('type'):ax.scatter(q[prefix+'_rms_score'],q[prefix+'_brightness_score'],s=25,c=[colors.get(typ,'#b4b5b1')],label=typ)
    r=s[s.label.eq('A-27')].iloc[0];ax.scatter([r[prefix+'_rms_score']],[r[prefix+'_brightness_score']],s=140,facecolor='none',edgecolor='black');ax.set_title('Constant pitch'if prefix=='constant'else'Up to 3% pitch drift');ax.set_xlabel('Ridge RMS (Hz)');ax.set_xscale('log')
axs[0].set_ylabel('Profiled spectral contrast (dB)');fig.tight_layout();fig.savefig(P/'figures/reproduced_candidate_scores.png',dpi=200)
print('Wrote measured-curve and candidate-score figures')

"""Conceptual geometry, not measured candidate locations or a map."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
P=Path(__file__).resolve().parents[1]
plt.rcParams.update({'font.family':'DejaVu Serif','font.size':10})
fig,axes=plt.subplots(1,2,figsize=(10,4.4))
blue='#356579'; orange='#A84B32'; gray='#67717a'
for ax,g,label in zip(axes,[1.0,2.0],['Candidate A','Candidate B']):
 ax.set_xlim(-1.6,6.8);ax.set_ylim(-.7,6);ax.axis('off')
 ax.plot([-1.5,6],[0,0],color=blue,lw=1);ax.text(2.2,-.42,'Common approximate MSL datum',ha='center',fontsize=9,color=blue)
 x=4.3;Ha=5;h=.3;y=g+h
 ax.fill_between([3.1,3.8,4.3,4.8,5.8],[g-.3,g,g,g-.1,g-.2],0,color='#dbe2d8')
 ax.plot([3.1,3.8,4.3,4.8,5.8],[g-.3,g,g,g-.1,g-.2],color=gray,lw=1.1)
 ax.plot([x,x],[g,y],color='black',lw=2);ax.scatter([x],[y],color='black',s=20,zorder=5)
 ax.scatter([0],[Ha],marker='>',s=100,color=blue);ax.text(.2,Ha+.25,'Aircraft',fontsize=10,color=blue)
 ax.annotate('',(0,0),(0,Ha),arrowprops={'arrowstyle':'<->','color':blue,'lw':1.4});ax.text(-.16,Ha/2,r'$H_a$'+'\nAircraft altitude\nabove sea level',ha='right',va='center',fontsize=9,color=blue)
 ax.plot([0,x],[Ha,Ha],color=gray,ls=':',lw=.8);ax.plot([0,x],[y,y],color=gray,ls=':',lw=.8)
 ax.annotate('',(x+.8,0),(x+.8,g),arrowprops={'arrowstyle':'<->','color':gray});ax.text(x+.9,g/2,r'$E_g$'+'\nGround\nelevation',fontsize=9,va='center',color=gray)
 ax.annotate('',(x,Ha),(x,y),arrowprops={'arrowstyle':'<->','color':orange,'lw':1.5});ax.text(x+.1,(Ha+y)/2,r'$\Delta H$'+'\nVertical gap',fontsize=9,va='center',color=orange)
 ax.plot([0,x],[Ha,y],color=blue,lw=2);angle=np.degrees(np.arctan2(y-Ha,x));ax.text(x*.48,(Ha+y)/2+.18,r'$R$: slant distance',rotation=angle,rotation_mode='anchor',ha='center',fontsize=10,color=blue)
 ax.annotate('',(0,y-.2),(x,y-.2),arrowprops={'arrowstyle':'<->','color':gray});ax.text(x/2,y-.53,r'$d$: horizontal separation',ha='center',fontsize=9,color=gray)
 ax.annotate(r'$h_o=1.5$ m',(x,y),(x-1.5,g-.7),fontsize=9,ha='center',arrowprops={'arrowstyle':'-','color':gray,'connectionstyle':'angle,angleA=0,angleB=-90,rad=5'})
 ax.set_title(label+' | different terrain elevation',fontsize=11,pad=10)
fig.text(.5,.025,r'$\Delta H=H_a-(E_g+h_o)$     |     $R\approx\sqrt{d^2+\Delta H^2}$',ha='center',fontsize=13)
fig.subplots_adjust(bottom=.16,wspace=.4,left=.11,right=.96,top=.86)
fig.savefig(P/'figures/geometry.pdf',bbox_inches='tight');fig.savefig(P/'figures/geometry.png',dpi=160,bbox_inches='tight')

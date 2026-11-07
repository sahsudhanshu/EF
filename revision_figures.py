"""Render report figures from verified full-precision analysis and model assumptions."""
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

OUT=Path('Group_31/revised/figures'); OUT.mkdir(parents=True,exist_ok=True)
A=json.loads(Path('Group_31_analysis_audit.json').read_text())
D={r['comparison']:r for r in A['descriptives']}
def v(k): return D[k]['weighted_percent']
BLUE='#2463A0'; TEAL='#16877F'; GRAY='#E7EDF2'; NAVY='#142C43'; AMBER='#AD6A12'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'text.color':NAVY,'axes.labelcolor':NAVY,'xtick.color':'#526272','ytick.color':NAVY,'axes.spines.top':False,'axes.spines.right':False,'axes.spines.left':False,'axes.spines.bottom':False,'figure.facecolor':'white'})
def finish(fig,name):
    fig.savefig(OUT/name,dpi=240,bbox_inches='tight',facecolor='white',pad_inches=.06); plt.close(fig)
def group(name,labels,a,b,legend):
    fig,ax=plt.subplots(figsize=(8.6,2.55)); y=np.arange(len(labels)); h=.29
    for off,vals,c,lab in [(-h/2,a,TEAL,legend[0]),(h/2,b,BLUE,legend[1])]:
        bars=ax.barh(y+off,vals,h,color=c,label=lab)
        ax.bar_label(bars,labels=[f'{q:.1f}%' for q in vals],padding=4,fontsize=10,fontweight='bold')
    ax.set_yticks(y,labels); ax.invert_yaxis(); ax.set_xlim(0,104); ax.set_xticks([0,25,50,75,100]); ax.set_xlabel('Survey-weighted share (%)',fontsize=9)
    ax.xaxis.grid(True,color=GRAY); ax.set_axisbelow(True); ax.tick_params(axis='both',length=0)
    ax.legend(loc='upper center',bbox_to_anchor=(.51,1.19),ncol=2,frameon=False,fontsize=10)
    fig.subplots_adjust(left=.27,right=.94,top=.85,bottom=.20); finish(fig,name)
group('figure1.png',['Account ownership','Made or received\na digital payment','Phone ownership'],[v(f'female=1: {q}') for q in ['account','anydigpayment','con1']],[v(f'female=2: {q}') for q in ['account','anydigpayment','con1']],['Women','Men'])
group('figure2.png',['Made or received\na digital payment','Phone has a lock'],[v('inc_q=1: anydigpayment'),v('Phone owners, inc_q=1: con18')],[v('inc_q=5: anydigpayment'),v('Phone owners, inc_q=5: con18')],['Lowest income quintile','Highest income quintile'])
fig,ax=plt.subplots(figsize=(8.6,2.1))
vals=[v('Phone owners, anydigpayment=1: con21'),v('Phone owners, anydigpayment=0: con21')]
bars=ax.barh([1,0],vals,.48,color=[BLUE,TEAL]);ax.set_yticks([1,0],['Digital-payment users\n(n = 1,283)','Non-users\n(n = 862)']); ax.set_xlim(0,16);ax.set_xticks([0,4,8,12,16]);ax.set_xlabel('Reported unsolicited request (%)',fontsize=9)
ax.bar_label(bars,labels=[f'{q:.1f}%' for q in vals],padding=5,fontweight='bold');ax.xaxis.grid(True,color=GRAY);ax.set_axisbelow(True);ax.tick_params(axis='both',length=0);fig.subplots_adjust(left=.27,right=.96,top=.95,bottom=.25);finish(fig,'figure3.png')

F=json.loads(Path('Group_31/revised/financial_model.json').read_text())
fig,ax=plt.subplots(figsize=(8.6,2.6))
for scenario,c,marker in [('Conservative',AMBER,'s'),('Base',BLUE,'o'),('Optimistic',TEAL,'D')]:
    rows=[r for r in F['projection'] if r['scenario']==scenario]
    ax.plot([1,2,3],[r['surplus_lakh'] for r in rows],color=c,marker=marker,linewidth=2.2,label=scenario)
ax.axhline(0,color='#697784',lw=.8);ax.set_xticks([1,2,3],['Year 1','Year 2','Year 3']);ax.set_ylabel('Operating surplus / deficit\n(INR lakh)',fontsize=9);ax.yaxis.grid(True,color=GRAY);ax.set_axisbelow(True);ax.legend(loc='upper left',ncol=3,frameon=False,fontsize=9);ax.tick_params(length=0);fig.subplots_adjust(left=.15,right=.97,top=.94,bottom=.17);finish(fig,'figure4.png')

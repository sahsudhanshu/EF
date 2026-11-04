import csv, os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
os.makedirs('Group_31/figures',exist_ok=True)
with open('Group_31_weighted_results.csv',encoding='utf-8-sig') as f: data={r['comparison']:float(r['weighted_percent']) for r in csv.DictReader(f)}
navy='#102a49'; blue='#246bb2'; teal='#15998a'; amber='#ec9e08'; orange='#e4510c'; gray='#e4ebf1'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'axes.spines.left':False,'axes.labelcolor':navy,'text.color':navy,'xtick.color':'#617387','ytick.color':navy,'figure.facecolor':'white'})
def save(fig,name):
    fig.savefig('Group_31/figures/'+name,dpi=200,bbox_inches='tight',facecolor='white'); plt.close(fig)
def foot(fig,note):fig.text(.07,.035,note+'\nSource: Global Findex India 2024; Group 31 weighted calculations.',fontsize=8,color='#5b6e80')
fig,axes=plt.subplots(1,2,figsize=(9,4.7));fig.suptitle('Financial access and digital use',x=.08,y=.97,ha='left',fontsize=16,fontweight='bold',color=navy)
for ax,v,title,c in zip(axes,[data['All adults: account'],data['All adults: anydigpayment']],['Account ownership','Made or received a digital payment'],[blue,teal]):
    ax.pie([v,100-v],startangle=90,counterclock=False,colors=[c,gray],wedgeprops={'width':.25,'edgecolor':'white'},radius=1)
    ax.text(0,0,f'{v:.1f}%',ha='center',va='center',fontsize=23,fontweight='bold',color=navy);ax.set_title(title,fontsize=11,fontweight='bold',pad=14);ax.set_aspect('equal')
foot(fig,'Each ring is a separate share of all adults, n = 3,000. Grey is the remainder.');fig.subplots_adjust(top=.79,bottom=.20,wspace=.12);save(fig,'fig1_access_and_use.png')
fig,ax=plt.subplots(figsize=(9,4.7));vals=[data['Phone owners, anydigpayment=1: con21'],data['Phone owners, anydigpayment=0: con21']];bars=ax.barh(['Digital-payment users','Non-users'][::-1],vals[::-1],height=.5,color=[orange,blue]);ax.set_xlim(0,17);ax.set_xlabel('Reported unsolicited request (%)');ax.set_title('Requests for money by digital payment use',loc='left',fontsize=15,fontweight='bold',pad=15);ax.bar_label(bars,labels=[f'{x:.1f}%' for x in vals[::-1]],padding=6,fontweight='bold',color=navy);ax.xaxis.grid(True,color=gray);ax.set_axisbelow(True);foot(fig,'Phone owners: users n = 1,283; non-users n = 862. Requests are not verified fraud.');fig.subplots_adjust(left=.28,right=.95,top=.80,bottom=.23);save(fig,'fig2_exposure.png')
def grouped(name,title,groups,series,notes):
    fig,ax=plt.subplots(figsize=(9,4.8));y=np.arange(len(groups)); h=.27
    a=ax.barh(y-h/2,series[0][1],height=h,color=series[0][2],label=series[0][0]);b=ax.barh(y+h/2,series[1][1],height=h,color=series[1][2],label=series[1][0]);ax.invert_yaxis();ax.set_yticks(y,groups);ax.set_xlim(0,100);ax.set_xlabel('Weighted share (%)');ax.set_title(title,loc='left',fontsize=15,fontweight='bold',pad=14);ax.bar_label(a,labels=[f'{v:.1f}%' for v in series[0][1]],padding=3,fontsize=9);ax.bar_label(b,labels=[f'{v:.1f}%' for v in series[1][1]],padding=3,fontsize=9);ax.legend(loc='upper center',bbox_to_anchor=(.5,-.2),ncol=2,frameon=False);ax.xaxis.grid(True,color=gray);ax.set_axisbelow(True);foot(fig,notes);fig.subplots_adjust(left=.24,right=.94,top=.83,bottom=.31);save(fig,name)
grouped('fig3_gender.png','Gender differences in use and protection',['Made or received payment','Phone has a lock'],[('Women',[data['female=1: anydigpayment'],data['Phone owners, female=1: con18']],teal),('Men',[data['female=2: anydigpayment'],data['Phone owners, female=2: con18']],blue)],'Payment: all adults. Phone lock: valid responses among phone owners.')
grouped('fig4_income.png','Income differences in use and protection',['Made or received payment','Phone has a lock'],[('Lowest quintile',[data['inc_q=1: anydigpayment'],data['Phone owners, inc_q=1: con18']],teal),('Highest quintile',[data['inc_q=5: anydigpayment'],data['Phone owners, inc_q=5: con18']],blue)],'Payment: all adults. Phone lock: valid responses among phone owners.')

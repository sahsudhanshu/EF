"""Reproduce Group 31 weighted descriptive analysis (Global Findex India v02)."""
import pandas as pd
import numpy as np
from pathlib import Path

df=pd.read_stata('data/Findex_Microdata_2025_updateIndia.dta',convert_categoricals=False)
assert len(df)==3000 and (df.wgt>0).all()
df['age_group']=pd.cut(df.age,[14,24,39,59,120],labels=['15–24','25–39','40–59','60+'])
assert ((df.con21==1)==df.con22.notna()).all()
rows=[]
audit_rows=[]
def add(label, mask, outcome, positive):
    z=df.loc[mask & df[outcome].isin([0,1] if outcome in ['account','anydigpayment'] else [1,2])]
    value=100*np.average((z[outcome]==positive).astype(float),weights=z.wgt)
    rows.append(dict(comparison=label, n=len(z), positives=int((z[outcome]==positive).sum()), weighted_percent=round(value,2)))
    audit_rows.append(dict(comparison=label, n=len(z), positives=int((z[outcome]==positive).sum()), weighted_percent=float(value), weight_denominator=float(z.wgt.sum()), weight_numerator=float(z.loc[z[outcome]==positive,'wgt'].sum())))
allrows=pd.Series(True,index=df.index)
phone=df.con1.eq(1)
for var,positive in [('account',1),('anydigpayment',1),('con1',1)]: add('All adults: '+var,allrows,var,positive)
for var in ['con18','con21']: add('Phone owners: '+var,phone,var,1)
add('Reported unsolicited request: con22',df.con21.eq(1),'con22',1)
for status in [0,1]:
    for var in ['con21','con18']:
        add(f'Phone owners, anydigpayment={status}: {var}',phone & df.anydigpayment.eq(status),var,1)
for g in [1,2]:
    for var in ['account','anydigpayment','con1']:
        add(f'female={g}: {var}',df.female.eq(g),var,1)
    for var in ['con18','con21']:
        add(f'Phone owners, female={g}: {var}',phone & df.female.eq(g),var,1)
for col,values in [('age_group',['15–24','25–39','40–59','60+']),('educ',[1,2,3]),('inc_q',[1,2,3,4,5]),('urbanicity',[1,2]),('emp_in',[1,2])]:
    for value in values:
        add(f'{col}={value}: anydigpayment',df[col].eq(value),'anydigpayment',1)
        for var in ['con18','con21']:
            add(f'Phone owners, {col}={value}: {var}',phone & df[col].eq(value),var,1)
for v in [1,2]:
    add(f'Unsolicited request, phone lock={v}: sent money',df.con21.eq(1)&df.con18.eq(v),'con22',1)
out=pd.DataFrame(rows); out.to_csv('Group_31_weighted_results.csv',index=False)
print(out.to_string(index=False))

# Exploratory weighted logistic model; robust errors assume independent observations.
# The public file contains no strata or PSU identifiers, so these are not design-based.
from math import erfc, sqrt
z=df.loc[phone & df.con21.isin([1,2])].copy()
X=pd.DataFrame({'Intercept':1., 'Digital payment':z.anydigpayment, 'Female':(z.female==1).astype(float),
                'Age per 10 years':z.age/10, 'Secondary education':(z.educ==2).astype(float),
                'Tertiary education':(z.educ==3).astype(float), 'Income quintile':z.inc_q.astype(float),
                'In workforce':(z.emp_in==1).astype(float), 'Urban':(z.urbanicity==2).astype(float)},index=z.index)
valid=X.notna().all(axis=1) & z.wgt.notna(); X=X.loc[valid]; z=z.loc[valid]
x=X.to_numpy(); y=(z.con21==1).to_numpy(dtype=float); w=z.wgt.to_numpy(); b=np.zeros(x.shape[1])
for _ in range(100):
    p=1/(1+np.exp(-np.clip(x@b,-30,30))); h=x.T@((w*p*(1-p))[:,None]*x)
    step=np.linalg.solve(h,x.T@(w*(y-p))); b+=step
    if np.max(np.abs(step))<1e-10: break
else: raise RuntimeError('Logistic model did not converge')
p=1/(1+np.exp(-np.clip(x@b,-30,30))); bread=np.linalg.inv(x.T@((w*p*(1-p))[:,None]*x))
score=x*(w*(y-p))[:,None]; cov=bread@(score.T@score)@bread; se=np.sqrt(np.diag(cov))
model=pd.DataFrame({'variable':X.columns,'odds_ratio':np.exp(b),'low_95':np.exp(b-1.96*se),'high_95':np.exp(b+1.96*se),'p_approx':[erfc(abs(a/s)/sqrt(2)) for a,s in zip(b,se)]})
model.to_csv('Group_31_exploratory_model.csv',index=False); print('\nModel n=',len(z)); print(model.to_string(index=False))

# Full precision audit output for consistent one-decimal report rounding.
# Statistical formulas and the existing two-decimal CSV outputs are unchanged.
import json, hashlib
audit={'source':'IND_2024_FINDEX_v02_M','survey_year':2024,'n':len(df),
       'data_sha256':hashlib.sha256(Path('data/Findex_Microdata_2025_updateIndia.dta').read_bytes()).hexdigest(),
       'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'model_n':len(z),'model_positive':int(y.sum()),'iterations':_+1,
       'max_score':float(np.max(np.abs(x.T@(w*(y-p))))),
       'descriptives':audit_rows,'model':model.to_dict(orient='records')}
Path('Group_31_analysis_audit.json').write_text(json.dumps(audit,indent=2),encoding='utf-8')

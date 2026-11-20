"""Builds the PROCESSED datasets from the raw ones.
Run from the submission folder (data/raw/ must hold the raw files):  python scripts/make_processed_data.py
Outputs: data/processed/findex_india_analysis_ready.csv   (survey variables used in the paper, plus derived flags)
         data/processed/reviews_processed.csv              (cleaned app reviews with the keyword-theme flags used in the paper)"""
import re
from pathlib import Path
import numpy as np
import pandas as pd

RAW = Path('data/raw') if Path('data/raw').exists() else Path('data')
OUT = Path('data/processed'); OUT.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------- 1. survey microdata
d = pd.read_stata(RAW / 'Findex_Microdata_2025_updateIndia.dta', convert_categoricals=False)
keep = ['wgt', 'account', 'anydigpayment', 'con1', 'con18', 'con21', 'con22', 'female', 'age', 'educ', 'inc_q', 'emp_in', 'urbanicity']
p = d[keep].copy()
p['age_group'] = pd.cut(p.age, [14, 24, 39, 59, 120], labels=['15-24', '25-39', '40-59', '60+'])
p['phone_owner'] = p.con1.eq(1)
p['lock_valid_yes_no'] = p.con18.isin([1, 2]) & p.phone_owner          # eligible for the lock share
p['request_reported'] = p.con21.eq(1)
p['sent_money_after_request'] = p.con22.eq(1)
p['note'] = ''
p.drop(columns='note').to_csv(OUT / 'findex_india_analysis_ready.csv', index=False)

# ---------------------------------------------------------------- 2. app reviews (same cleaning and dictionaries as the analysis scripts)
def themes_from(script):
    src = Path(script).read_text(encoding='utf-8')
    block = src[src.index('THEMES = {'):]
    block = block[:block.index('\n}') + 2]
    ns = {}
    exec(block, ns)
    return ns['THEMES']

def friction_from(script):
    src = Path(script).read_text(encoding='utf-8')
    line = [l for l in src.splitlines() if l.startswith('FRICTION')][0]
    ns = {}
    exec(line, ns)
    return ns['FRICTION']

TH = themes_from('scripts/analysis_bankapps.py'); FR = friction_from('scripts/analysis_bankapps.py')
a = pd.read_csv(RAW / 'app_reviews.csv').dropna(subset=['text']); a['text'] = a.text.astype(str)
a = a[a.text.str.len() >= 15].drop_duplicates(subset=['app', 'text'])
a = a.assign(dataset='Payment apps, Google Play', store='Google Play')[['dataset', 'store', 'app', 'date', 'rating', 'text']]
b = pd.read_csv(RAW / 'appstore_reviews.csv').fillna('')
b['text'] = (b.title.astype(str) + '. ' + b.text.astype(str)).str.strip()
b = b.assign(dataset='Payment apps, App Store', store='App Store')[['dataset', 'store', 'app', 'date', 'rating', 'text']]
c = pd.read_csv(RAW / 'bankapps_play_reviews.csv').assign(store='Google Play')
e = pd.read_csv(RAW / 'bankapps_appstore_reviews.csv').fillna('')
e['text'] = (e.title.astype(str) + '. ' + e.text.astype(str)).str.strip(); e['store'] = 'App Store'
bank = pd.concat([c[['store', 'app', 'date', 'rating', 'text']], e[['store', 'app', 'date', 'rating', 'text']]], ignore_index=True).assign(dataset='Bank apps')
bank = bank[['dataset', 'store', 'app', 'date', 'rating', 'text']]
rv = pd.concat([a, b, bank], ignore_index=True)
rv['text'] = rv.text.astype(str)
cols = {'Fraud, scam or unauthorised transactions': 'theme_fraud', 'Money deducted or failed payment': 'theme_failed_payment', 'Support and complaint handling': 'theme_support',
        'Account blocking, verification or login barriers': 'theme_blocking_verification', 'Safety and trust language': 'theme_safety_trust'}
for name, col in cols.items():
    rv[col] = rv.text.str.contains(TH[name], case=False, regex=True)
rv['security_friction_prompt'] = rv.text.str.contains(FR, case=False, regex=True)
rv.to_csv(OUT / 'reviews_processed.csv', index=False)
print('processed:', len(p), 'survey rows;', len(rv), 'reviews', rv.dataset.value_counts().to_dict())

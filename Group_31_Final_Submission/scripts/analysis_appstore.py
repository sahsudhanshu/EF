"""Apply the same keyword themes as analysis_extra.py to the Apple App Store (India) reviews.
Run from the submission folder after fetch_appstore.py:  python scripts/analysis_appstore.py
Outputs: results/appstore_theme_counts.csv, results/appstore_summary.json, results/appstore_fraud_keyword_all.csv"""
import json
import re
from pathlib import Path
import pandas as pd

THEMES = {
    'Fraud, scam or unauthorised transactions': r'\b(fraud\w*|scam\w*|scammer\w*|cheat\w*|hack\w*|phishing|unauthori[sz]ed|stolen|fake|spam|looted|duped|thief|theft)\b',
    'Money deducted or failed payment': r'(money|amount|payment|balance)\s+(got\s+|was\s+|is\s+|has\s+been\s+|been\s+)?(deducted|debited|cut|stuck|failed|pending)|\b(deducted|debited)\b|refund|transaction\s+(failed|pending)|payment\s+failed',
    'Support and complaint handling': r'customer\s*(care|support|service)|\bsupport\b|complain\w*|helpline|grievance|no\s+response|not\s+respon\w+|\bticket\b|escalat\w+',
    'Account blocking, verification or login barriers': r'block\w*|\bkyc\b|verif\w+|\botp\b|device\s+binding|re-?login|login\s+(issue|problem)|\bsim\b|restrict\w*|suspend\w*',
    'Safety and trust language': r'\b(safe|secure|security|trust\w*|reliable|privacy)\b',
}
rv = pd.read_csv('data/appstore_reviews.csv').fillna('')
rv['full'] = (rv.title.astype(str) + '. ' + rv.text.astype(str)).str.strip()
for name, pat in THEMES.items():
    rv[name] = rv.full.str.contains(pat, case=False, regex=True)
rv['any_theme'] = rv[list(THEMES)].any(axis=1)
rows = []
for name in THEMES:
    m = rv[name]
    rows.append(dict(theme=name, reviews=int(m.sum()), share_pct=round(100 * m.mean(), 1), mean_rating=round(rv.loc[m, 'rating'].mean(), 2),
                     one_star_share_pct=round(100 * (rv.loc[m, 'rating'] == 1).mean(), 1)))
out = pd.DataFrame(rows); out.to_csv('results/appstore_theme_counts.csv', index=False); print(out.to_string(index=False))
f = list(THEMES)[0]
summary = dict(n_reviews=int(len(rv)), apps=rv.app.value_counts().to_dict(), date_min=rv.date.min(), date_max=rv.date.max(),
               mean_rating=round(rv.rating.mean(), 2), any_theme_pct=round(100 * rv.any_theme.mean(), 1),
               fraud_theme_mean_rating=round(rv.loc[rv[f], 'rating'].mean(), 2), non_fraud_mean_rating=round(rv.loc[~rv[f], 'rating'].mean(), 2))
Path('results/appstore_summary.json').write_text(json.dumps(summary, indent=2), encoding='utf-8'); print(summary)
rv[rv[f]][['app', 'date', 'rating', 'full']].rename(columns={'full': 'text'}).to_csv('results/appstore_fraud_keyword_all.csv', index=False)

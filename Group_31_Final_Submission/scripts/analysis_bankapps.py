"""Analyse public reviews of bank mobile-banking apps (Google Play and Apple App Store) and compare with the UPI payment apps.
Same five keyword themes as analysis_extra.py, plus a security-friction dictionary (device binding, SIM, root, VPN, screen sharing, biometrics).
Run after fetch_bankapps.py, from the submission folder:  python scripts/analysis_bankapps.py
Outputs: results/bankapps_theme_counts.csv, results/bankapps_theme_by_store.csv, results/bankapps_summary.json,
         results/bankapps_fraud_keyword_all.csv, results/bankapps_security_friction.csv"""
import json
from pathlib import Path
import pandas as pd

THEMES = {
    'Fraud, scam or unauthorised transactions': r'\b(?:fraud\w*|scam\w*|scammer\w*|cheat\w*|hack\w*|phishing|unauthori[sz]ed|stolen|fake|spam|looted|duped|thief|theft)\b',
    'Money deducted or failed payment': r'(?:money|amount|payment|balance)\s+(?:got\s+|was\s+|is\s+|has\s+been\s+|been\s+)?(?:deducted|debited|cut|stuck|failed|pending)|\b(?:deducted|debited)\b|refund|transaction\s+(?:failed|pending)|payment\s+failed',
    'Support and complaint handling': r'customer\s*(?:care|support|service)|\bsupport\b|complain\w*|helpline|grievance|no\s+response|not\s+respon\w+|\bticket\b|escalat\w+',
    'Account blocking, verification or login barriers': r'block\w*|\bkyc\b|verif\w+|\botp\b|device\s+binding|re-?login|login\s+(?:issue|problem)|\bsim\b|restrict\w*|suspend\w*',
    'Safety and trust language': r'\b(?:safe|secure|security|trust\w*|reliable|privacy)\b',
}
FRICTION = r'device\s*(?:binding|lock|bind)|screen\s*lock|\bsim\b|rooted|\broot(?:ed)?\b|developer\s*options|screen\s*(?:sharing|mirroring|record\w*)|remote\s*access|\bvpn\b|biometric|fingerprint|face\s*(?:id|lock|unlock)|two[- ]factor|\b2fa\b|security\s*(?:check|alert|risk|reasons?|restriction)|\bunsafe\b'
play = pd.read_csv('data/bankapps_play_reviews.csv').assign(store='Google Play')
ios = pd.read_csv('data/bankapps_appstore_reviews.csv').fillna('')
ios['text'] = (ios.title.astype(str) + '. ' + ios.text.astype(str)).str.strip(); ios['store'] = 'App Store'
rv = pd.concat([play[['store', 'app', 'date', 'rating', 'text']], ios[['store', 'app', 'date', 'rating', 'text']]], ignore_index=True)
rv['text'] = rv.text.astype(str)
for name, pat in THEMES.items():
    rv[name] = rv.text.str.contains(pat, case=False, regex=True)
rv['friction'] = rv.text.str.contains(FRICTION, case=False, regex=True)
rv['any_theme'] = rv[list(THEMES)].any(axis=1)
f = list(THEMES)[0]

def table(d):
    rows = []
    for name in THEMES:
        m = d[name]
        rows.append(dict(theme=name, reviews=int(m.sum()), share_pct=round(100 * m.mean(), 1), mean_rating=round(d.loc[m, 'rating'].mean(), 2),
                         one_star_share_pct=round(100 * (d.loc[m, 'rating'] == 1).mean(), 1)))
    m = d.friction
    rows.append(dict(theme='Security-friction prompts (device binding, SIM, root, VPN, screen sharing, biometrics)', reviews=int(m.sum()),
                     share_pct=round(100 * m.mean(), 1), mean_rating=round(d.loc[m, 'rating'].mean(), 2), one_star_share_pct=round(100 * (d.loc[m, 'rating'] == 1).mean(), 1)))
    return pd.DataFrame(rows)

all_t = table(rv); all_t.to_csv('results/bankapps_theme_counts.csv', index=False); print(all_t.to_string(index=False))
by = pd.concat([table(g).assign(store=s) for s, g in rv.groupby('store')]); by.to_csv('results/bankapps_theme_by_store.csv', index=False)
upi = pd.read_csv('results/review_theme_counts.csv').set_index('theme').share_pct
summary = dict(n_reviews=int(len(rv)), by_store=rv.store.value_counts().to_dict(), apps=rv.groupby(['store', 'app']).size().to_dict().__repr__(),
               date_min=rv.date.min(), date_max=rv.date.max(), mean_rating=round(float(rv.rating.mean()), 2), any_theme_pct=round(float(100 * rv.any_theme.mean()), 1),
               fraud_theme_mean_rating=round(float(rv.loc[rv[f], 'rating'].mean()), 2), non_fraud_mean_rating=round(float(rv.loc[~rv[f], 'rating'].mean()), 2),
               friction_by_app=rv.groupby('app').friction.mean().mul(100).round(1).to_dict())
Path('results/bankapps_summary.json').write_text(json.dumps(summary, indent=2, default=str), encoding='utf-8'); print({k: v for k, v in summary.items() if k != 'apps'})
rv[rv[f]][['store', 'app', 'date', 'rating', 'text']].to_csv('results/bankapps_fraud_keyword_all.csv', index=False)
rv[rv.friction][['store', 'app', 'date', 'rating', 'text']].to_csv('results/bankapps_security_friction.csv', index=False)
print('fraud-keyword reviews:', int(rv[f].sum()), '| friction reviews:', int(rv.friction.sum()))

# ---- comparison with the payment apps (Google Play + App Store reviews of PhonePe, Google Pay, Paytm, BHIM, SBI YONO), same dictionaries
pp = pd.read_csv('data/app_reviews.csv').dropna(subset=['text']); pp['text'] = pp.text.astype(str)
pp = pp[pp.text.str.len() >= 15].drop_duplicates(subset=['app', 'text'])[['app', 'date', 'rating', 'text']]
pi = pd.read_csv('data/appstore_reviews.csv').fillna(''); pi['text'] = (pi.title.astype(str) + '. ' + pi.text.astype(str)).str.strip()
pay = pd.concat([pp, pi[['app', 'date', 'rating', 'text']]], ignore_index=True)
for name, pat in THEMES.items():
    pay[name] = pay.text.str.contains(pat, case=False, regex=True)
pay['friction'] = pay.text.str.contains(FRICTION, case=False, regex=True)
tp_, tb_ = table(pay), table(rv)
cmp_ = pd.DataFrame({'theme': tb_.theme, 'bank_reviews': tb_.reviews, 'bank_share_pct': tb_.share_pct, 'bank_mean_rating': tb_.mean_rating,
                     'payment_reviews': tp_.reviews, 'payment_share_pct': tp_.share_pct, 'payment_mean_rating': tp_.mean_rating})
cmp_.to_csv('results/bank_vs_payment_themes.csv', index=False); print(cmp_.to_string(index=False)); print('payment apps n =', len(pay))

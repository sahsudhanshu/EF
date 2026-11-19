"""Peer-economy comparison and qualitative app-review coding. Run after fetch_data.py:  python analysis_extra.py
Outputs: results/peers_table.csv, results/review_theme_counts.csv, results/review_coded_sample.csv, results/review_summary.json,
         figures/figure5.png, figures/figure6.png"""
import json
import re
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

Path('results').mkdir(exist_ok=True); Path('figures').mkdir(exist_ok=True)
plt.rcParams['font.family'] = 'Times New Roman'

# ------------------------------------------------------------------ 1. peers
peers = pd.read_csv('data/wdi_peers.csv')
order = ['India', 'China', 'Indonesia', 'Bangladesh', 'Pakistan', 'Brazil', 'South Africa', 'Lower middle income', 'World']
peers = peers.set_index('economy').reindex([o for o in order if o in set(peers.economy)]).reset_index()
peers.loc[peers.economy == 'India', 'unsolicited_money_request_pct_phone_owners'] = 9.4  # authors' microdata estimate (not published in the API)
peers.round(1).to_csv('results/peers_table.csv', index=False)
print(peers.round(1).to_string(index=False))

cols = [('account_pct_adults', 'Account (% adults)'), ('own_phone_pct_adults', 'Own phone (% adults)'),
        ('phone_lock_pct_phone_owners', 'Phone lock (% phone owners)'), ('unsolicited_money_request_pct_phone_owners', 'Unsolicited money request (% phone owners)')]
fig, axes = plt.subplots(2, 2, figsize=(11, 8))
for ax, (c, t) in zip(axes.ravel(), cols):
    d = peers.dropna(subset=[c]).sort_values(c)
    colors = ['#1B8A7E' if e == 'India' else '#9FB3C8' for e in d.economy]
    ax.barh(d.economy, d[c], color=colors)
    for y, v in enumerate(d[c]): ax.text(v + 1, y, f'{v:.1f}', va='center', fontsize=11)
    ax.set_title(t, fontsize=13); ax.set_xlim(0, 110 if 'account' in c or 'phone' in c and 'lock' not in c else 100)
    for s in ('top', 'right'): ax.spines[s].set_visible(False)
    ax.tick_params(labelsize=11)
plt.tight_layout(); plt.savefig('figures/figure5.png', dpi=200); plt.close()

# ------------------------------------------------------------------ 2. reviews
rv = pd.read_csv('data/app_reviews.csv').dropna(subset=['text'])
rv['text'] = rv.text.astype(str)
rv = rv[rv.text.str.len() >= 15].drop_duplicates(subset=['app', 'text']).reset_index(drop=True)
THEMES = {
    'Fraud, scam or unauthorised transactions': r'\b(fraud\w*|scam\w*|scammer\w*|cheat\w*|hack\w*|phishing|unauthori[sz]ed|stolen|fake|spam|looted|duped|thief|theft)\b',
    'Money deducted or failed payment': r'(money|amount|payment|balance)\s+(got\s+|was\s+|is\s+|has\s+been\s+|been\s+)?(deducted|debited|cut|stuck|failed|pending)|\b(deducted|debited)\b|refund|transaction\s+(failed|pending)|payment\s+failed',
    'Support and complaint handling': r'customer\s*(care|support|service)|\bsupport\b|complain\w*|helpline|grievance|no\s+response|not\s+respon\w+|\bticket\b|escalat\w+',
    'Account blocking, verification or login barriers': r'block\w*|\bkyc\b|verif\w+|\botp\b|device\s+binding|re-?login|login\s+(issue|problem)|\bsim\b|restrict\w*|suspend\w*',
    'Safety and trust language': r'\b(safe|secure|security|trust\w*|reliable|privacy)\b',
}
for name, pat in THEMES.items():
    rv[name] = rv.text.str.contains(pat, case=False, regex=True)
rv['any_theme'] = rv[list(THEMES)].any(axis=1)
rows = []
for name in THEMES:
    m = rv[name]
    rows.append(dict(theme=name, reviews=int(m.sum()), share_pct=round(100 * m.mean(), 1), mean_rating=round(rv.loc[m, 'rating'].mean(), 2),
                     one_star_share_pct=round(100 * (rv.loc[m, 'rating'] == 1).mean(), 1)))
out = pd.DataFrame(rows); out.to_csv('results/review_theme_counts.csv', index=False); print(out.to_string(index=False))
by_app = rv.groupby('app')[list(THEMES)].mean().mul(100).round(1); by_app['n'] = rv.groupby('app').size()
by_app.to_csv('results/review_theme_by_app.csv'); print(by_app.to_string())
summary = dict(n_reviews=int(len(rv)), apps=rv.app.value_counts().to_dict(), date_min=rv.date.min(), date_max=rv.date.max(), mean_rating=round(rv.rating.mean(), 2),
               any_theme_pct=round(100 * rv.any_theme.mean(), 1), fraud_theme_mean_rating=round(rv.loc[rv[list(THEMES)[0]], 'rating'].mean(), 2),
               non_fraud_mean_rating=round(rv.loc[~rv[list(THEMES)[0]], 'rating'].mean(), 2))
Path('results/review_summary.json').write_text(json.dumps(summary, indent=2), encoding='utf-8'); print(summary)
# reproducible random sample of coded reviews for manual validation
samp = rv[rv.any_theme].sample(n=min(100, int(rv.any_theme.sum())), random_state=31)[['app', 'date', 'rating', 'text'] + list(THEMES)]
samp.to_csv('results/review_coded_sample.csv', index=False)

d = out.sort_values('share_pct')
fig, ax = plt.subplots(figsize=(9, 3.8))
ax.barh(d.theme, d.share_pct, color='#2A5FA5')
for y, v in enumerate(d.share_pct): ax.text(v + 0.3, y, f'{v:.1f}%', va='center', fontsize=10)
ax.set_xlabel('Share of reviews mentioning the theme (%)'); ax.set_xlim(0, d.share_pct.max() * 1.2)
for s in ('top', 'right'): ax.spines[s].set_visible(False)
plt.tight_layout(); plt.savefig('figures/figure6.png', dpi=200); plt.close()

# ------------------------------------------------------------------ 3. what the fraud-keyword reviews are actually about
fr = rv[rv[list(THEMES)[0]]].copy()
SUB = [('Third-party theft, hacking or phishing', r'stolen|hack\w*|unauthori[sz]ed|phishing|thief|theft|looted|duped|spam|someone|without\s+my|fraud\s+(call|message|sms|transaction)|scammer'),
       ('Reward, cashback or offer deception', r'cashback|cash\s*back|reward|coupon|offer|refer|scratch|gold\s+coin|bonus|coins?'),
       ('Failed or missing payment called fraud', r'deduct\w*|debit\w*|refund|fail\w*|pending|transaction|payment|amount|not\s+receiv\w+|money')]
def sub(t):
    for name, pat in SUB:
        if re.search(pat, t, re.I): return name
    return 'General complaint using the word (no specific incident)'
fr['subtype'] = fr.text.map(sub)
sc = fr.subtype.value_counts().rename_axis('subtype').reset_index(name='reviews'); sc['share_of_fraud_keyword_reviews_pct'] = (100 * sc.reviews / len(fr)).round(1)
sc.to_csv('results/review_fraud_subtypes.csv', index=False); fr[['app', 'date', 'rating', 'subtype', 'text']].to_csv('results/review_fraud_keyword_all.csv', index=False)
print(sc.to_string(index=False))

"""Inclusion vs cybersecurity risk by group (descriptive).
Inclusion = share of all adults in the group who made or received a digital payment.
Risk = share of phone owners in the group who reported an unsolicited money request.
Protection = share of phone owners in the group with a device lock.
Reads the audited weighted results (results/Group_31_analysis_audit.json); no microdata needed.
Outputs: results/inclusion_risk_by_group.csv, results/inclusion_risk_summary.json, figures/figure7_inclusion_vs_risk.png
Run from the submission folder:  python scripts/analysis_inclusion_risk.py"""
import json
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

rows = {d['comparison']: d for d in json.loads(Path('results/Group_31_analysis_audit.json').read_text())['descriptives']}
GROUPS = [('Sex', 'Women', 'female=1'), ('Sex', 'Men', 'female=2'),
          ('Age', '15–24', 'age_group=15–24'), ('Age', '25–39', 'age_group=25–39'), ('Age', '40–59', 'age_group=40–59'), ('Age', '60+', 'age_group=60+'),
          ('Education', 'Primary or less', 'educ=1'), ('Education', 'Secondary', 'educ=2'), ('Education', 'Tertiary', 'educ=3'),
          ('Income', 'Quintile 1 (lowest)', 'inc_q=1'), ('Income', 'Quintile 2', 'inc_q=2'), ('Income', 'Quintile 3', 'inc_q=3'),
          ('Income', 'Quintile 4', 'inc_q=4'), ('Income', 'Quintile 5 (highest)', 'inc_q=5'),
          ('Residence', 'Rural', 'urbanicity=1'), ('Residence', 'Urban', 'urbanicity=2'),
          ('Work', 'In workforce', 'emp_in=1'), ('Work', 'Out of workforce', 'emp_in=2')]
out = []
for dim, name, key in GROUPS:
    pay, risk, lock = rows[f'{key}: anydigpayment'], rows[f'Phone owners, {key}: con21'], rows[f'Phone owners, {key}: con18']
    out.append(dict(dimension=dim, group=name, payment_use_pct=pay['weighted_percent'], payment_n=pay['n'],
                    request_exposure_pct=risk['weighted_percent'], exposure_n=risk['n'], lock_use_pct=lock['weighted_percent'], lock_n=lock['n']))
df = pd.DataFrame(out); df.round(1).to_csv('results/inclusion_risk_by_group.csv', index=False)
rho_risk = df.payment_use_pct.rank().corr(df.request_exposure_pct.rank())
rho_lock = df.payment_use_pct.rank().corr(df.lock_use_pct.rank())
hi = df.sort_values('request_exposure_pct', ascending=False).head(3)[['group', 'request_exposure_pct']].round(1).values.tolist()
summary = dict(n_groups=len(df), spearman_payment_vs_exposure=round(float(rho_risk), 2), spearman_payment_vs_lock=round(float(rho_lock), 2),
               highest_exposure_groups=hi, note='Groups overlap; descriptive only; payment use and lock use have different denominators from exposure.')
Path('results/inclusion_risk_summary.json').write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding='utf-8'); print(df.round(1).to_string(index=False)); print(summary)

plt.rcParams['font.family'] = 'Liberation Serif'
colors = {'Sex': '#1B8A7E', 'Age': '#2A5FA5', 'Education': '#E08E0B', 'Income': '#7A4FA0', 'Residence': '#6B7280', 'Work': '#B03A48'}
fig, ax = plt.subplots(figsize=(7.2, 5.0))
for dim, g in df.groupby('dimension'):
    ax.scatter(g.payment_use_pct, g.request_exposure_pct, s=55, color=colors[dim], label=dim, zorder=3)
OFFSETS = {'15–24': (5, -11), 'Quintile 3': (6, -12), 'Primary or less': (-10, 6), 'Out of workforce': (-62, -12), '40–59': (-30, 6), 'Rural': (5, 5),
           'Urban': (5, -10), 'Women': (5, -11), 'Quintile 2': (-30, -12)}
for _, r in df.iterrows():
    ax.annotate(r.group, (r.payment_use_pct, r.request_exposure_pct), xytext=OFFSETS.get(r.group, (4, 4)), textcoords='offset points', fontsize=8)
ax.axhline(9.35, color='#9CA3AF', lw=0.8, ls='--'); ax.axvline(48.46, color='#9CA3AF', lw=0.8, ls='--')
ax.text(ax.get_xlim()[1] - 0.5, 9.35 + 0.2, 'all phone owners 9.4%', ha='right', fontsize=8, color='#6B7280')
ax.set_xlabel('Inclusion: made or received a digital payment (% of adults in group)'); ax.set_ylabel('Risk: reported unsolicited money request (% of phone owners)')
for s in ('top', 'right'): ax.spines[s].set_visible(False)
ax.legend(frameon=False, fontsize=8, ncol=3, loc='upper left'); plt.tight_layout()
Path('figures').mkdir(exist_ok=True); plt.savefig('figures/figure7_inclusion_vs_risk.png', dpi=200); plt.close()

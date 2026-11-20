"""Significance tests for comparisons made in the paper.
(1) RQ3: sending money by device-lock status among request recipients (Fisher exact test on unweighted counts; the weighted shares in the paper are
    descriptive and no design-based test is possible without strata or cluster identifiers).
(2) Bank-app vs payment-app reviews: two-sample proportion tests (chi-square) for each of the six dictionary themes, Holm-adjusted.
(3) Bank-app vs payment-app fraud-keyword reviews: Fisher exact tests for the share about rewards and the share about blocked accounts, charges or grievances.
Run from the submission folder after the other analysis scripts:  python scripts/analysis_tests.py
Outputs: results/significance_tests.csv"""
import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency, fisher_exact

rows = []
# (1) RQ3
tab = [[39, 170 - 39], [6, 49 - 6]]
odds, p = fisher_exact(tab)
rows.append(dict(test='RQ3: sent money, lock (39/170) vs no lock (6/49)', method='Fisher exact (unweighted)', statistic=round(odds, 3), p_raw=p, p_holm=np.nan))

# (2) themes, bank vs payment
bv = pd.read_csv('results/bank_vs_payment_themes.csv')
NB, NP = 6240, 7848
ps = []
for r in bv.itertuples():
    t = [[r.bank_reviews, NB - r.bank_reviews], [r.payment_reviews, NP - r.payment_reviews]]
    chi, p, _, _ = chi2_contingency(t, correction=False); ps.append(p)
order = np.argsort(ps); holm = np.empty(len(ps)); run = 0.0
for rank, i in enumerate(order):
    run = max(run, min(1.0, (len(ps) - rank) * ps[i])); holm[i] = run
for r, p, h in zip(bv.itertuples(), ps, holm):
    t = [[r.bank_reviews, NB - r.bank_reviews], [r.payment_reviews, NP - r.payment_reviews]]
    chi, _, _, _ = chi2_contingency(t, correction=False)
    rows.append(dict(test=f'Bank vs payment apps, theme: {r.theme[:40]} ({r.bank_reviews}/{NB} vs {r.payment_reviews}/{NP})', method='chi-square, 2x2', statistic=round(chi, 2), p_raw=p, p_holm=h))

# (3) manual categories among fraud-keyword reviews
bank = pd.read_csv('results/bankapps_fraud_manual_codes.csv').manual_category
play = pd.read_csv('results/review_fraud_manual_codes.csv').manual_category
ios = pd.read_csv('results/appstore_fraud_manual_codes.csv').manual_category
pay = pd.concat([play, ios], ignore_index=True)
for label, key in [('rewards or cashback not honoured', 'Reward'), ('blocked account, mis-selling or grievance', 'Blocked')]:
    a, n1 = int(bank.str.startswith(key).sum()), len(bank)
    b, n2 = int(pay.str.startswith(key).sum()), len(pay)
    odds, p = fisher_exact([[a, n1 - a], [b, n2 - b]])
    rows.append(dict(test=f'Fraud-keyword reviews about {label}: bank {a}/{n1} vs payment (Play + App Store) {b}/{n2}', method='Fisher exact', statistic=round(odds, 3), p_raw=p, p_holm=np.nan))
out = pd.DataFrame(rows); out.to_csv('results/significance_tests.csv', index=False)
pd.set_option('display.width', 250, 'display.max_colwidth', 110); print(out.to_string(index=False, float_format=lambda x: f'{x:.2g}'))

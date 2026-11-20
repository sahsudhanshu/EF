"""Agreement between a human coder and the first pass / AI second pass for the 122 round-2 reviews.
Usage: python3 compute_agreement_round2.py PartC_coding_sheet_filled.csv PRIVATE_DO_NOT_SHARE/PartC_answer_key.csv
If two people split the work, concatenate their filled rows into one file first (keep the header)."""
import sys
import pandas as pd

LET = dict(zip('ABCDEFG', [
 "Reward, cashback or offer not honoured (called scam/fraud)", "Money debited, payment failed or refund missing",
 "Blocked account, mis-selling or poor grievance handling", "Spam, permissions, privacy or intrusive security controls",
 "General accusation, no specific incident", "Praise or no complaint", "Unauthorised access, theft or hacking (reported or feared)"]))

def kappa(a, b):
    po = (a == b).mean(); pe = sum((a == k).mean() * (b == k).mean() for k in set(a) | set(b))
    return (po - pe) / (1 - pe) if pe < 1 else 1.0

sheet = pd.read_csv(sys.argv[1]); key = pd.read_csv(sys.argv[2])
d = sheet.merge(key, on='item_id')
d['human'] = d.your_code_letter.astype(str).str.strip().str.upper().map(LET)
if d.human.isna().any(): print(f'WARNING: {int(d.human.isna().sum())} rows without a valid letter are excluded')
d = d.dropna(subset=['human'])
def report(x, label):
    for name, col in [('first pass', 'manual_category'), ('AI blind second pass', 'second_pass')]:
        ag = (x.human == x[col]).mean()
        print(f'{label} vs {name}: {int((x.human == x[col]).sum())}/{len(x)} = {100*ag:.1f}%, Cohen kappa {kappa(x.human, x[col]):.3f}')
report(d, 'ALL')
for ds, g in d.groupby('dataset'): report(g, ds)
print('\nDisagreements with the first pass:')
for r in d[d.human != d.manual_category].itertuples(): print(f'  {r.item_id} ({r.dataset[:10]}): first={r.manual_category[:26]} | human={r.human[:26]}')

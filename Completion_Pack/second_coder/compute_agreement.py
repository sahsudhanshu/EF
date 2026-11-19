"""Agreement between a human second coder and the first-pass (and AI second-pass) labels.
Usage: python3 compute_agreement.py PartA_filled.csv PartA_answer_key.csv [PartB_filled.csv]"""
import sys
import pandas as pd

LET = dict(zip('ABCDEFG', [
 "Reward, cashback or offer not honoured (called scam/fraud)",
 "Money debited, payment failed or refund missing",
 "Blocked account, mis-selling or poor grievance handling",
 "Spam, permissions, privacy or intrusive security controls",
 "General accusation, no specific incident",
 "Praise or no complaint",
 "Unauthorised access, theft or hacking (reported or feared)"]))

def kappa(a, b):
    po = (a == b).mean()
    pe = sum((a == k).mean() * (b == k).mean() for k in set(a) | set(b))
    return (po - pe) / (1 - pe) if pe < 1 else 1.0

sheet = pd.read_csv(sys.argv[1]); key = pd.read_csv(sys.argv[2])
d = sheet.merge(key, on='item_id')
d['human'] = d.your_code_letter.astype(str).str.strip().str.upper().map(LET)
missing = d.human.isna().sum()
if missing: print(f'WARNING: {missing} rows have no valid letter and are excluded')
d = d.dropna(subset=['human'])
for name, col in [('first pass (single coder)', 'manual_category'), ('AI blind second pass', 'second_pass')]:
    print(f'{name}: agreement {(d.human == d[col]).sum()}/{len(d)} = {100*(d.human == d[col]).mean():.1f}%, Cohen kappa {kappa(d.human, d[col]):.3f}')
print('\nDisagreements with the first pass:')
for _, r in d[d.human != d.manual_category].iterrows():
    print(f"  {r.item_id}: first={r.manual_category[:28]} | you={r.human[:28]}")
if len(sys.argv) > 3:
    b = pd.read_csv(sys.argv[3]); ans = b.iloc[:, 4].astype(str).str.strip().str.lower()
    print(f"\nPart B: {(ans == 'yes').sum()} of {ans.isin(['yes','no']).sum()} non-keyword reviews described fraud/unauthorised use")

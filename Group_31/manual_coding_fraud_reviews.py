"""Manual classification of every review that contains a fraud/scam keyword (118 reviews).
Each review was read in full and assigned ONE category. Index = row number in results/review_fraud_keyword_all.csv
(the file produced by analysis_extra.py). Re-run to regenerate results/review_fraud_manual_codes.csv."""
import pandas as pd
CODES = {
 'Reward, cashback or offer not honoured (called scam/fraud)': [3,8,20,22,23,24,25,26,28,31,32,33,35,36,37,38,39,40,41,42,44,45,47,48,49,50,51,52,54,55,57,58,59,61,62,65,69,70,74,75,76,78,79,80,81,83,84,85,86,87,90,91,92,94,95,96,98,102,105,106],
 'Money debited, payment failed or refund missing': [4,6,12,17,30,43,46,53,60,64,67,72,93,99,100],
 'Unauthorised access, theft or hacking (reported or feared)': [7,19,101,107,110,114],
 'Blocked account, mis-selling or poor grievance handling': [0,10,18,34,88,97,103,108,109,111,116],
 'Spam, permissions, privacy or intrusive security controls': [2,29,63,68,71,89,104,113,115,117],
 'Praise or no complaint': [5,14,15,21,27,73,77],
 'General accusation, no specific incident': [1,9,11,13,16,56,66,82,112],
}
d = pd.read_csv('results/review_fraud_keyword_all.csv').reset_index(drop=True)
assigned = {i: k for k, v in CODES.items() for i in v}
assert len(assigned) == sum(len(v) for v in CODES.values()), 'an index appears in two categories'
missing = [i for i in range(len(d)) if i not in assigned]; assert not missing, missing
d['manual_category'] = d.index.map(assigned)
d.to_csv('results/review_fraud_manual_codes.csv', index=False)
t = d.manual_category.value_counts().rename_axis('category').reset_index(name='reviews'); t['share_pct'] = (100 * t.reviews / len(d)).round(1)
t.to_csv('results/review_fraud_manual_summary.csv', index=False); print(t.to_string(index=False)); print('total', len(d))

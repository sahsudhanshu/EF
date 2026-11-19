"""Tally themes from interview_notes_template.csv once filled in. Usage: python3 tally_themes.py interview_notes_template.csv"""
import sys
import pandas as pd
d = pd.read_csv(sys.argv[1])
d = d.dropna(subset=['participant_id'])
th = [c for c in d.columns if c.startswith('T') and c[1:].isdigit()]
print(f'{len(d)} interviews; by group:\n{d.group.value_counts().to_string()}\n')
t = d[th].apply(pd.to_numeric, errors='coerce').fillna(0).astype(int)
out = pd.DataFrame({'interviews_mentioning': t.sum(), 'share_pct': (100 * t.mean()).round(0)})
for g, sub in d.groupby('group'):
    out[f'n_{g}'] = t.loc[sub.index].sum()
print(out.to_string())
print('\nThemes in 3+ interviews (may be called a pattern):', ', '.join(out.index[out.interviews_mentioning >= 3]) or 'none')

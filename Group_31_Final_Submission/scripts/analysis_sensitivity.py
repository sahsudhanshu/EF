"""Design-effect sensitivity for the exploratory logistic model (RQ2).
The public Findex file has no strata or PSU identifiers, so design-based variances cannot be computed.
This script (a) reports the Kish design effect and effective sample size from the weights alone, (b) refits the same
weighted model, and (c) re-reports the intervals after inflating the variance by assumed extra design effects
(clustering) of 1.5, 2 and 3, to show which conclusions survive. Run from the folder containing data/:
    python scripts/analysis_sensitivity.py [output_dir]      (default output_dir = results)"""
import sys
from math import erfc, sqrt
from pathlib import Path
import numpy as np
import pandas as pd

out_dir = Path(sys.argv[1] if len(sys.argv) > 1 else 'results'); out_dir.mkdir(exist_ok=True, parents=True)
df = pd.read_stata('data/Findex_Microdata_2025_updateIndia.dta', convert_categoricals=False)
phone = df.con1.eq(1)
z = df.loc[phone & df.con21.isin([1, 2])].copy()
X = pd.DataFrame({'Intercept': 1., 'Digital payment': z.anydigpayment, 'Female': (z.female == 1).astype(float),
                  'Age per 10 years': z.age / 10, 'Secondary education': (z.educ == 2).astype(float),
                  'Tertiary education': (z.educ == 3).astype(float), 'Income quintile': z.inc_q.astype(float),
                  'In workforce': (z.emp_in == 1).astype(float), 'Urban': (z.urbanicity == 2).astype(float)}, index=z.index)
valid = X.notna().all(axis=1) & z.wgt.notna(); X = X.loc[valid]; z = z.loc[valid]
x = X.to_numpy(); y = (z.con21 == 1).to_numpy(dtype=float); w = z.wgt.to_numpy(); b = np.zeros(x.shape[1])
for _ in range(100):
    p = 1 / (1 + np.exp(-np.clip(x @ b, -30, 30))); h = x.T @ ((w * p * (1 - p))[:, None] * x)
    step = np.linalg.solve(h, x.T @ (w * (y - p))); b += step
    if np.max(np.abs(step)) < 1e-10: break
p = 1 / (1 + np.exp(-np.clip(x @ b, -30, 30))); bread = np.linalg.inv(x.T @ ((w * p * (1 - p))[:, None] * x))
score = x * (w * (y - p))[:, None]; cov = bread @ (score.T @ score) @ bread; se = np.sqrt(np.diag(cov))

deff_kish = len(w) * np.sum(w ** 2) / np.sum(w) ** 2
print(f'n = {len(w)}; Kish design effect from weights = {deff_kish:.3f}; effective n = {len(w) / deff_kish:.0f}')
rows = []
for extra in (1.0, 1.5, 2.0, 3.0):
    s = se * sqrt(extra)
    for name, bi, si in zip(X.columns, b, s):
        rows.append(dict(extra_design_effect=extra, variable=name, odds_ratio=round(float(np.exp(bi)), 3),
                         low_95=round(float(np.exp(bi - 1.96 * si)), 3), high_95=round(float(np.exp(bi + 1.96 * si)), 3),
                         excludes_1=bool(np.exp(bi - 1.96 * si) > 1 or np.exp(bi + 1.96 * si) < 1)))
res = pd.DataFrame(rows); res.to_csv(out_dir / 'Group_31_design_sensitivity.csv', index=False)
(out_dir / 'Group_31_design_sensitivity_note.txt').write_text(
    f'n={len(w)}; Kish design effect from weights={deff_kish:.3f}; effective n={len(w)/deff_kish:.0f}\n'
    'Intervals inflate the sandwich variance by the stated extra design effect (assumed clustering); not design-based.\n', encoding='utf-8')
print(res[res.variable != 'Intercept'].pivot(index='variable', columns='extra_design_effect', values='excludes_1').to_string())
print(res[(res.variable.isin(['Digital payment', 'Female', 'Tertiary education'])) & (res.extra_design_effect.isin([1.0, 2.0, 3.0]))].to_string(index=False))

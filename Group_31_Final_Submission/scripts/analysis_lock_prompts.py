"""Counts Google Play payment-app reviews that describe device-lock, security-alert or developer-option prompts (Section 4.5 of the paper).
Run from the submission folder:  python scripts/analysis_lock_prompts.py   Output: results/review_device_lock_prompts.json"""
import json
import pandas as pd

rv = pd.read_csv('data/app_reviews.csv').dropna(subset=['text'])
rv = rv[rv.text.astype(str).str.len() >= 15].drop_duplicates(subset=['app', 'text'])
pat = r'device\s+lock|lock\s+authentication|screen\s+lock|developer\s+option|security\s+alert|device\s+security|enable\s+(?:your\s+)?(?:device|screen)'
m = rv.text.astype(str).str.contains(pat, case=False, regex=True)
out = dict(n=int(m.sum()), total=int(len(rv)), pct=round(100 * m.mean(), 1), by_app=rv[m].app.value_counts().to_dict(), mean_rating=round(float(rv[m].rating.mean()), 2),
           note='Dictionary: device lock, lock authentication, screen lock, developer option, security alert, device security, enable device/screen.')
json.dump(out, open('results/review_device_lock_prompts.json', 'w'), indent=2)
print(out)

"""Sensitivity check: reviews flagged by Hindi/Hinglish fraud and money-loss words that the English keyword dictionary misses.
The main dictionary (analysis_extra.py, analysis_appstore.py, analysis_bankapps.py) is English only; it is kept unchanged so that all counts
and the manual classifications stay comparable. This script lists the additional reviews an extended dictionary would flag.
Run from the submission folder:  python scripts/analysis_hinglish.py
Outputs: results/hinglish_extra_reviews.csv, results/hinglish_summary.json"""
import json
import re
from pathlib import Path
import pandas as pd

ENGLISH = re.compile(r'\b(?:fraud\w*|scam\w*|scammer\w*|cheat\w*|hack\w*|phishing|unauthori[sz]ed|stolen|fake|spam|looted|duped|thief|theft)\b', re.I)
# Hindi / Hinglish (Latin script and Devanagari) words for cheating, theft, looting and money cut without consent
EXTRA = re.compile(r'dhokha|dhoka|dhokebaaz|dhokhebaaz|\bchor\b|chori|\bthag\w*|\bloot\w*|lutera|farzi|jhootha|'
                   r'(?:paise|paisa|rupay\w*|amount)\s+(?:kat|cut|kate)\w*|kat\s*gay\w*|cut\s*(?:gaya|ho\s*gay\w*)|'
                   r'धोखा|धोखाधड़ी|चोर|ठग|लूट|फर्जी|पैसे\s*कट', re.I)

def clean_play(path, extra_cols=()):
    d = pd.read_csv(path).dropna(subset=['text']); d['text'] = d.text.astype(str)
    return d[d.text.str.len() >= 15].drop_duplicates(subset=['app', 'text'])

def clean_ios(path):
    d = pd.read_csv(path).fillna(''); d['text'] = (d.title.astype(str) + '. ' + d.text.astype(str)).str.strip()
    return d[d.text.str.len() >= 15].drop_duplicates(subset=['app', 'title', 'text', 'date'])

sets = {'Play payment apps': clean_play('data/app_reviews.csv'), 'App Store payment apps': clean_ios('data/appstore_reviews.csv'),
        'Play bank apps': clean_play('data/bankapps_play_reviews.csv'), 'App Store bank apps': clean_ios('data/bankapps_appstore_reviews.csv')}
rows, summ = [], {}
for name, d in sets.items():
    hit = d.text.str.contains(EXTRA, regex=True) & ~d.text.str.contains(ENGLISH, regex=True)
    summ[name] = dict(reviews=int(len(d)), english_fraud_keyword=int(d.text.str.contains(ENGLISH, regex=True).sum()), extra_hinglish_only=int(hit.sum()))
    for r in d[hit].itertuples():
        rows.append(dict(dataset=name, app=r.app, date=r.date, rating=r.rating, text=r.text))
out = pd.DataFrame(rows); out.to_csv('results/hinglish_extra_reviews.csv', index=False)
Path('results/hinglish_summary.json').write_text(json.dumps(summ, indent=2), encoding='utf-8'); print(json.dumps(summ, indent=2))
# the extra reviews were then read and classified with the same seven categories (column manual_category; one coder, no second pass)

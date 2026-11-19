"""Fetch the open data used for the peer comparison and the qualitative review analysis.
Run from the folder that contains this file:  python fetch_data.py
Outputs: data/wdi_peers.csv  (World Bank Global Findex 2025 country aggregates, open API)
         data/app_reviews.csv (public Google Play reviews of five Indian payment/banking apps)
The India household microdata (Findex_Microdata_2025_updateIndia.dta) is NOT fetched here: it needs a
World Bank microdata-library login and acceptance of its terms. See README.txt."""
import csv
import json
import time
import urllib.request
from pathlib import Path

D = Path('data'); D.mkdir(exist_ok=True)

# ----------------------------------------------------------------------------- 1. Findex country aggregates
INDICATORS = {
    'account.t.d': 'account_pct_adults',
    'con1': 'own_phone_pct_adults',
    'con18.s': 'phone_lock_pct_phone_owners',
    'con21.s': 'unsolicited_money_request_pct_phone_owners',
}
ECONOMIES = 'IND;CHN;IDN;BGD;PAK;BRA;ZAF;WLD;LMC;SAS'


def wb(code):
    url = f'https://api.worldbank.org/v2/country/{ECONOMIES}/indicator/{code}?format=json&date=2024&per_page=100&source=28'
    with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'student-research'}), timeout=60) as r:
        data = json.load(r)
    return {x['country']['value']: x['value'] for x in (data[1] or [])}


rows = {}
for code, name in INDICATORS.items():
    for country, value in wb(code).items():
        rows.setdefault(country, {'economy': country, 'year': 2024})[name] = value
with open(D / 'wdi_peers.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=['economy', 'year'] + list(INDICATORS.values()))
    w.writeheader(); w.writerows(rows.values())
print('wrote data/wdi_peers.csv', len(rows), 'economies')

# ----------------------------------------------------------------------------- 2. Public app-store reviews
APPS = {
    'PhonePe': 'com.phonepe.app',
    'Google Pay': 'com.google.android.apps.nbu.paisa.user',
    'Paytm': 'net.one97.paytm',
    'BHIM': 'in.org.npci.upiapp',
    'SBI YONO': 'com.sbi.lotusintouch',
}
try:
    from google_play_scraper import reviews, Sort
except ImportError:
    raise SystemExit('pip install google-play-scraper   (needed only for the review download)')

with open(D / 'app_reviews.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f); w.writerow(['app', 'date', 'rating', 'text'])
    for app, pkg in APPS.items():
        got, token, n = [], None, 0
        while n < 3000:
            batch, token = reviews(pkg, lang='en', country='in', sort=Sort.NEWEST, count=200, continuation_token=token)
            got += batch; n = len(got)
            if not token or not batch:
                break
            time.sleep(1)
        for r in got:
            w.writerow([app, r['at'].date().isoformat(), r['score'], (r['content'] or '').replace('\n', ' ')])
        print(app, len(got), 'reviews')

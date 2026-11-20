"""Download public reviews of bank mobile-banking apps (the 'mobile banking' side of the topic).

Google Play (India store, English): newest reviews via google-play-scraper.
Apple App Store (India): public customer-review feed (newest ~500 per app).
Only app, date, rating, text (and version/title on iOS) are stored; reviewer names are not.
Emails and phone numbers in text are masked. Reviews under 15 characters and duplicates are removed.
Outputs: data/bankapps_play_reviews.csv, data/bankapps_appstore_reviews.csv
Run from the submission folder:  python scripts/fetch_bankapps.py
"""
import re
import time
from pathlib import Path

import pandas as pd
import requests
from google_play_scraper import Sort, reviews

PLAY = {"ICICI iMobile": "com.csam.icici.bank.imobile", "Axis Mobile": "com.axis.mobile", "Kotak Bank": "com.kotak.bank.mobile",
        "bob World": "com.bankofbaroda.mconnect", "Canara ai1": "com.canarabank.mobility", "IDFC FIRST": "com.idfcfirstbank.optimus"}
IOS = {"HDFC Bank": 6504402552, "ICICI iMobile": 375276006, "Axis Mobile": 699582556, "Kotak 811": 6447808696,
       "PNB ONE": 1434797444, "bob World": 1191046038}
PER_APP_PLAY = 1500
MASK = [(re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+"), "[email]"), (re.compile(r"(?<!\d)(?:\+?91[- ]?)?[6-9]\d{9}(?!\d)"), "[phone]")]
data = Path(__file__).resolve().parent.parent / "data"; data.mkdir(exist_ok=True)


def mask(t):
    for pat, rep in MASK:
        t = pat.sub(rep, t)
    return t


rows = []
for app, pid in PLAY.items():
    res, _ = reviews(pid, lang="en", country="in", sort=Sort.NEWEST, count=PER_APP_PLAY)
    for r in res:
        rows.append(dict(app=app, date=r["at"].strftime("%Y-%m-%d"), rating=r["score"], text=mask(r["content"] or "")))
    print(app, len(res))
play = pd.DataFrame(rows).dropna(subset=["text"])
play = play[play.text.str.len() >= 15].drop_duplicates(subset=["app", "text"])
play.to_csv(data / "bankapps_play_reviews.csv", index=False)

rows = []
URL = "https://itunes.apple.com/in/rss/customerreviews/page={page}/id={id}/sortby=mostrecent/json"
for app, app_id in IOS.items():
    for page in range(1, 11):
        r = requests.get(URL.format(page=page, id=app_id), timeout=30, headers={"User-Agent": "Group31-term-paper/1.0"})
        if r.status_code != 200:
            break
        entries = r.json().get("feed", {}).get("entry", [])
        entries = [entries] if isinstance(entries, dict) else entries
        entries = [e for e in entries if "im:rating" in e]
        if not entries:
            break
        for e in entries:
            rows.append(dict(app=app, date=e["updated"]["label"][:10], rating=int(e["im:rating"]["label"]),
                             title=e["title"]["label"], text=mask(e["content"]["label"])))
        time.sleep(1)
ios = pd.DataFrame(rows)
ios["full"] = (ios.title.fillna("") + ". " + ios.text.fillna("")).str.strip()
ios = ios[ios.full.str.len() >= 15].drop(columns="full").drop_duplicates(subset=["app", "title", "text", "date"])
ios.to_csv(data / "bankapps_appstore_reviews.csv", index=False)
for name, d in (("Play", play), ("App Store", ios)):
    print(name, len(d)); print(d.groupby("app").agg(n=("rating", "size"), mean=("rating", "mean"), first=("date", "min"), last=("date", "max")).round(2))

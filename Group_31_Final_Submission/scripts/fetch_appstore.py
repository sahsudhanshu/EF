"""Download public Apple App Store (India) customer reviews for the five payment apps.

Uses Apple's public customer-review RSS/JSON feed (the feed serves at most 10 pages of 50 reviews per app,
newest first). Only app, date, rating, version, title and text are stored; reviewer names are not.
Email addresses and phone numbers in text are masked. Output: data/appstore_reviews.csv
"""
import re
import time
from pathlib import Path

import pandas as pd
import requests

APPS = {"PhonePe": 1170055821, "Google Pay": 1193357041, "Paytm": 473941634,
        "BHIM": 1200315258, "SBI YONO": 1231393474}
URL = "https://itunes.apple.com/in/rss/customerreviews/page={page}/id={id}/sortby=mostrecent/json"
MASK = [(re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+"), "[email]"), (re.compile(r"(?<!\d)(?:\+?91[- ]?)?[6-9]\d{9}(?!\d)"), "[phone]")]

rows = []
for app, app_id in APPS.items():
    for page in range(1, 11):
        r = requests.get(URL.format(page=page, id=app_id), timeout=30, headers={"User-Agent": "Group31-term-paper/1.0"})
        if r.status_code != 200:
            break
        entries = r.json().get("feed", {}).get("entry", [])
        if isinstance(entries, dict):
            entries = [entries]
        entries = [e for e in entries if "im:rating" in e]
        if not entries:
            break
        for e in entries:
            text = e["content"]["label"]
            for pat, rep in MASK:
                text = pat.sub(rep, text)
            rows.append(dict(app=app, date=e["updated"]["label"][:10], rating=int(e["im:rating"]["label"]),
                             version=e["im:version"]["label"], title=e["title"]["label"], text=text))
        time.sleep(1)

df = pd.DataFrame(rows).drop_duplicates(subset=["app", "title", "text", "date"])
df["chars"] = (df.title.fillna("") + " " + df.text.fillna("")).str.len()
df = df[df.chars >= 15].drop(columns="chars")
out = Path(__file__).resolve().parent.parent / "data" / "appstore_reviews.csv"
out.parent.mkdir(exist_ok=True)
df.to_csv(out, index=False)
print(len(df), "reviews saved to", out)
print(df.groupby("app").agg(n=("rating", "size"), mean_rating=("rating", "mean"), first=("date", "min"), last=("date", "max")))

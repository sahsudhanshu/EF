"""Download open World Bank WDI/Findex indicators and save a country-year panel to data/panel_raw.csv."""
import requests
import pandas as pd

INDICATORS = {
    # firm financing outcomes (World Bank Enterprise Surveys, via WDI)
    "IC.FRM.CRDC.FL.ZS": "fully_constrained",     # % of firms fully credit constrained
    "IC.FRM.CRDC.PT.ZS": "partially_constrained",  # % of firms partially credit constrained
    "IC.FRM.BNKS.ZS": "firms_bank_invest",         # % of firms using banks to finance investment
    "IC.FRM.BNKL.ZS": "firms_bank_loan",           # % of firms with a bank loan/line of credit
    "IC.FRM.TAXE.ZS": "firms_etax",                # % of firms filing taxes electronically (firm digitisation)
    "IC.FRM.EXS.ZS": "firms_exporting",
    "IC.FRM.FO.ZS": "firms_foreign_owned",
    "IC.FRM.CORR.ZS": "informal_payments",
    # digital access / digital finance
    "IT.NET.USER.ZS": "internet_users",
    "IT.CEL.SETS.P2": "mobile_subs",
    "IT.NET.SECR.P6": "secure_servers",
    "FX.OWN.TOTL.ZS": "account_ownership",
    "IT.NET.BBND.P2": "broadband_subs",
    # financial depth and macro controls
    "FS.AST.PRVT.GD.ZS": "private_credit_gdp",
    "FR.INR.LNDP": "lending_spread",
    "NY.GDP.PCAP.KD": "gdp_pc",
    "NY.GDP.MKTP.KD.ZG": "gdp_growth",
    "FP.CPI.TOTL.ZG": "inflation",
}


def fetch(code):
    url = f"https://api.worldbank.org/v2/country/all/indicator/{code}"
    r = requests.get(url, params={"format": "json", "per_page": 20000, "date": "2005:2024"}, timeout=60)
    data = r.json()
    if len(data) < 2 or data[1] is None:
        return None
    rows = [(d["countryiso3code"], d["country"]["value"], int(d["date"]), d["value"])
            for d in data[1] if d["countryiso3code"] and d["value"] is not None]
    return pd.DataFrame(rows, columns=["iso3", "country", "year", INDICATORS[code]])


if __name__ == "__main__":
    panel = None
    for code in INDICATORS:
        df = fetch(code)
        if df is None or df.empty:
            print("skip", code)
            continue
        print(code, len(df))
        panel = df if panel is None else panel.merge(df.drop(columns="country"), on=["iso3", "year"], how="outer")
    panel.to_csv("data/panel_raw.csv", index=False)
    print(panel.shape)

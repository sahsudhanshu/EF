GROUP 31 - ENTREPRENEURIAL FINANCE TERM PAPER
Mobile Banking, Financial Inclusion and Cybersecurity Risk in India
Authors: Rushal Verma, Vichanshu Raj, Sudhanshu

Research_Report.pdf        The final paper (same file as report/Group_31_Research_Paper.pdf)
report/                    Paper as PDF and editable Word file (follows the TA's paper structure)
slides/                    Presentation (PPTX and PDF, 18 slides with speaker notes)
analysis.ipynb             Notebook that reproduces every result (outputs stored)
fetch_data.py              Downloads the open data: Findex 2025 country aggregates (World Bank API) and public Google Play reviews
data/                      wdi_peers.csv, app_reviews.csv (usernames not stored; emails/phone numbers masked)
figures/                   The six charts used in the paper
results/                   Weighted results, logistic model, audit file, review coding, peer table, finance model outputs
scripts/                   analysis_group31.py (survey), analysis_extra.py (peers + reviews), manual_coding_fraud_reviews.py,
                           revision_finance.py (finance model), build_structured_paper.py / build_structured_deck.py (document builders)

DATA NOT INCLUDED
The India household microdata (World Bank, India - The Global Findex Database 2025, 2024 survey, ref. IND_2024_FINDEX_v02_M,
DOI 10.48529/c9vy-pq51, https://microdata.worldbank.org/index.php/catalog/7916) is not included because of the World Bank's access
conditions. To rerun the notebook, download it and save it as data/Findex_Microdata_2025_updateIndia.dta.

TO RERUN (Python with pandas, numpy, matplotlib, google-play-scraper, jupyter):  python fetch_data.py   then open analysis.ipynb
Note: re-fetching app reviews returns the newest reviews at that time, so review counts will differ from the paper's
snapshot (2 Oct to 19 Nov 2026); data/app_reviews.csv holds the snapshot used in the paper.

GROUP 31 - ENTREPRENEURIAL FINANCE TERM PAPER
Mobile Banking: Financial Inclusion vs Cybersecurity Risks
Authors: Rushal Verma (IIT2024045), Vichanshu Raj (IIT2024083), Sudhanshu (IIT2024081)

Research_Report.pdf        The final paper (same file as report/Group_31_Research_Paper.pdf; PDF rendered with LibreOffice, 27 pages)
report/                    Paper as PDF and editable Word file (follows the TA's paper structure), plus IEEE_Report (2-page condensed version, PDF and Word)
slides/                    Presentation (PPTX and PDF, 18 slides with speaker notes)
analysis.ipynb             Notebook that reproduces every result (outputs stored)
fetch_data.py              Downloads the open data: Findex 2025 country aggregates (World Bank API) and public Google Play reviews
                           (scripts/fetch_appstore.py downloads the Apple App Store reviews: data/appstore_reviews.csv)
data/                      wdi_peers.csv, app_reviews.csv, appstore_reviews.csv, bankapps_play_reviews.csv, bankapps_appstore_reviews.csv (usernames not stored; emails/phone numbers masked)
figures/                   The six charts used in the paper
results/                   Weighted results, logistic model, audit file, review coding (first pass, blind AI second pass, human second coder on 40 reviews), peer table, finance model outputs
scripts/                   analysis_group31.py (survey), analysis_extra.py (peers + reviews), manual_coding_fraud_reviews.py,
                           analysis_appstore.py (App Store reviews), analysis_sensitivity.py (design-effect sensitivity), fetch_bankapps.py + analysis_bankapps.py (bank mobile-banking app reviews), analysis_inclusion_risk.py (inclusion vs risk by group), revision_finance.py (finance model), build_structured_paper.py / build_structured_deck.py / build_ieee_report.py (document builders)

DATA NOT INCLUDED
The India household microdata (World Bank, India - The Global Findex Database 2025, 2024 survey, ref. IND_2024_FINDEX_v02_M,
DOI 10.48529/c9vy-pq51, https://microdata.worldbank.org/index.php/catalog/7916) is not included because of the World Bank's access
conditions. To rerun the notebook, download it and save it as data/Findex_Microdata_2025_updateIndia.dta.

TO RERUN (Python with pandas, numpy, matplotlib, google-play-scraper, jupyter):  python fetch_data.py   then open analysis.ipynb
Note: re-fetching app reviews returns the newest reviews at that time, so review counts will differ from the paper's
snapshot (2 Oct to 19 Nov 2026); data/app_reviews.csv holds the snapshot used in the paper.

SECONDARY QUALITATIVE EVIDENCE
No interviews were conducted by the group. results/published_studies.csv and results/published_studies_themes.csv record the five published interview studies and the eight themes used in Section 4.11; results/appstore_* hold the App Store review coding. The App Store feed returns only the newest reviews, so re-running fetch_appstore.py gives different counts from the paper's snapshot (30 Apr to 18 Nov 2026).

DESIGN-EFFECT SENSITIVITY
results/Group_31_design_sensitivity.csv shows the logistic-model intervals after inflating the variance for assumed extra design effects of 1, 1.5, 2 and 3 (the public file has no strata or cluster identifiers). It needs the microdata file to re-run.

TOPIC
Mobile banking: financial inclusion vs cybersecurity risks. The quantitative core compares inclusion (account ownership, digital payment use) with cybersecurity risk (reported unsolicited money requests, device protection) for individuals and for 18 groups (results/inclusion_risk_by_group.csv, figures/figure7_inclusion_vs_risk.png). Qualitative evidence: 14,088 public reviews of 13 payment and bank apps (Google Play and App Store; results/bankapps_*, appstore_*, review_*), institutional documents, and five published interview studies.

GROUP 31 - ENTREPRENEURIAL FINANCE TERM PAPER
Mobile Banking: Financial Inclusion vs Cybersecurity Risks
Authors: Rushal Verma (IIT2024045), Vichanshu Raj (IIT2024083), Sudhanshu (IIT2024081)

THE SUBMISSION
Research_Report.pdf        The paper, 12 pages (same file as report/Group_31_Research_Paper.pdf)
report/                    The paper as PDF and editable Word file (TA's paper structure; Times New Roman 12)
slides/                    Presentation, 19 slides with speaker notes (PPTX and PDF)

SUPPORTING MATERIAL
analysis.ipynb             Notebook that reproduces the results (outputs stored)
fetch_data.py              Downloads the open data: Findex 2025 country aggregates (World Bank API) and public app reviews
data/                      Peer indicators and public app reviews (no usernames; emails and phone numbers masked)
figures/                   Charts used in the paper and slides
results/                   Weighted results, model, audit file, significance tests, review coding, second-coder agreement, finance model
scripts/                   Analysis, fetching and coding scripts; scripts/condensed/ holds the builders for the paper and slides
                           (they run from the full project layout and read references_source.txt)

DATA NOT INCLUDED
The India household microdata (World Bank, India - The Global Findex Database 2025, 2024 survey, ref. IND_2024_FINDEX_v02_M,
DOI 10.48529/c9vy-pq51, https://microdata.worldbank.org/index.php/catalog/7916) is not included because of the World Bank's access
conditions. To rerun the notebook, download it and save it as data/Findex_Microdata_2025_updateIndia.dta.

NOTES
- Re-fetching app reviews returns the newest reviews at that time, so counts will differ from the paper; data/ holds the snapshot used.
- Review coding: first pass by one coder; blind AI second passes; a human coder outside the group re-coded 40 Google Play reviews;
  a further second coder (a person who used software, including AI tools, as an aid but made each coding decision, as reported by the group) re-coded 122 App Store and bank-app reviews.
  The private answer key is not part of this folder.
- Finance inputs are illustrative assumptions, not findings.

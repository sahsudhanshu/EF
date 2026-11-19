# Project context: Group 31 term paper (Entrepreneurial Finance)

Share this file with anyone (or any AI session) picking up the work. Last updated 20 November 2026.

## 1. What this is
- **Course:** Entrepreneurial Finance. **Group 31.** **Authors:** Rushal Verma, Vichanshu Raj, Sudhanshu (use "Sudhanshu" only; "Sah" removed on request).
- **Topic:** Mobile banking, financial inclusion and cybersecurity risk in India.
- **Title:** *Mobile Banking, Financial Inclusion and Cybersecurity Risk in India: A Survey-Weighted Analysis of the 2024 Global Findex and an Institutional Payment-Safety Service Proposal.*
- **Goal:** a term paper that follows the TA's required structure (`Paper structure.pdf`), plus a presentation. A friend's submission (folder `Friend/`) was the quality reference.

## 2. The TA's rules (the only hard requirements)
Structure: Title, Abstract (150–200 words), Keywords, 1 Introduction, 2 Literature review (at least 30 papers), 3 Methodology (3.1 design, 3.2 sampling, 3.3 data collection, 3.4 instruments, 3.5 analysis, 3.6 ethics, plus a justification for each method), 4 Results (no interpretation), 5 Discussion (5.1 academic, 5.2 policy, 5.3 managerial, 5.4 future scope), 6 Conclusion, References.
Formatting: Times New Roman 12 throughout; table label above the table; figure label below the figure.
The TA confirmed there is **no page limit** and to use a **standard citation style** (we use numbered in-text citations with APA-style reference entries; APA author-year in text was offered but not requested).

## 3. Where everything is
| Location | Contents |
|---|---|
| `Group_31_Final_Submission/` | **The submission folder.** `Research_Report.pdf`, `analysis.ipynb`, `fetch_data.py`, `report/` (DOCX + PDF), `slides/` (PPTX + PDF), `data/`, `figures/`, `results/`, `scripts/`, `README.txt` |
| `Group_31/revised/` | Working files: paper builder (`build_structured_paper.py`), deck builder (`build_structured_deck.py`), patch scripts, QA images (`qa2/`), earlier 16-page paper |
| `Group_31/data/Findex_Microdata_2025_updateIndia.dta` | India household microdata (3,000 adults). **Not redistributed** (World Bank access conditions) |
| `Group_31/analysis_extra.py`, `manual_coding_fraud_reviews.py`, `fetch_data.py` | Peer comparison, app-review coding, open-data download |
| `Group_31_Term_Paper_Progress_Report.pdf` | Original progress report as submitted (still lists "Sudhanshu Sah"; not in the submission folder). Corrected copy with "Sudhanshu": `Group_31_Term_Paper_Progress_Report_corrected.pdf`/`.docx` |
| `Completion_Pack/` | Plan to finish (`PLAN.md`), proofreading record, human second-coder pack (`second_coder/`) and interview pack (`interviews/`) |
| `Friend/` | Friend's submission, reference only |

Final deliverables: `Group_31_Final_Submission/Research_Report.pdf` (30 pages in the LibreOffice render; 21 tables, 6 figures, 53 references) and `slides/Group_31_Presentation_Final.pptx` (19 slides with speaker notes).
Rebuild commands (run from `C:\Users\Sudhanshu\Desktop\EF`): `python Group_31/revised/build_structured_paper.py` then export the DOCX to PDF with Word; `python Group_31/revised/build_structured_deck.py`. The final folder was assembled by a helper script kept in the session scratchpad, not in the project.

## 4. Research questions (as in the paper)
1. How do account ownership, digital payment use and device protection differ by gender, age and income, and how does India compare with peer economies?
2. Are payment users more likely than non-users to report unsolicited money requests, after adjustment?
3. Among request recipients, is a device lock associated with a lower share reporting they sent money?
4. Which groups show the largest gap between digital payment use and device protection?
5. What do public app reviews and institutional documents reveal about fraud grievances, security friction and support?
6. What price, cost and customer numbers let an institution-funded safety service break even?

## 5. Data sources
1. **India Global Findex 2024 microdata** (World Bank, ref. IND_2024_FINDEX_v02_M, DOI 10.48529/c9vy-pq51): 3,000 adults aged 15+, 199 variables, survey weight `wgt`. Percentages are weighted; n and counts are unweighted.
2. **Findex 2025 country aggregates** from the World Bank open API (source 28, year 2024): `account.t.d`, `con1`, `con18.s`, `con21.s` for India, China, Indonesia, Bangladesh, Pakistan, Brazil, South Africa, South Asia, lower-middle-income and world. India has no published `con21.s`, so our microdata estimate (9.4%) is used and marked.
3. **Public Google Play reviews** (India store) of PhonePe, Google Pay, Paytm, BHIM, SBI YONO: 15,000 fetched, 5,758 after removing reviews under 15 characters and duplicates; 2 Oct to 19 Nov 2026. Usernames not stored; one email/phone string masked.
4. **Institutional documents:** World Bank trust page, World Bank responsible financial access page, RBI circular RBI/2019-20/256 (plus a Google Pay blog, the helpline 1930 press release, a World Bank blog with global aggregates, and the NPCI live-members page for context only).
5. **Literature:** 35 academic papers, all citation details checked against Crossref; each summary checked against the abstract or paper (Luarn & Lin and Burke et al. were checked from the downloaded PDFs).

## 6. Key results (all weighted unless stated)
- Account ownership **89.0%**; made or received a digital payment **48.5%**; phone ownership **66.5%**; phone lock **57.7%** of phone owners (n = 2,141 valid).
- Women's payment use 42.7% vs men's 54.1%; lock use women 50.3%, men 62.7%; lowest vs highest income quintile payment use 34.8% vs 67.4%, lock 40.6% vs 75.2%; ages 15–24 lock 75.7% vs 60+ 22.9%.
- Unsolicited money request: **9.4%** of phone owners; **13.1%** of payment users vs **4.3%** of non-users; **21.0%** of the 219 recipients sent money (45).
- Adjusted weighted logistic model (2,145 phone owners): payment user odds ratio **3.45** (approx. 95% interval 2.24–5.30); women vs men 0.47 (0.32–0.69). Intervals are approximate (no design variables in the public file).
- Largest payment-use-minus-lock gap: ages 60+ (+33.7 points, 56.6% vs 22.9%); ages 15–24 −32.1 (43.5% vs 75.7%). Different denominators, descriptive only.
- **Peers (2024):** India account 89.0 (second to China 89.4); phone 66.5 (second lowest, above Pakistan 62.9); lock 57.6 (peers 46.4–78.0); request 9.4 vs peers 12.7–32.4.
- **App reviews:** mean rating 2.90. Keyword themes: fraud 118 (2.0%), money deducted/failed 133 (2.3%), support 306 (5.3%), blocking/verification 365 (6.3%), safety/trust language 302 (5.2%). Of the 118 fraud-keyword reviews (all read and classified): 60 reward/cashback not honoured, 15 failed or unrefunded payments, 11 blocked account/mis-selling/grievance handling, 10 spam/permissions/privacy, 9 general accusation, 7 praise, **6 unauthorised access or theft (0.1% of all reviews)**. 104 reviews (1.8%) mention device-lock or security-alert prompts (86 BHIM, 18 SBI YONO).
- **Venture model (illustrative assumptions, not findings):** fee INR 50,000 per institution per month, variable cost 10,000, acquisition cost INR 2 lakh, fixed cost INR 3 lakh per month (grows 20%/year). Contribution INR 40,000 (80%); payback 5 months; steady-state break-even **8** institutions (13 while acquiring one per month); base case −32.80, 0.00, +52.16 lakh over Years 1–3; seed request INR 75 lakh. Year 3 closing counts of 18/40/65 are 2.4%/5.3%/8.6% of about 758 live UPI entries (NPCI snapshot, undated).

## 7. Important limits (stated in the paper; keep them)
- Cross-sectional, self-reported; no causal claims; unsolicited requests are not verified fraud; sending money is not a loss amount.
- Findex describes individuals, not businesses.
- **No interviews or surveys of our own.** Qualitative evidence = institutional document themes + public app reviews (self-selected, seven weeks, five apps, English, keyword-coded then manually classified).
- **App-review coding:** first pass by an AI assistant; blind AI second pass on all 118 (94.9%); human coder on a sample of 40 (95.0%). App Store reviews: AI first pass and blind AI second pass (82.5%), no human check.
- Peer values are published aggregates without sampling errors; no statistical test.
- All financial inputs are unvalidated assumptions; no churn, tax or financing flows; no partner, investor or willingness-to-pay claimed. The NPCI count comes from a search snippet.
- Scraping Google Play reviews may conflict with the store's terms of service; the group should be comfortable with this.
- Microdata is not included in the submission (access conditions).

## 7b. Verification added 20 Nov 2026 (second session)
- **Reproduction:** `analysis_group31.py` re-run on the microdata (Linux, Python 3.13, pandas 3.1). Weighted results CSV is byte-identical; model CSV differs only at floating-point noise (max 3.6e-15); headline numbers (89.0, 48.5, 57.7, 13.1 vs 4.3, 21.0, OR 3.45) match the paper. The audit JSON differs only in the script SHA-256 (likely line endings).
- **Second-pass review coding:** all 118 fraud-keyword reviews were re-coded blind to the first-pass labels (`results/review_fraud_second_pass.csv`, column `second_pass`). Agreement 112/118 = 94.9%, Cohen's kappa 0.93. The 6 disagreements do not change any headline: unauthorised access/theft stays at 6, reward/cashback is 59 vs 60. **Caveat: both passes were done by AI sessions, so this is a consistency check, not an independent human second rater.** The paper (Methodology 3.5, table note, limitations) and deck now report the second pass. Rebuilt on Linux: PDFs were rendered with LibreOffice (27 pages) because Word is not available; the earlier Word-made PDF was 25 pages. Re-export from Word if the exact earlier layout matters.
- Progress report vs paper: report RQ1-4 became RQ1-6; the uploaded aggregate file (8,577 x 438) is replaced by World Bank API peer indicators; the report says "Sudhanshu Sah", the paper "Sudhanshu".

## 7c. Fixed 20 Nov 2026 (third pass)
- Discussion RQ1 wrongly said digital use was lower for older adults (Table 7: payment use is highest at 60+); corrected. Stray "and" removed in 3.1.
- Interviews and a human second coder are NOT done: they need people. Ready-to-use packs and the step-by-step plan are in `Completion_Pack/`. The paper still states that no interviews were conducted.

## 7d. Secondary qualitative evidence added 20 Nov 2026 (fourth pass)
- **Why:** the group could not run interviews. Reddit blocks scripted access (not bypassed), so no Reddit data. Instead: (a) **Apple App Store reviews** of the same five apps via Apple's public customer-review feed (`scripts/fetch_appstore.py`, `scripts/analysis_appstore.py`; 2,090 reviews, 30 Apr to 18 Nov 2026; 57 fraud-keyword reviews classified by one coder, no second pass; 2 describe unauthorised access, 0.1%); (b) **five published qualitative studies** analysed as secondary evidence: Mungara et al. 2025 (USENIX Security, 26 interviews), Bajaj et al. 2026 (ASIA CCS, 46 interviews), Jain et al. 2021 (COMPASS, 24 merchants and 10 agents), Aadil et al. 2023 (MicroSave policy brief 28, 50 users and 10 officials), Sengupta et al. 2025 (CIS India, 18 interviews, 7 focus groups, survey of 3,784).
- **In the paper:** Methodology 3.3 sources 5 and 6, 3.5; Results 4.10 (Table 15) and 4.11 (Tables 16 and 17: eight themes S1 to S8, counts of studies not respondents); Discussion "Evidence beyond Google Play"; abstract, RQ5, limitations and conclusion updated. Provenance in `results/published_studies*.csv` and `results/appstore_*`.
- **Caveats:** CIS India study was coded from its publisher summary page only, not the full report. The GSMA India Consumer Scam Report 2025 was read but not used (it is a survey, and the PDF carries a DRAFT watermark). Theme coding is by one coder (AI-assisted); the group should check Table 17 against the papers. One reference author is named Sah (R. Sah, MicroSave) because that is how the source is credited; it is not a group member. Tables 18 to 21 were renumbered (canvas, alternatives, seed, risks).

## 7e. Weaknesses addressed 20 Nov 2026 (fifth pass)
- **CIS India study** now coded from its full 128-page report (S1 becomes 5 of 5; survey figures added to Table 17).
- **NPCI count replaced:** the undated 758 figure is gone. The paper now uses the Government of India (PIB) UPI factsheet of 24 Aug 2026: 741 live banks in July 2026; Year 3 shares 2.4%, 5.4%, 8.8%.
- **Intervals:** `scripts/analysis_sensitivity.py` adds a Kish design effect (1.43, effective n 1,501) and variance inflation for assumed extra design effects 1.5, 2, 3. Payment-user and gender results survive; tertiary education does not (Section 4.3, limitations).
- **App Store coding:** a separate AI instance re-coded the 57 reviews blind: 82.5% agreement, kappa 0.78; unauthorised access 2 vs 4 (0.1% vs 0.2%).
- **Notebook** now has App Store and sensitivity cells (outputs stored). **TA note** on progress-report differences: `Completion_Pack/TA_NOTE.md`; the paper also states the differences (1.4, 3.3).
- **Human second coder done** (reported by the group as a person outside the group who did not see the first-pass labels): stratified sample of 40 of the 118 Google Play fraud-keyword reviews, 38/40 agreement with the first pass (95.0%, kappa 0.93), 39/40 with the AI second pass; 0 of 60 non-keyword reviews described fraud (`results/human_second_coder_partA.csv`, `_partB.csv`). Disagreements: A21 and A25. The coder's identity is not recorded in the repo. Human reliability rests on 40 reviews only; the 57 App Store reviews have no human check.
- **Still not fixable by software:** no own fieldwork, all finance inputs are assumptions.

## 8. Open items (human steps)
1. Read the final PDF and slides once: names, dates, numbers, anything that reads oddly or cannot be defended.
2. Audit the review classification file (and optionally have a second person re-code a sample).
3. Decide whether to keep the app-review scraping and the numbered citation style.
4. Optional: delete old drafts and test files in `Group_31/` (nothing was deleted; the submission folder only holds copies).
5. If the course expects primary qualitative work, real interviews are needed; they were not done.

## 9. Technical notes
- Python (miniconda 3.14). Packages installed with `pip --user` for this work: pandas, numpy, matplotlib, nbformat, nbclient, ipykernel, google-play-scraper. A live Jupyter kernel failed in the tool environment, so `analysis.ipynb` stores outputs from running each script; it can be re-run normally.
- The PowerShell tool and the Bash tool saw different Python package locations; use the Bash `python` for the analysis scripts.
- Word (COM) is used to export the DOCX to PDF; PowerPoint (COM) exports the slides to PDF.
- Weighted results and the model CSVs reproduce the earlier audited outputs exactly (byte-identical).

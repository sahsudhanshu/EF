# Project context: Group 31 term paper (Entrepreneurial Finance)

Share this file with anyone (or any AI session) picking up the work. Last updated 20 November 2026.

## 1. What this is
- **Course:** Entrepreneurial Finance. **Group 31.** **Authors:** Rushal Verma (IIT2024045), Vichanshu Raj (IIT2024083), Sudhanshu (IIT2024081) (use "Sudhanshu" only; "Sah" removed on request).
- **Topic:** Mobile banking, financial inclusion and cybersecurity risk in India.
- **Title:** *Mobile Banking: Financial Inclusion vs Cybersecurity Risks*. Subtitle: *Evidence from the Global Findex Database 2025 (India survey, fielded in 2024), public app reviews and published interview studies, with implications for entrepreneurs.* (Changed 20 Nov 2026: the group confirmed the actual topic is "Mobile banking: financial inclusion vs cybersecurity risks"; see `Completion_Pack/TOPIC_ALIGNMENT_PLAN.md`.)
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

Final deliverables: `Group_31_Final_Submission/Research_Report.pdf` (39 pages in the LibreOffice render; 27 tables, 7 figures, 54 references, Appendix A) and `slides/Group_31_Presentation_Final.pptx` (21 slides with speaker notes).
Rebuild commands (run from `C:\Users\Sudhanshu\Desktop\EF`): `python Group_31/revised/build_structured_paper.py` then export the DOCX to PDF with Word; `python Group_31/revised/build_structured_deck.py`. The final folder was assembled by a helper script kept in the session scratchpad, not in the project.

## 4. Research questions (as in the paper)
1. How do account ownership, digital payment use and device protection differ by gender, age and income, and how does India compare with peer economies?
2. Are payment users more likely than non-users to report unsolicited money requests, after adjustment?
3. Among request recipients, is a device lock associated with a lower share reporting they sent money?
4. Which groups show the largest gap between digital payment use and device protection?
5. What do public app reviews and institutional documents reveal about fraud grievances, security friction and support?
6. What price, cost and customer numbers let an institution-funded safety service break even?

## 5. Data sources
1. **India microdata, Global Findex Database 2025 (survey fielded in 2024)** (World Bank, ref. IND_2024_FINDEX_v02_M, DOI 10.48529/c9vy-pq51): 3,000 adults aged 15+, 199 variables, survey weight `wgt`. Percentages are weighted; n and counts are unweighted.
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

## 7f. Added 20 Nov 2026 (sixth pass)
- Student IDs on the paper, deck, IEEE report and README. Table 18 (answers to RQ1 to RQ6) added at the start of the Discussion; tables 19 to 22 renumbered; paper now 31 pages (LibreOffice render).
- `report/IEEE_Report.docx/pdf`: 2-page condensed IEEE-style version built by `scripts/build_ieee_report.py` (10 pt two columns; the TA's Times New Roman 12 rule applies to the full paper).
- Automated check: tables, numbering, fonts, caption order, abstract length and references all pass (117 checks).

## 7g. Topic alignment 20 Nov 2026 (seventh pass)
- **Topic confirmed by the group:** "Mobile banking: financial inclusion vs cybersecurity risks". Title changed everywhere (paper, slides, IEEE report, notebook, README, metadata); the venture proposal is no longer in the title (it stays as Section 5.3). Plan: `Completion_Pack/TOPIC_ALIGNMENT_PLAN.md`.
- **New quantitative analysis:** inclusion vs risk by group (`scripts/analysis_inclusion_risk.py`; Table 8, Figure 4): 18 groups, rank correlation 0.38 (payment use vs exposure) and 0.63 (payment use vs lock use); exposure highest among tertiary-educated (17.9%) and the lowest income quintile (12.5%), lowest at ages 60+ (4.1%).
- **New web data:** reviews of eight bank mobile-banking apps (`scripts/fetch_bankapps.py`, `analysis_bankapps.py`): 6,240 reviews (4,279 Google Play, 1,961 App Store), 65 fraud-keyword reviews classified (first pass plus blind AI second pass: 57/65 = 87.7%, kappa 0.84; no human check); 149 security-friction reviews (SIM binding 69, biometrics 46, developer or root checks 14). Compared with 7,848 payment-app reviews (Tables 17 and 18, Section 4.11). Reddit remains blocked and unused.
- **Paper now:** Tables 1 to 25, Figures 1 to 7; Section 4.12 is the published studies (Tables 19 and 20); Table 21 answers the research questions including a central inclusion-vs-risk row.
- **Check by hand:** Table 20 (published studies) and the bank-app classification (`results/bankapps_fraud_manual_codes.csv`).

## 7h. Fixes after the audit, 20 Nov 2026 (eighth pass)
- **Audit result:** all eight analysis scripts re-run to identical results in a clean copy; `analysis.ipynb` runs end to end.
- **Significance tests** (`scripts/analysis_tests.py`, `results/significance_tests.csv`): RQ3 lock vs sending money Fisher exact p = 0.11 (not significant); bank vs payment apps differ significantly (Holm p < 0.001) for fraud keywords, failed payments, safety language and security friction, but not for support (p = 0.87) or blocking (p = 0.12); rewards 3/65 vs 77/175 and blocks/grievances 25/65 vs 21/175 (both p < 0.001).
- **Hinglish sensitivity** (`scripts/analysis_hinglish.py`): the English dictionary stays the main one; an extension flagged 41 more reviews (classified by one coder); unauthorised or unexplained-debit reports in Play payment-app reviews would rise from 6 to 12 of 5,758. Section 4.13.
- **Appendix A** (Tables 26 and 27): the seven categories and all dictionaries. README now says the builder scripts run only from the full project layout.
- **Human checks still pending (prepared, not done):** `Completion_Pack/second_coder_round2/` (122 App Store and bank-app reviews; the answer key is in a git-ignored private folder and must stay local) and `Completion_Pack/table20_check/` (verify Table 20 and Table 19 figures).

## 7i. State at the last push (20 Nov 2026)
- `main` at commit 51f78b6, then this update of `CONTEXT.md` and `CHAT.md`. Paper 39 pages (LibreOffice render), 27 tables, 7 figures, 54 references, Appendix A; deck 21 slides; IEEE report 2 pages; notebook 30 cells; 153 automated checks pass.
- Review coding: all classification by an AI first coder with blind AI second passes, except 40 Google Play reviews checked by a human blind coder (95.0%, kappa 0.93; reported on the user's word). App Store and bank-app reviews have no human check yet. Table 20 was extracted by AI reading and is unverified by a person.
- The round-2 answer key (`Completion_Pack/second_coder_round2/PRIVATE_DO_NOT_SHARE/`) is git-ignored; never commit it.
- `CHAT.md` is the narrative log of the sessions.

## 8. Open items (human steps)
1. Re-code `Completion_Pack/second_coder_round2/PartC_coding_sheet_BLANK.csv` (122 reviews, about 1 hour), run `compute_agreement_round2.py` with the private key and update the paper with the numbers.
2. Fill `Completion_Pack/table20_check/TABLE20_CHECK_SHEET.csv` (30–45 minutes) and apply corrections to Table 20 and Table 19 figures, the slides and results files.
3. Final read of the paper and slides in Word and PowerPoint; export PDFs from Word (current PDFs are LibreOffice renders).
4. Optional: the group's own interviews (`Completion_Pack/interviews/`); cleanup of old drafts in `Group_31/` (nothing deleted so far).
5. Known limits to keep stated: finance inputs are unvalidated assumptions; intervals are not design-based; app-store coding is partly AI-assisted.

## 9. Technical notes
- Python (miniconda 3.14). Packages installed with `pip --user` for this work: pandas, numpy, matplotlib, nbformat, nbclient, ipykernel, google-play-scraper. A live Jupyter kernel failed in the tool environment, so `analysis.ipynb` stores outputs from running each script; it can be re-run normally.
- The PowerShell tool and the Bash tool saw different Python package locations; use the Bash `python` for the analysis scripts.
- Word (COM) is used to export the DOCX to PDF; PowerPoint (COM) exports the slides to PDF.
- Weighted results and the model CSVs reproduce the earlier audited outputs exactly (byte-identical).


## 7j. Condensed submission, 20 Nov 2026 (ninth pass) - CURRENT STATE
- **Decision by the user:** only the 12-page paper is used. The earlier ~39-page paper, the 2-page IEEE report and the old 21-slide deck are **no longer part of `Group_31_Final_Submission/`** (they remain in git history and in `Group_31/revised/`, `Group_31/report/` and `Group_31/slides/`; nothing was deleted there).
- **Submission folder now:** `Research_Report.pdf` and `report/Group_31_Research_Paper.(docx|pdf)` = the **12-page paper** (Word export; 4 tables, 2 figures, 48 references of which 35 are academic; top and bottom margins 0.9 in); `slides/Group_31_Presentation_Final.(pptx|pdf)` = **19 slides** with native charts and speaker notes; `analysis.ipynb`, `fetch_data.py`, `data/`, `figures/`, `results/`, `scripts/`, `README.txt`.
- **Builders:** `Condensed/build_short_paper.py` (reads reference entries from `Condensed/references_source.txt`, cites with the old reference numbers and renumbers by first appearance) and `Condensed/build_short_deck.py`; copies in `Group_31_Final_Submission/scripts/condensed/`. Run from the project root (`Desktop/EF`), then export the DOCX to PDF with Word.
- **What the 12-page paper left out compared with the old full paper:** the full 18-group table, the data-sources table, theme-share tables, the published-studies table, the RQ-answers table, the business-model canvas table, the peer figure, appendices, six references (Lusardi and Mitchell, Robinson et al., Venkatesh et al., Kashyap and Wetherilt, Findex 2014, the World Bank blog and the PIB UPI factsheet) and the UPI market-anchor sentence (741 banks).
- **Second coder on the 122 App Store and bank-app reviews:** per the user, **a person who used software, including AI tools, as an aid but made each coding decision**, blind to the first-pass labels and the key. Agreement with the first pass 102/122 = 83.6% (kappa 0.80; App Store 80.7%, 0.76; bank apps 86.2%, 0.81); with the AI second pass 104/122 = 85.2% (0.82). Verified by re-running `compute_agreement_round2.py`. The coder labelled 8 of 122 as unauthorised access or theft (first pass 5, AI second pass 8); 10 of the 20 disagreements were first-pass "general accusation" reviews. The paper says "a person who used software, including AI tools, as an aid but made each coding decision, as reported by the group" (clarified by the user 20 Nov 2026). Filled sheet: `Completion_Pack/second_coder_round2/PartC_coding_sheet_filled.csv`; output: `results/second_coder_round2_agreement.txt` (also a notebook cell).
- **Open items now:** (1) final read of the 12-page paper and 18 slides in Word and PowerPoint; (2) the group should be able to explain the coding method and the two second-coder checks if asked; (3) optional: commit and push.

## 7k. Additions after comparing with the friend's submission, 20 Nov 2026 (tenth pass)
- **Added to the 12-page paper:** an entrepreneurial-finance paragraph in 2.2 with five verified sources (Stiglitz and Weiss 1981; Berger and Udell 1998; Beck and Demirguc-Kunt 2006; Evans and Jovanovic 1989; Berg et al. 2018, checked on Crossref and OpenAlex); JEL codes (G21, G23, L26, O16); a Data availability paragraph; an "Answers to the research questions" table (Table 4); a review-category figure (Figure 2, `figures/figure8_review_categories.png`, made by `scripts/condensed/make_figure8.py`). To keep 12 pages the group table, the scenario table and the finance figure were dropped (numbers stay in the text). Paper now: 4 tables, 2 figures, 48 references (35 academic), Word export 12 pages.
- **Deck (19 slides):** added the two charts from `Group_31_Dataset_Key_Findings.pdf` that were missing: access vs active use (account 89.0, phone 66.5, digital payment 48.5, plus the gender comparison) and device-lock adoption by group (six bars). The exposure chart and the 118-review category chart were already in the deck.
- **Not added:** a 3-page IEEE-format version (the friend has one; removed from our folder at the user's request).

- **Slide removed for now (20 Nov 2026):** "Analysis and coding reliability" is out of the deck (18 slides). It can be restored by setting `SHOW_RELIABILITY = True` in `build_short_deck.py`. `PRESENTATION_GUIDE.md` was renumbered and keeps the slide's script as a backup (section 10).

- **Figures added to the paper (20 Nov 2026):** the user said page count no longer matters. The paper now has **9 figures** (access and gender; device lock by group; exposure and sending money; inclusion vs exposure by group; payment use vs lock; peer economies; review categories; published-study themes; finance scenarios) and is **15 pages** in Word. New charts are made by `scripts/condensed/make_paper_figures.py` (Times New Roman, same numbers as the tables) and saved as `figures/pfig_*.png`. The 12-page limit no longer applies.

- **Slide 6 restored (20 Nov 2026):** "Analysis and coding reliability" is back in the deck (19 slides; `SHOW_RELIABILITY = True` in `build_short_deck.py`). `PRESENTATION_GUIDE.md` is renumbered back (Part 1 slides 1 to 6, Part 2 slides 7 to 12, Part 3 slides 13 to 19) with the slide's script in place.

## 7l. FINAL STATE after the last audit, 20 Nov 2026 (supersedes older counts above)
- **Paper:** `Group_31_Final_Submission/Research_Report.pdf` = **15 pages** (Word export), **9 figures, 4 tables, 48 references (35 academic)**, TA structure, Times New Roman 12. The "12-page" statements above are historical.
- **Deck:** **19 slides** (coding-reliability slide included), speaker notes on every slide.
- **Audit result (automated):** all headline numbers in the paper match `results/` (weighted results, model, peers, finance, second-coder agreement); all headings of the TA structure present; abstract 169 words; deck contains the paper's headline numbers; no stale text ("extended report", "TODO") in the paper.
- **Known open points:** (1) the repository is **public** and still tracks the World Bank microdata file (`data/` and `Group_31/data/`) and `Completion_Pack/second_coder/PartA_answer_key_DO_NOT_OPEN.csv`; (2) the numbers quoted from the five published studies were extracted by AI and are not checked by a person; (3) the identity of the 40-review human coder is not recorded; (4) the final read in Word and PowerPoint is the group's.
- **Cleanup (20 Nov 2026):** removed scratch files (rendered QA page images in `Group_31/revised/qa` and `qa2`, patch scripts, the paper text dump, preview PNGs in `Condensed/`) and four unused old figures from `Group_31_Final_Submission/figures/`. Re-ran all ten analysis scripts in a clean copy: every file in `results/` is byte-identical to the stored version, and the builders still reproduce the submitted paper text. Old drafts (`Group_31/revised/Group_31_Term_Paper_Revised.*`, `IEEE_Report.docx`, `Group_31/report`, `Group_31/slides`, `Group_31/Research_Report.*`) and `Friend/` were left in place.
- **Title block (20 Nov 2026):** the date was removed from the paper and the title slide, and the author order is now Rushal Verma (IIT2024045), Sudhanshu (IIT2024081), Vichanshu Raj (IIT2024083) in the paper, deck and README.
- **Dataset naming fix (20 Nov 2026):** the dataset is the *Global Findex Database 2025*; the India survey was fielded in 2024. Title, abstract and slide wording now say "Global Findex Database 2025 (India survey, fielded in 2024)" instead of "2024 Global Findex".

## 7m. Full cross-verification, 20 Nov 2026 (final audit)
- **Verified against `results/` and the data (all match):** every number in Tables 1 to 3 and the model text (counts, weighted shares, odds ratios, design-effect sensitivity at 1.5, 2 and 3); the 18-group values and both rank correlations; all peer values; review dataset sizes, mean ratings, theme shares, fraud-keyword counts, the seven-category counts for all three review sets, kappas (0.93, 0.78, 0.84) and agreements; chi-square, Holm and Fisher p-values; human Part A (38 of 40, kappa 0.93) and Part B (0 of 60); the round-2 second coder (102/122 = 83.6%, kappa 0.80; 8 vs 5 vs 8 unauthorised labels; 10 of 20 disagreements were first-pass general accusations); published-study theme counts; the whole finance model (contribution, payback, break-even 8 and 13, sensitivity 6 to 12, scenario surpluses, seed 75 and 81.80); every number in the nine figures and on the 19 slides.
- **Re-run in a clean copy:** all analysis scripts reproduce every file in `results/` byte for byte.
- **Fixed in this audit:** (1) the 104 device-lock prompt reviews had no script behind them, now `scripts/analysis_lock_prompts.py` and `results/review_device_lock_prompts.json`; the paper now describes the dictionary correctly (device-lock, security-alert or developer-option prompts, 86 BHIM); (2) the Hindi/Hinglish classification (6 to 12) was not stored, now `results/hinglish_extra_coded.csv` (re-coded independently; it gives the same counts); (3) slide 14 wording ("Redress: of 91 victims who reported fraud, 59 could not recover their money").
- **Source figures checked against the published papers (full text):** Bajaj et al. (46 participants; 45 of 46 said trusting the receiver matters; recipient trust badge rated highest, mean 8.26 of 10) and Jain et al. (24 merchants and 10 agents; fake payment confirmations reported by 12 merchants). **Not verifiable in this audit:** Sengupta et al. (the "91 reported, 59 could not recover" figure; the 3,784 survey, 18 interviews and 7 focus groups are confirmed on the report's summary page) and the Mungara and Aadil figures. The group should check these against the papers before presenting.

## 7n. Aligned with the TA's reference documents, 20 Nov 2026
- The TA's reference files (`Term paper for reference.docx`, an IIIT Allahabad student term paper, and the journal article `1-s2.0-S0001691825009886-main.pdf`, Puri, Kumar & Singh 2025, Acta Psychologica) both use **APA author-year citations** and an alphabetical reference list. The paper was switched from numbered citations to **APA author-year** (for example Suri & Jack, 2016; Demirguc-Kunt et al., 2017), the reference list is alphabetical with `2025a/2025b` and `n.d.-a/n.d.-b` suffixes for same-author same-year entries, and every in-text label was matched to a reference entry.
- Structure now mirrors the TA's `Paper structure.pdf` exactly: Introduction has subsections 1.1 Background, 1.2 Problem and importance, 1.3 Research gap, 1.4 Research questions (ending with a section roadmap as in the journal article); Methodology subsections use the TA's names (3.1 Research Design to 3.6 Ethical Considerations) and each has a Justification; Data availability moved from the Conclusion into 3.4; main title now ends "in India" (scope).
- The title block also names the institution ("Indian Institute of Information Technology, Allahabad") as on the TA's reference paper; **this is an assumption from the student IDs and the reference paper, remove it if it is wrong.** The paper is now 16 pages in Word.

## 7o. Official submission package, 20 Nov 2026
- **Instructor guideline (Google Classroom):** one zip named with the group number containing four items: the final term paper in **Word** format, **all code**, **all tables and figures**, and the **dataset (processed and unprocessed)**. **Deadline: 21 Nov 2026, 06:00 AM.** The instructor also warned that **AI-based content writing may reduce marks.**
- **Built:** `Group_31.zip` in the project root (3.5 MB, 128 files; staging copy in `Submission_Zip/`, both git-ignored because the zip holds the licensed microdata). Layout: `1_Term_Paper/Group_31_Term_Paper.docx`; `2_Code/` (scripts, notebook, fetch scripts, results); `3_Tables_and_Figures/` (nine numbered figures, the four paper tables as CSV, supporting results); `4_Dataset/raw/` (Findex microdata .dta, raw app-review CSVs, API peer extract) and `4_Dataset/processed/` (`findex_india_analysis_ready.csv`, `reviews_processed.csv`, built by `scripts/make_processed_data.py`).
- **Verified:** unzipped into a clean folder, all 12 scripts run and every results file and both processed files are identical to the zip's copies; processed reviews = 14,088 rows with fraud-keyword counts 118, 57, 65 as in the paper.
- **Honesty note:** the paper, analysis code and slides were produced with heavy AI assistance (Claude). The instructor's AI-content warning therefore applies; the group has to decide how to handle it (disclose, and/or rewrite in its own words) before submitting. Nothing in the zip claims the work is AI-free.
- **Sengupta et al. figure verified (21 Nov 2026):** the CIS report (section on redressal mechanisms) says of those who reported digital financial fraud to authorities, 10 of 91 (11%) recovered all the money, 59 of 91 (65%) were unable to recover, and 12 of 91 (13%) stopped pursuing recovery. The paper and slide 14 now say "reported the fraud to authorities".

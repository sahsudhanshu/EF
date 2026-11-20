# Proofreading record (20 Nov 2026)

**Checked (script re-run plus reading) against `Group_31_Final_Submission/results/`:** survey analysis re-run on the licensed microdata (weighted table identical; model equal to floating-point precision); headline figures in Abstract, Results, Discussion and Conclusion (89.0, 48.5, 66.5, 57.7, 9.4, 13.1, 4.3, 21.0, OR 3.45, gaps in Table 7, peer comparison arithmetic: 10, 14 and 12.5-point comparisons); Table 14 totals (118); the author name (only "Sudhanshu" appears in the paper, deck and corrected progress report).

**Fixed in this pass**
1. Discussion (RQ1) said digital use was lower among older adults. Table 7 shows payment use is highest at ages 60+ (56.6%); only device protection is lowest there. Sentence corrected.
2. Methodology 3.1 had a stray "and" in the list of components.
3. Slide 3 listed five research questions with RQ5 = break-even; the paper has six (RQ5 = reviews and documents, RQ6 = break-even). Slide 3 and the method slide now match the paper.
4. Surname: the progress report PDF in the repo still said "Sudhanshu Sah". A corrected copy was built: `Group_31_Term_Paper_Progress_Report_corrected.pdf` (the original is untouched).

**Slides:** all 18 slides were rendered and inspected visually on 20 Nov 2026; no overflow or clipping seen.

**Needs human eyes**
- Word layout: open the DOCX in Word; check table breaks and figure placement (the PDF here was rendered by LibreOffice, 27 pages, not Word).
- Slides: open the PPTX in PowerPoint and check text fit on every slide; the checks here were rendering only.
- Reference list: all 35 DOI links were tested on 20 Nov 2026. 34 are registered in Crossref and the World Bank microdata DOI resolves to the World Bank catalogue. Several publisher sites return 403 to scripts but open in a normal browser; click two or three yourselves.
- Anything in the paper that names your own work (the NPCI count of about 758 UPI entries comes from a search snippet with no stated date: decide whether to keep it).
- Wording you are not comfortable defending. Everything in the paper is yours to defend.

**Known limitations kept in the text:** single first-pass coder, illustrative finance model, approximate (non-design-based) intervals, no interviews yet.

## Added 20 Nov 2026: secondary qualitative evidence
Check by hand before submitting: (1) Table 20 (themes in the published studies; was Table 17 before the 20 Nov topic change) against the five studies (counts of studies per theme and every quoted figure: 32%/24%/20% of 50 users, 12 of 24 and 3 of 24 merchants, 45 of 46 twice, badge mean 8.26 vs 4.78, 60% of net-banking users); (2) the CIS India row (now coded from the full report: check the 6.2%/39%/11% figures against Chapter 6); (3) the App Store category counts (57 reviews, `results/appstore_fraud_manual_codes.csv`): first pass plus a blind AI second pass, 82.5% agreement; a human should re-code the disagreements; (4) that you are comfortable citing the MicroSave policy brief and CIS report as grey literature.

Also check: the PIB factsheet figure (741 live banks, July 2026) at https://pib.gov.in/FactsheetDetails.aspx?Id=150962, and the design-effect sensitivity numbers in Section 4.3 against `results/Group_31_design_sensitivity.csv`.

## Added 20 Nov 2026: topic alignment
Check by hand: Table 8 and Figure 4 (inclusion vs exposure by group, from `results/inclusion_risk_by_group.csv`); Table 17 and 18 (bank-app themes and the manual classification of 65 reviews, `results/bankapps_fraud_manual_codes.csv`, first pass plus blind AI second pass only); the eight bank apps and store identifiers in `scripts/fetch_bankapps.py`.

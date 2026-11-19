# Plan to finish the Group 31 term paper

Status on 20 Nov 2026: paper (27 pages in the LibreOffice render), 18-slide deck, notebook and data scripts are complete and verified. Three things need people, not software. This plan covers them in order. The submission deadline is not recorded in the repo: confirm it with the TA first and work backwards.

| # | Task | Who | Time | Needed for |
|---|---|---|---|---|
| 1 | Final read of PDF and slides | all three, split by section | 2 to 3 hours | any submission |
| 2 | Human second coder on review sample | one person not involved in the first pass | 1.5 hours | RQ5 reliability |
| 3 | Own interviews (8 to 10) - OPTIONAL | all three, about 3 each | 4 to 6 days incl. recruiting | only if the course demands primary qualitative work |
| 4 | Fold results into paper and deck, rebuild | one person | 2 to 3 hours | after 2 and 3 |
| 5 | Submit | one member | 30 minutes | |

If the deadline is close, do 1 and 2 only and submit. Since 20 Nov 2026 the paper also has secondary qualitative evidence (App Store reviews and five published interview studies, Sections 4.10 and 4.11), so it no longer relies on reviews alone; it still says honestly that the group ran no interviews. Do 3 only if the course demands primary qualitative work and you have at least a week.

## Step 1: Final read (see PROOFREAD.md)
- Assign sections: Rushal = Sections 1 to 3 and references; Vichanshu = Section 4 and tables; Sudhanshu = Section 5, 6, abstract and slides.
- Check each number against `Group_31_Final_Submission/results/`. PROOFREAD.md lists what has already been checked and what to look at by eye (names, dates, layout in Word).
- Open `report/Group_31_Research_Paper.docx` in Word and export the PDF yourselves if you want the original 25-page layout.
- Make sure every member can explain one weakness: single-source review coding, illustrative finance inputs, no design-based intervals.

## Step 2: Human second coder (DONE 20 Nov 2026: 40 reviews, 95.0% agreement; see results/human_second_coder_partA.csv)
The instructions below are kept for anyone who wants a larger sample or a human check of the App Store reviews.

1. One person who did not take part in the first coding reads `CODEBOOK.md` and fills `PartA_coding_sheet_BLANK.csv` (40 reviews) and `PartB_missed_fraud_check_BLANK.csv` (60 reviews). Do not open the answer key.
2. Run `compute_agreement.py` (command in the codebook). Expect agreement above 80% and kappa above 0.6; if lower, discuss the disagreements and refine the categories, then recode all 118 and update the tables.
3. Paper edits (Methodology 3.5, Table 14 source note, limitations 5.4): replace "no independent human rater" with the real result, e.g. "a human coder re-coded a stratified random sample of 40 of the 118 reviews; agreement with the first pass was x% (kappa y)". Edit `Group_31/revised/build_structured_paper.py` (search for "second pass") and rebuild.

## Step 3: Interviews (folder `interviews/`)
1. Day 0: ask the TA whether interviews need formal ethics approval; read `INTERVIEW_PROTOCOL.md` together; each member practises the guide once.
2. Days 1 to 4: recruit and interview. Target 8 to 10: 3 merchants, 4 users (include women and 55+), 1 to 3 institution staff. Fill `interview_notes_template.csv` the same day.
3. Day 5: code themes with `THEME_CODEBOOK.md`; two members independently code 3 interviews and compare. Run `tally_themes.py`.
4. Day 6: use `PAPER_INTEGRATION_TEMPLATE.md` to write the new Methodology, Results 4.12, Discussion and limitation text. Update every place that says no interviews were conducted: abstract (if mentioned), 3.1, 3.3, 3.6, 5.4, the deck (slides on qualitative method and limits), `CONTEXT.md`, `README.txt`. Run `grep -rn -i "no interviews" Group_31/revised/*.py` to find them.
5. Only claim what was done. If you complete fewer than 6 interviews, call them "exploratory".

## Step 4: Rebuild
    python3 Group_31/revised/build_structured_paper.py
    python3 Group_31/revised/build_structured_deck.py
Export both to PDF from Word and PowerPoint, copy into `Group_31_Final_Submission/` (report/, slides/, Research_Report.pdf), copy the updated builders to `scripts/`, and add the interview notes (anonymised) to `results/`. Do not commit names or contact details.

## Step 5: Submit
Send `Group_31_Final_Submission/` (without the survey microdata, per World Bank access conditions). One member submits; the name on the paper is "Sudhanshu" only.

## Decisions for the group
- Keep scraping-based app reviews? (Google Play terms may restrict scraping; data are public and no usernames are stored.)
- Keep numbered citations with APA entries (the TA allowed any standard style).
- Whether to include the interviews at all if time is short.

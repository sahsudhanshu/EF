# Checking Table 20 (and Tables 19) of the paper

Table 20 (Section 4.12) says which of eight themes each of five published studies reports, and quotes a figure for most themes. These were extracted by reading, so a person should confirm them. Give this folder to one person who did not build the table; it takes about 30 to 45 minutes.

**Files:** `TABLE20_CHECK_SHEET.csv` (open in Excel or Google Sheets).

**What to do**
1. Download the five studies (links are in the sheet's `study` column; the Mungara and CIS reports are long, so search inside them rather than reading everything).
2. Rows starting `T` (40 rows): for each theme and study, the `paper_says` column says whether the paper claims the study reports the theme. Decide yes or no in `verifier_agrees_yes_no`. If you disagree, say what is right in `correct_answer_if_no`. A theme counts only if the study's own text reports it (a passing mention does not count).
3. Rows starting `F` (28 rows): each is a figure or fact quoted in the paper. Find it using `where_to_look` and write `yes` if it matches, `no` if not (put the correct figure in `correct_answer_if_no`). Use `notes` for doubts.
4. Send the filled sheet back. Every `no` becomes a fix in the paper, the slides and `results/published_studies*.csv`.

Rule of thumb: when unsure, write `no` and a note; it is better to correct the table than to leave a doubtful claim.

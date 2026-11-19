# Chat log: how the Group 31 term paper was finished

A chronological summary of the working session (not verbatim). For the project state see `CONTEXT.md`.

## Starting point
- The user shared an earlier summary of the project: a 16-page paper (`Group_31_Term_Paper_Revised`), a presentation built before the financial content, the progress report, and a friend's submission as a quality reference.
- The TA then sent a **required paper structure** (`Paper structure.pdf`) and said students writing research papers must follow it.

## 1. Restructuring to the TA's format
- Read the structure PDF: Abstract and Keywords, six numbered sections, References; Times New Roman 12; table labels above, figure labels below; at least 30 papers in the literature review.
- Found that the old paper did not follow it (contents page, key findings page, venture sections placed separately).
- Built a new generator, `build_structured_paper.py`, producing the DOCX, then exported the PDF through Word.
- Verified 35 real academic papers via the Crossref API (titles, authors, journals, DOIs), wrote a themed literature review, and moved all interpretation out of Results into Discussion 5.1–5.4. The venture material went under managerial implications; financial inputs went to Methodology, outputs to Results.

## 2. Completing the remaining phases
- Added RQ3 and RQ4 from the progress report (lock status vs sending money; largest gap between payment use and device protection). New result: ages 60+ show the largest gap (+33.7 points).
- Added a comparison with published World Bank Findex aggregates (79% world, 75% low- and middle-income account ownership, 61% digital payment use), verified on the World Bank blog.
- Rebuilt the presentation from scratch to follow the paper structure (python-pptx), with native charts and speaker notes.
- Ran automated checks: table percentages against the audit file, financial table against the model CSV, caption and reference numbering, all references cited.

## 3. Verifying the literature summaries
- The user asked how to check the summaries; the assistant listed the papers with DOI links.
- The user then asked the assistant to fetch the papers. Abstracts were retrieved (Crossref, OpenAlex, Semantic Scholar) and compared with the paper's sentences. Corrected: Banerjee et al., Gordon & Loeb, Anderson et al., Button et al., Aker et al. (Niger), Bachas et al., Downs et al., Ozili, Arner et al., Burke et al.
- The user downloaded the Luarn & Lin and Burke et al. PDFs; both abstracts were read and the Burke sentence was corrected (survey experiment; effects last three months only with a reminder).
- One mislabelled link was corrected (a WorldCat page had been called "World Bank search results").

## 4. Decisions by the user
- No page limit and standard citation style (TA confirmed). Only the structure must match.
- Create a final submission folder with everything, without unnecessary files (copied, not deleted).
- Do not include the progress report (it still lists "Sudhanshu Sah").

## 5. A gap found when the user asked "have you completed everything?"
- The qualitative document-review themes had been dropped when restructuring. Added them back (Methodology 3.5, Results, Discussion, a slide).

## 6. The friend's layout and the three limits
- The user shared a screenshot of the friend's submission (`data`, `figures`, `report`, `slides`, `analysis.ipynb`, `fetch_data.py`, `Research_Report.pdf`) and asked to include the same kinds of things.
- The user then asked the assistant to "find out the dataset and do this" for three stated limits: no primary qualitative work, an assumption-only financial model, and a global comparison that used published totals rather than data.
- Found the World Bank Findex country indicators on the open API (`account.t.d`, `con1`, `con18.s`, `con21.s`) and fetched peers for 2024. India's account ownership (89.0%) and phone ownership (66.5%) match our microdata exactly.
- Collected public Google Play reviews of five payment apps (15,000 fetched, 5,758 kept). Keyword-coded five themes, then read and classified all 118 fraud-keyword reviews. Finding: half are about unpaid cashback, only 6 describe unauthorised access.
- Added an NPCI market anchor (about 758 live UPI entries) to the financial section; the model inputs remain unvalidated assumptions.
- Added peer comparison, app-review results, discussion, limitations and two slides; rebuilt the paper (25 pages) and deck (18 slides).
- Built the final folder in the friend's layout, with an `analysis.ipynb` and `fetch_data.py`. A live Jupyter kernel failed in the tool environment, so notebook outputs were stored by running each script directly. The weighted results and model reproduce the originals byte for byte.

## 7. Honest caveats given to the user
- Review coding was done by one coder (the assistant) with no second rater; the group should audit it.
- Still no interviews or surveys of the group's own.
- Scraping Google Play may conflict with its terms of service.
- Python packages were installed on the user's machine with `pip --user`.
- The financial model is illustrative; the NPCI count comes from a search snippet with no stated date.

## Open at the end of the session
- Final read of the PDF and slides by the group.
- Audit of `results/review_fraud_manual_codes.csv`.
- Optional cleanup of old drafts in `Group_31/` (the user decides).

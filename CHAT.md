# Chat log: how the Group 31 term paper was finished

A chronological summary of the working sessions (not verbatim). Sections 1–7 cover the first session; sections 8–17 cover the later passes. For the project state see `CONTEXT.md`.

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

## 8. Verification pass (second session)
- Re-ran the analysis scripts and checked the paper against the result files: tables against `results/`, table and figure numbering, Times New Roman 12, caption placement, abstract length (150–200 words) and at least 30 references. Corrections: a wrong Discussion claim about older adults' digital use, and a slide that listed five research questions instead of six.

## 9. Names and the first plan
- The user asked to use "Sudhanshu" only (not "Sah") and to turn three pending human steps (real interviews, a human second coder, a final read) into a plan. A corrected progress report was saved beside the original, which was left untouched.
- Interviews were not feasible, so the group chose secondary evidence instead, and the user said not to worry about app-store terms of service because the work is being published. Reddit was blocked and was **not** bypassed.

## 10. Secondary qualitative evidence
- Scraped public Apple App Store (India) reviews of the five payment apps (2,090) and later of six bank apps (1,961 on App Store; 4,279 on Google Play).
- Synthesised five published interview and focus-group studies into eight themes S1–S8 (Table 20; counts are of studies, not respondents).
- Blind second passes were run by fresh subagents who did not see the first labels: Play 118 reviews (94.9%, kappa 0.93), App Store 57 (82.5%, 0.78), bank apps 65 (87.7%, 0.84).

## 11. Weaknesses fixed
- The user pasted a list of weak points and small things; the assistant fixed them: a design-effect sensitivity check, stale single-coder statements in the deck, notebook and README, and a UPI market anchor sourced from the PIB factsheet (741 live banks, July 2026).
- The user approved the first push ("Push anyway"). The repository is public and already held the microdata and an earlier answer key; the user chose to continue.

## 12. Human second coder
- The user asked what a second coder is and what to check in Table 17, then returned results for a human, blind coder on 40 Play reviews: 38/40 = 95.0%, kappa 0.93, and 0 of 60 non-fraud reviews missed. The paper reports this on the user's word; the coder's identity is not recorded in the repository, so the group should be ready to back it up.

## 13. Student IDs, summary table and IEEE report
- Added IDs (Rushal IIT2024045, Sudhanshu IIT2024081, Vichanshu IIT2024083), a research-question summary table and a two-page IEEE-style report. A remote commit with an identical tree forced a `git rebase origin/main`; there was no force push.

## 14. Topic correction
- The user said the actual topic is **"Mobile banking: financial inclusion vs cybersecurity risks"**. The title, framing, analysis, data and scraping were realigned (plan in `Completion_Pack/TOPIC_ALIGNMENT_PLAN.md`): a new inclusion-versus-risk table and figure by 18 groups (Spearman 0.38 and 0.63), and bank-app reviews added next to payment-app reviews.

## 15. Audit and the last additions
- The user asked what was left, then asked for a proper audit. All eight analysis scripts reproduced identical results in a clean copy and the notebook ran end to end.
- Added significance tests (RQ3 Fisher p = 0.11; bank versus payment themes with Holm correction), a Hindi/Hinglish sensitivity check (41 extra reviews; unauthorised-type reports in Play payment apps 6 → 12 of 5,758), Appendix A with the coding scheme, and the human-check packs. 153 automated checks pass.
- Pushed as commit 51f78b6. The new second-coder answer key lives in a git-ignored private folder and was not uploaded.

## 16. Style and process notes from the user
- The user did not want to be asked about the deadline; it was dropped.
- Every push was approved explicitly. No force pushes. Access blocks (Reddit) were not bypassed.

## 17. This request
- The user asked for a context file and a chat file in Markdown and to push everything. `CONTEXT.md` and `CHAT.md` were brought up to date and pushed.

## Open at the end of the session
- A person re-codes the 122 reviews in `Completion_Pack/second_coder_round2/` (about 1 hour); then run `compute_agreement_round2.py` and update the paper with the numbers.
- A person fills `Completion_Pack/table20_check/TABLE20_CHECK_SHEET.csv` (30–45 minutes); corrections go into the paper, slides and result files.
- Final read in Word and PowerPoint, then export the PDFs from Word in place of the LibreOffice versions.
- Optional: the group's own interviews (`Completion_Pack/interviews/`).


## 18. Shorter paper, new deck, final folder (ninth pass)
- The user asked to cut the paper to 10 to 12 pages and rebuild the PPT. The assistant wrote a condensed builder, trimmed the prose, dropped six references (keeping 31 academic sources) and used 0.9 in top and bottom margins to land on exactly 12 pages in Word; checks: every reference cited, table captions above and figure captions below, Times New Roman 12. A new 18-slide deck was built with native charts and speaker notes and checked slide by slide.
- The user pasted the round-2 second coder's results (83.6% agreement with the first pass, kappa 0.80). The assistant re-ran the agreement script to verify them and added them to the paper. Asked who coded, the user said it was done by a person using software; the paper says "a person assisted by coding software, as reported by the group".
- The user then said to remove the extended paper and use only the 12-page one. The final folder now holds only the 12-page paper and the 18-slide deck (extended paper, IEEE report and their builders removed from the folder; originals remain elsewhere in the repo and in git history), plus a refreshed README and notebook.

## 19. Friend comparison and additions (tenth pass)
- The assistant compared `Friend/` with the final folder and listed what to add; the user said "do the things". Done: entrepreneurial-finance literature (five verified sources) and framing, JEL codes, Data availability, a research-question answers table and a review-category figure, all within 12 pages in Word.
- The user also supplied `Group_31_Dataset_Key_Findings.pdf` and asked for its graphs to be in the PPT. Two were missing (access vs use; device lock by group) and were added as native charts; the deck now has 19 slides.

## 20. Slide 6 removed (for now)
- The user asked to remove the coding-reliability slide. The deck has 18 slides; the guide was renumbered (Part 1 slides 1 to 5, Part 2 slides 6 to 11, Part 3 slides 12 to 18) and the slide's script moved to a backup section.

# -*- coding: utf-8 -*-
c = open('CONTEXT.md', encoding='utf-8').read()
i = c.index("## 7j. Condensed submission")
new = r'''## 7j. Condensed submission, 20 Nov 2026 (ninth pass) - CURRENT STATE
- **Decision by the user:** only the 12-page paper is used. The earlier ~39-page paper, the 2-page IEEE report and the old 21-slide deck are **no longer part of `Group_31_Final_Submission/`** (they remain in git history and in `Group_31/revised/`, `Group_31/report/` and `Group_31/slides/`; nothing was deleted there).
- **Submission folder now:** `Research_Report.pdf` and `report/Group_31_Research_Paper.(docx|pdf)` = the **12-page paper** (Word export; 6 tables, 1 figure, 44 references of which 31 are academic; top and bottom margins 0.9 in); `slides/Group_31_Presentation_Final.(pptx|pdf)` = **18 slides** with native charts and speaker notes; `analysis.ipynb`, `fetch_data.py`, `data/`, `figures/`, `results/`, `scripts/`, `README.txt`.
- **Builders:** `Condensed/build_short_paper.py` (reads reference entries from `Condensed/references_source.txt`, cites with the old reference numbers and renumbers by first appearance) and `Condensed/build_short_deck.py`; copies in `Group_31_Final_Submission/scripts/condensed/`. Run from the project root (`Desktop/EF`), then export the DOCX to PDF with Word.
- **What the 12-page paper left out compared with the old full paper:** the full 18-group table, the data-sources table, theme-share tables, the published-studies table, the RQ-answers table, the business-model canvas table, the peer figure, appendices, six references (Lusardi and Mitchell, Robinson et al., Venkatesh et al., Kashyap and Wetherilt, Findex 2014, the World Bank blog and the PIB UPI factsheet) and the UPI market-anchor sentence (741 banks).
- **Second coder on the 122 App Store and bank-app reviews:** per the user, **a person who used coding software**, blind to the first-pass labels and the key. Agreement with the first pass 102/122 = 83.6% (kappa 0.80; App Store 80.7%, 0.76; bank apps 86.2%, 0.81); with the AI second pass 104/122 = 85.2% (0.82). Verified by re-running `compute_agreement_round2.py`. The coder labelled 8 of 122 as unauthorised access or theft (first pass 5, AI second pass 8); 10 of the 20 disagreements were first-pass "general accusation" reviews. The paper says "a person assisted by coding software, as reported by the group"; "using software" is ambiguous (it could include an AI tool), so keep that wording unless the group can say more. Filled sheet: `Completion_Pack/second_coder_round2/PartC_coding_sheet_filled.csv`; output: `results/second_coder_round2_agreement.txt` (also a notebook cell).
- **Open items now:** (1) final read of the 12-page paper and 18 slides in Word and PowerPoint; (2) the group should be able to explain the coding method and the two second-coder checks if asked; (3) optional: commit and push.
'''
c = c[:i] + new
open('CONTEXT.md', 'w', encoding='utf-8').write(c)
h = open('CHAT.md', encoding='utf-8').read()
i = h.index("## 18. Shorter paper and new deck")
h = h[:i] + '''## 18. Shorter paper, new deck, final folder (ninth pass)
- The user asked to cut the paper to 10 to 12 pages and rebuild the PPT. The assistant wrote a condensed builder, trimmed the prose, dropped six references (keeping 31 academic sources) and used 0.9 in top and bottom margins to land on exactly 12 pages in Word; checks: every reference cited, table captions above and figure captions below, Times New Roman 12. A new 18-slide deck was built with native charts and speaker notes and checked slide by slide.
- The user pasted the round-2 second coder's results (83.6% agreement with the first pass, kappa 0.80). The assistant re-ran the agreement script to verify them and added them to the paper. Asked who coded, the user said it was done by a person using software; the paper says "a person assisted by coding software, as reported by the group".
- The user then said to remove the extended paper and use only the 12-page one. The final folder now holds only the 12-page paper and the 18-slide deck (extended paper, IEEE report and their builders removed from the folder; originals remain elsewhere in the repo and in git history), plus a refreshed README and notebook.
'''
open('CHAT.md', 'w', encoding='utf-8').write(h)
print('updated')

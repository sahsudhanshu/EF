# -*- coding: utf-8 -*-
"""Make the paper follow the TA's 'Paper structure.pdf' exactly (headings, intro elements, justification per method, no extra content in Conclusion)."""
p = 'Condensed/build_short_paper.py'
s = open(p, encoding='utf-8').read()


def rep(a, b):
    global s
    assert s.count(a) == 1, (a[:70], s.count(a))
    s = s.replace(a, b)


# ---- title: scope in the main title
rep("add_runs(tp, 'Mobile Banking: Financial Inclusion vs Cybersecurity Risks', bold=True)", "add_runs(tp, 'Mobile Banking: Financial Inclusion vs Cybersecurity Risks in India', bold=True)")

# ---- introduction: the four elements as 1.1 to 1.4
i = s.index("H1('1. Introduction')\n") + len("H1('1. Introduction')\n")
j = s.index('P("**Research questions.**')
old = s[i:j]
# paragraph 1 stays as background; split the 'Problem and gap' paragraph
k = old.index('P("**Problem and gap.**')
p1 = old[:k]
p2 = old[k:]
gap_start = p2.index('  "The literature is strong on')
problem = p2[:gap_start]
gap = p2[gap_start:]
problem = problem.replace('P("**Problem and gap.** Mobile banking', 'P("Mobile banking').rstrip()
assert problem.endswith('{12,13}. "')
problem = problem[:-1] + ' "\n  "This matters because trust and safety shape whether new users keep using digital channels {12,13}, and because institutions and entrepreneurs that serve them need to know where safeguards are weakest.")\n'
gap = 'P("The literature is strong' + gap[len('  "The literature is strong'):]
gap = gap.replace("We ask where inclusion and cybersecurity risk move together, where they do not, and what institutions and entrepreneurs could do.", "This study addresses that gap with the Global Findex India survey, public app reviews and published interview studies, and a transparent, assumption-labelled venture model.")
new = ("H2('1.1 Background')\n" + p1 + "H2('1.2 Problem and importance')\n" + problem + "H2('1.3 Research gap')\n" + gap + "H2('1.4 Research questions')\n")
s = s[:i] + new + s[j:]
rep('P("**Research questions.** RQ1:', 'P("We ask where inclusion and cybersecurity risk move together, where they do not, and what institutions and entrepreneurs could do. The six questions are: RQ1:')

# ---- methodology headings (TA wording) and justification for each method
for a, b in [("H2('3.1 Research design')", "H2('3.1 Research Design')"), ("H2('3.2 Sampling method and participants')", "H2('3.2 Sampling Method and Participants')"),
             ("H2('3.3 Data collection methods')", "H2('3.3 Data Collection Methods')"), ("H2('3.4 Materials and instruments')", "H2('3.4 Materials and Instruments')"),
             ("H2('3.5 Data analysis')", "H2('3.5 Data Analysis')"), ("H2('3.6 Ethical considerations')", "H2('3.6 Ethical Considerations')")]:
    rep(a, b)
# 3.4: justification + data availability moved here from the Conclusion
rep("con21 (unsolicited request; 2,145 phone owners) and con22 (sent money; 219 recipients).\")",
    "con21 (unsolicited request; 2,145 phone owners) and con22 (sent money; 219 recipients). \"\n  \"**Justification:** open tools keep every step reproducible, and the stored keyword dictionaries and coding scheme make the review coding auditable.\")\n"
    "P(\"**Data availability.** The India household microdata are available from the World Bank microdata library {37} under its access terms and are not redistributed here. Country indicators come from the World Bank open data API {38}. The app-review snapshots, scripts, results tables and notebook are in the submission folder (data/, scripts/, results/, analysis.ipynb).\")")
# remove the Data availability paragraph from the Conclusion section
i = s.index('P("**Data availability.** The India household microdata are available from the World Bank microdata library {37} under its access terms and are not redistributed here. Country indicators come from the World Bank open data API {38}. The app-review snapshots, scripts, results tables and notebook are in the submission folder (data/, scripts/, results/, analysis.ipynb).")', s.index("H1('6. Conclusion')"))
j = s.index('\n', i) + 1
s = s[:i] + s[j:]
# 3.5 justification (after the financial-model paragraph, before 3.6)
rep("H2('3.6 Ethical Considerations')", 'P("**Justification:** weighting is needed for population statements; the logistic model separates payment use from demographic differences; group comparisons and rank correlations answer the inclusion-versus-risk question without overclaiming; Fisher and chi-square tests suit small counts; two-step coding with second coders makes free text measurable and checks reliability; and scenario and sensitivity analysis shows which assumptions drive viability without false precision.")\nH2(\'3.6 Ethical Considerations\')')
# 3.6 justification
rep("Future interviews or pilots would need informed consent and would not collect credentials.\")", "Future interviews or pilots would need informed consent and would not collect credentials. **Justification:** public, de-identified data and no stored names let us study a sensitive topic without exposing individuals, and labelling exposure as reports and finance as illustrative keeps claims within the evidence.\")")
open(p, 'w', encoding='utf-8').write(s)
print('structure patched')

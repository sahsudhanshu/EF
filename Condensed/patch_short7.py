# -*- coding: utf-8 -*-
p = 'Condensed/build_short_paper.py'
s = open(p, encoding='utf-8').read()


def between(a, b, new):
    global s
    i = s.index(a) + len(a); j = s.index(b, i)
    s = s[:i] + new + s[j:]


def rep(a, b):
    global s
    assert s.count(a) == 1, (a[:70], s.count(a))
    s = s.replace(a, b)


# ---- intro (first two paragraphs only; RQ paragraph is kept)
between("H1('1. Introduction')\n", 'P("**Research questions.**', '''P("Access to formal finance is linked with household resilience, enterprise formation and poverty reduction {1,2}, and mobile phones and digital payments have changed how it is delivered {3,4}, in India with public digital identity and payment infrastructure {5,6}. "
  "For a small merchant, a first-time business owner or any digital customer, an account helps only if it can be used reliably and without undue risk. Financial inclusion here means use of formal financial services: account ownership measures access, digital payment use measures activity. Reported cybersecurity exposure means a report of an unsolicited call or message asking for money, a sign of a possible scam attempt and not verified fraud. The World Bank's Global Findex is the main cross-country source for the first two measures {7,8,9}.")
P("**Problem and gap.** Mobile banking can bring people into the formal system, but each new user is also a possible target and may lack the safeguards of experienced users; deception exploits ordinary behaviour {10,11}, and trust shapes adoption {12,13}. "
  "The literature is strong on mobile-money benefits and on phishing, but rarely joins them in a recent national survey of India, and little work turns such patterns into an entrepreneurial question: what service could be built, who would pay, and what would make it viable. We ask where inclusion and cybersecurity risk move together, where they do not, and what institutions and entrepreneurs could do.")
''')

# ---- 2.1
between("H2('2.1 Inclusion, mobile money and development')\n", "H2('2.2 Entrepreneurial finance, adoption, trust and fintech')", '''P("Deeper finance disproportionately raises the incomes of the poorest {14}, and account access supports inclusive growth depending on how accounts are used {1}. Measurement advanced with the Global Findex {7} and its rounds {8,9}, which separated ownership from usage. "
  "The best causal evidence is from Kenya: M-PESA helped households share risk {18} and lifted around 2% of households out of poverty, more in female-headed households {2}. Mobile transfers improved diets in Niger {19}, debit cards raised savings in Mexico {20}, diffusion varies by institutional context {21}, and digital inclusion is linked with growth {22}. "
  "In India, biometric payments reduced leakage {5} and demonetisation was used to study digital payments {6}; gains are not automatic, as microcredit raised business investment but not average consumption {23}. Benefits arise when services are used, so this study measures use, not ownership alone.")
''')

# ---- 3.1 / 3.2 / 3.6
between("H2('3.1 Research design')\n", "H2('3.2 Sampling method and participants')", '''P("The design is cross-sectional, observational and descriptive-analytical: weighted descriptives and group comparisons (RQ1, RQ4); a weighted logistic model (RQ2) and lock-status comparison (RQ3); a peer comparison; qualitative analysis of documents, app reviews and published interview studies (RQ5); and a deterministic financial model (RQ6). "
  "**Justification:** a population survey is the only source recording adoption and exposure for the same adults; interviews of our own were not feasible, so published studies serve as secondary evidence; and scenario modelling is the standard test of a venture before commercial data exist.")
''')
between("H2('3.2 Sampling method and participants')\n", "H2('3.3 Data collection methods')", '''P("We use the India file of the Global Findex Database 2025 (survey year 2024, IND_2024_FINDEX_v02_M) {37}: 3,000 respondents aged 15 or older, a nationally representative adult sample drawn by the World Bank and Gallup. All percentages use the survey weight (wgt); n and counts are unweighted. The data describe individuals, not businesses. **Justification:** it is the standard public inclusion benchmark and the only source linking payments to phone-safety items in India.")
''')
between("H2('3.6 Ethical considerations')\n", "# ============================================================ 4 RESULTS", '''P("De-identified public microdata are used under the World Bank's access terms and not redistributed; reviews are public with no usernames stored; published studies are summarised, not reproduced. Exposure is reported as reports, not verified fraud, and commercial figures are illustrative with no partner, investor or willingness to pay claimed. Future interviews or pilots would need informed consent and would not collect credentials.")

''')

# ---- 4.7 text and drop the finance figure
between("H2('4.7 Illustrative financial model outputs')\n", "figure('fin',", '''P("Contribution per institution is INR 40,000 a month (80%) and simple acquisition payback is 5 months. Steady-state break-even is 8 paying institutions, or 13 when one new institution is acquired each month. The base case records a deficit of INR 32.80 lakh in Year 1, zero in Year 2 and a surplus of INR 52.16 lakh in Year 3; the conservative case is in deficit throughout (INR 36.80, 30.00 and 17.44 lakh) and the optimistic case reaches INR 48.80 and 173.16 lakh in Years 2 and 3 (Figure 3). "
  "Cutting the fee to INR 40,000 raises break-even to 10 institutions, raising variable cost to INR 15,000 raises it to 9, and an acquisition cost of INR 3 lakh extends payback to 7.5 months; across all fee and cost combinations tested the requirement is 6 to 12.")
''')
rep("figure('fin', 'figure4.png', \"Illustrative annual operating surplus or deficit by scenario (INR lakh; assumptions, not findings; no churn, tax or financing flows).\", 4.6)", "figure('fin', 'figure4.png', \"Illustrative annual operating surplus or deficit by scenario (INR lakh; assumptions, not findings; no churn, tax or financing flows).\", 3.9)")

# ---- discussion first paragraph
between("**Inclusion versus cybersecurity risk.**", 'P("**Reviews, studies and documents.**', ''' Payment users reported more unsolicited requests than non-users and the association survived adjustment, so inclusion in digital payments goes with greater reachability by scammers, plausibly because digital users are reachable through more channels {30}. "
  "Across groups the link was weak to moderate (rank correlation 0.38): exposure was highest among the most included (tertiary-educated) but also in the lowest income quintile, and lowest among older adults and women. Protection rose with inclusion (0.63) except among older adults, whose payment use far exceeds lock use. "
  "Risk therefore concentrates where inclusion outruns safeguards and where people have little margin for loss. A lock limits access to a handset, not deception {10,11,28}; the RQ3 comparison rests on 45 senders and is not significant.")
''')

# ---- table 1: fewer rows
rep("    ['Account ownership, all adults', '2,710 / 3,000', '89.0%'],\n", "")
rep("    ['Phone ownership, all adults', '2,145 / 3,000', '66.5%'],\n", "")
rep("    ['Digital payment, all adults', '1,539 / 3,000', '48.5%'],", "    ['Account ownership | digital payment, all adults', '2,710 | 1,539 / 3,000', '89.0% | 48.5%'],")
# ---- figure widths
rep("each point is a group). Source: authors' calculations from {37}.\", 3.1)", "each point is a group). Source: authors' calculations from {37}.\", 2.9)")
rep("second-pass agreement is in Section 3.5.\", 5.6)", "second-pass agreement is in Section 3.5.\", 5.1)")
open(p, 'w', encoding='utf-8').write(s)
print('patched7')

# -*- coding: utf-8 -*-
p = 'Condensed/build_short_paper.py'
s = open(p, encoding='utf-8').read()


def rep(a, b):
    global s
    assert s.count(a) == 1, (a[:70], s.count(a))
    s = s.replace(a, b)


def before(marker, text):
    global s
    assert s.count(marker) == 1, (marker[:50], s.count(marker))
    s = s.replace(marker, text + marker)


# 4.1
rep("and 21.0% of the 219 recipients reported sending money (Table 1).", "and 21.0% of the 219 recipients reported sending money (Table 1; Figures 1 and 2).")
before("H2('4.2 Adjusted association and lock status')",
       "figure('acc', 'pfig_access_gender.png', \"Account ownership, phone ownership and digital payment use among all adults, and digital payment use and phone lock by gender (survey-weighted). Source: authors' calculations from {37}.\", 6.2)\n"
       "figure('lock', 'pfig_lock_groups.png', \"Device-lock use among phone owners by group (survey-weighted; teal and amber bars show the two highest and lowest groups). Source: authors' calculations from {37}.\", 6.0)\n")
# 4.2
rep("the Fisher exact test gave p = 0.11.", "the Fisher exact test gave p = 0.11 (Figure 3).")
before("H2('4.3 Inclusion, exposure and protection by group')",
       "figure('exp', 'pfig_exposure.png', \"Reported unsolicited money requests by digital payment use, and sending money after a request by lock status (survey-weighted percentages; counts are unweighted). Source: authors' calculations from {37}.\", 6.2)\n")
# 4.3
rep("(Figure 1). \"", "(Figure 4). \"")
rep("Payment use exceeded lock use most at ages 60 and above (56.6% against 22.9%; +33.7 points) and fell short of it most at ages 15 to 24 (43.5% against 75.7%; −32.1).", "Payment use exceeded lock use most at ages 60 and above (56.6% against 22.9%; +33.7 points) and fell short of it most at ages 15 to 24 (43.5% against 75.7%; −32.1; Figure 5).")
before("H2('4.4 Peer economies')",
       "figure('gap', 'pfig_gap_groups.png', \"Digital payment use (all adults) beside phone-lock use (phone owners) by group. Source: authors' calculations from {37}; the two shares have different denominators.\", 6.2)\n")
# 4.4
rep("Among the seven economies in Table 3,", "Among the seven economies in Table 3 and Figure 6,")
before("H2('4.5 Public app reviews')",
       "figure('peers', 'figure5.png', \"India and peer economies on account ownership, phone ownership, phone lock and unsolicited requests (2024). Source: {38}; India's request share from authors' calculations.\", 4.6)\n")
# 4.5
rep("poor grievance handling (Figure 2). \"", "poor grievance handling (Figure 7). \"")
# 4.6
rep("and of 91 victims who reported fraud, 59 could not recover their money {53}.", "and of 91 victims who reported fraud, 59 could not recover their money {53} (Figure 8).")
before("H2('4.7 Illustrative financial model outputs')",
       "figure('stud', 'pfig_studies.png', \"Themes reported by the five published interview studies (counts are of studies, not respondents). Source: authors' coding of {49,50,51,52,53}.\", 5.8)\n")
# 4.7
rep("the requirement is 6 to 12.", "the requirement is 6 to 12 (Figure 9).")
before("# ============================================================ 5 DISCUSSION",
       "figure('fin', 'pfig_finance.png', \"Illustrative annual operating surplus or deficit by scenario (INR lakh; assumptions, not findings; no churn, tax or financing flows). Source: authors' calculations.\", 5.8)\n\n")
open(p, 'w', encoding='utf-8').write(s)
print('figures patched')

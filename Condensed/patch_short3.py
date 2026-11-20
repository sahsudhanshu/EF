# -*- coding: utf-8 -*-
p = 'Condensed/build_short_paper.py'
s = open(p, encoding='utf-8').read()


def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:70], s.count(a))
    s = s.replace(a, b)


# ---- drop six reference-heavy items (keep >= 30 academic sources in the review)
rep("and its rounds {8,9,15}, which", "and its rounds {8,9}, which")
rep(", and financial illiteracy is widespread {17}.", ".")
rep(", and digital credit carries promise and risk {24}.", ".")
rep("Adoption depends on perceived usefulness and ease of use {25}, plus social influence and facilitating conditions {26}; for", "Adoption depends on perceived usefulness and ease of use {25}; for")
rep("and cyber risk is a market failure that regulators address through principles {35,36}.", "and cyber risk is a market failure and source of instability {35}.")
rep("credential hygiene {35,36}", "credential hygiene {35}")
rep("technology-acceptance models {12,25,26}", "technology-acceptance models {12,25}")
rep(" Published Findex 2025 aggregates were 79% of adults with an account worldwide, 75% in low- and middle-income economies, and 61% making or receiving a digital payment in those economies {45}.", "")
rep("Against peers and published aggregates {45}, India", "Against peers, India")
rep(" \"\n  \"Year 3 closing counts of 18, 40 and 65 institutions equal 2.4%, 5.4% and 8.8% of the 741 banks live on UPI in July 2026 {46}.\")", "\")")
rep("A UPI factsheet {46} and World Bank aggregates {45} gave context. ", "") if "A UPI factsheet {46}" in s else None

# ---- new second-coder results
rep("App Store and bank-app coding has no human check. ", "A further second coder, who coded all 122 App Store and bank-app fraud-keyword reviews without seeing the first-pass labels, agreed with the first pass on 102 (83.6%, kappa 0.80; App Store 80.7%, 0.76; bank apps 86.2%, 0.81) and with the AI second pass on 104 (85.2%, 0.82). ")
rep("A Hindi and Hinglish dictionary extension flagged", "That second coder labelled 8 of the 122 App Store and bank-app reviews as unauthorised access or theft, against 5 in the first pass and 8 in the AI second pass (about 0.1% of the 8,330 reviews); 10 of the 20 disagreements with the first pass were reviews it had labelled general accusations. A Hindi and Hinglish dictionary extension flagged")
rep("(a human check on 40 Google Play reviews only)", "(second-coder checks on 40 Google Play and 122 App Store and bank-app reviews)")

# ---- trims
rep("In India, biometric payments reduced leakage {5} and demonetisation was used to study digital payments {6}. Gains are not automatic: microcredit raised business investment but not average consumption {23}. ", "In India, biometric payments reduced leakage {5} and demonetisation was used to study digital payments {6}; gains are not automatic, as microcredit raised business investment but not average consumption {23}. ") if "Gains are not automatic: microcredit raised business investment but not average consumption {23}. " in s else None
rep(" Existing alternatives (RBI and bank campaigns {42}, in-app warnings, the national helpline, in-house builds) already cover parts of the problem, so the service must add measurable value through local-language journeys with comprehension checks, practice outside the transaction flow and faster routes to verified support. ", " Campaigns {42}, in-app warnings, the national helpline and in-house builds already cover parts of the problem, so the service must add measurable value through local-language journeys with comprehension checks and faster routes to verified support. ")
rep("Revenue is not cash, since procurement delays can create a gap. ", "")
rep("Main risks are weak willingness to pay, support cost above the margin, incorrect advice or compromised links, exclusion or payment friction, and dependence on one partner; each needs evidence from a paid pilot. These conclusions", "Main risks are weak willingness to pay, support cost above the margin, incorrect advice and dependence on one partner. These conclusions")
rep(" The findings do not support differential pricing or profiling of groups.", "")
rep("It clarifies that the make-or-receive payment indicator differs from the dashboard's made-payment indicator, shows how to label intervals when design variables are missing, and suggests", "It shows how to label intervals when design variables are missing and suggests")
rep("Bank and payment apps were compared by chi-square tests with Holm adjustment. ", "Bank and payment apps were compared by chi-square tests (Holm adjustment). ")
rep(" The studies (26 to 3,784 participants) were found by targeted search on 20 November 2026 as India-specific, open-access work on fraud, trust or support in digital payments; they are not a systematic review.", " The five studies (26 to 3,784 participants) were found by targeted search on 20 November 2026 and are not a systematic review.")
rep("Variables: account, anydigpayment (made or received a digital payment in the past year), con1 (phone), con18 (PIN, password or fingerprint lock; 2,141 valid), con21 (unsolicited money request in 12 months; 2,145 phone owners) and con22 (sent money; 219 recipients).", "Variables: account, anydigpayment (made or received a digital payment in the past year), con1 (phone), con18 (lock; 2,141 valid), con21 (unsolicited request; 2,145 phone owners) and con22 (sent money; 219 recipients).")
open(p, 'w', encoding='utf-8').write(s)
print('patched3')

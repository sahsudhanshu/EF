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


# drop group table (numbers stay in the text and Figure 1)
i = s.index("table('grp',"); j = s.index("figure('inc',")
s = s[:i] + s[j:]
rep("(Table 3, Figure 1). \"", "(Figure 1). \"")
rep("Among the seven economies in Table 4,", "Among the seven economies in Table 3,")

between("H2('4.5 Public app reviews')\n", "figure('cat',", '''P("The datasets hold 5,758 Google Play and 2,090 App Store reviews of five payment apps and 6,240 reviews of eight bank apps (mean ratings 2.90, 3.31 and 2.49). Fraud-keyword reviews were 2.0%, 2.7% and 1.0% of reviews (mean ratings 1.36, 1.51 and 1.22); support, account-blocking and safety-language themes were each 3% to 8% of reviews in every dataset, and failed payments 0.4% to 2.3%. "
  "After every fraud-keyword review was read, 50.8% of Google Play payment-app reviews concerned rewards or cashback not honoured, against 29.8% on the App Store and 4.6% for bank apps, while 38.5% of bank-app reviews concerned blocked accounts, mis-selling, charges or poor grievance handling (Figure 2). "
  "Reviews of unauthorised access or theft numbered 6 (0.1%), 2 (0.1%) and 3 (below 0.1%). Security-friction prompts matched 2.4% of bank-app reviews (mean rating 1.59) and 3.9% of payment-app reviews (2.09); 104 Google Play payment-app reviews (1.8%) described device-lock prompts, mostly for BHIM. "
  "Bank and payment apps differed after Holm adjustment (p < 0.001) for fraud keywords, failed payments, safety language and security friction, but not for support (p = 0.87) or account blocking (p = 0.12). "
  "The second coder labelled 8 of the 122 App Store and bank-app reviews as unauthorised access or theft (first pass 5, AI second pass 8; about 0.1% of 8,330 reviews), and 10 of the 20 disagreements with the first pass were reviews it had labelled general accusations. A Hindi and Hinglish extension (41 more reviews) would raise unauthorised or unexplained-debit reports on Google Play from 6 to 12 (0.2%).")
''')

between("H2('4.6 Institutional documents and published studies')\n", "H2('4.7 Illustrative financial model outputs')", '''P("The documents yield three themes: trust linked with risk awareness and timely dispute resolution {40}; consumer protection alongside financial capability {41}; and RBI calls for awareness campaigns and protection of credentials such as OTPs and PINs {42}. "
  "Of eight themes in the five published studies, social engineering, trust in the counterparty or bank, and low awareness appeared in all five; weak support or redress and reliance on family or informal channels in four; differences by gender, age or vulnerability in three; and protective advice and design cues and merchant harms in two each. Examples: 45 of 46 participants said trust in the receiver matters {50}; 12 of 24 merchants reported fake payment confirmations {51}; and of 91 victims who reported fraud, 59 could not recover their money {53}.")
''')

between("H2('5.1 Academic implications')\n", "H2('5.2 Policy implications')", '''P("The study joins the economics of inclusion {1,2,18} with the behavioural study of scams {10,11,31} and with entrepreneurial finance {55,57}, pairing national statistics with safety indicators and user-generated text to show where access and safe use diverge. It shows how to label intervals when design variables are missing and suggests that technology-acceptance models {12,25} include perceived safety and device safeguards.")
''')
between("H2('5.2 Policy implications')\n", "H2('5.3 Managerial implications')", '''P("Each implication is a hypothesis to test. Inclusion targets should track active and safe use, not only ownership {40,41}. Awareness efforts such as the RBI's {42} should be judged on behaviour change and designed for older, lower-income and women users, since generic campaigns often fail and education persisted in one experiment only with reminders {31,32}. Providers should own warnings, refunds and complaint handling, regulators clear reporting channels, and users credential hygiene {35}; security prompts should be tested so they do not lock out users.")
''')
between('P("**Financial interpretation.**', "H2('5.4 Future scope and limitations')", ''' Eight institutions cover fixed costs only in steady state, and about 13 are needed while growing because acquisition is expensed. A 20% lower fee adds two institutions, and the base case has no cushion in Year 2, so churn or slow sales would produce a deficit; the conservative case does not break even in three years. "
  "An illustrative INR 75 lakh seed (staged equity or grant) would cover the Year 1 deficit (32.80), prelaunch build (10.00) and pilot evaluation (5.00), a working-capital reserve (12.00) and contingency (15.20), but in the conservative case deficits plus prelaunch costs reach INR 81.80 lakh by Year 2 and exceed it. Main risks are weak willingness to pay, support cost above the margin and dependence on one partner; these conclusions follow security-investment economics {33,34} and hold only if prices and costs are validated with real buyers.")
''')
rep('P("**Financial interpretation.**', 'P("**Financial interpretation.**')
between('P("**Limitations.**', 'P("**Future scope.**', ''' The survey is cross-sectional and self-reported; requests are not verified fraud and sending money is not a loss measure. Cells such as the 45 senders are small, intervals are approximate (the tertiary-education result does not survive assumed clustering), and the data describe individuals, not enterprises. "
  "Reviews are self-selected, cover different windows, and were keyword-coded by one coder with AI second passes and second-coder checks on samples; a Hindi and Hinglish extension changed no conclusion. We conducted no interviews or surveys of our own, and the five published studies were selected by us and are small. Peer values are aggregates without sampling errors, and all financial inputs are unvalidated assumptions without churn, tax or financing flows.")
''')
open(p, 'w', encoding='utf-8').write(s)
print('patched5')

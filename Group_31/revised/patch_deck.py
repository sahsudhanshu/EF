# -*- coding: utf-8 -*-
p = 'Group_31/revised/build_structured_deck.py'
s = open(p, encoding='utf-8').read()


def rep(a, b):
    global s
    assert s.count(a) == 1, (a[:70], s.count(a))
    s = s.replace(a, b)


rep("# 9b -------------------------------------------------------------- qualitative", """# 9a -------------------------------------------------------------- peers
s = slide('4.7  Results: peer economies', 'India: top-tier accounts, below-peer phone ownership',
          'World Bank Findex 2025 aggregates for 2024. India account 89.0 (second to China 89.4), phone 66.5 (second lowest), lock 57.6, unsolicited requests 9.4 (our microdata; lowest among economies with a value). Indicative only.')
s.shapes.add_picture(str(FIG / 'figure5.png'), Inches(0.6), Inches(1.65), height=Inches(4.95))
bullets(s, 7.9, 1.8, 4.8, 4.6, ['Accounts|India 89.0%, second to China (89.4%); world 78.7%.',
        'Phones|India 66.5%, above only Pakistan (62.9%).',
        'Locks|India 57.6%; peers range 46.4% to 78.0%.',
        'Requests|India 9.4% (our microdata); peers 12.7% to 32.4%.'], 15)
source(s, 'Published aggregates, no sampling errors; India request share from authors\\' microdata. Source: World Bank Global Findex 2025 API.')

# 9b -------------------------------------------------------------- qualitative""")

rep("# 10 --------------------------------------------------------------- discussion", """# 9c -------------------------------------------------------------- reviews
s = slide('4.9  Results: app reviews', '5,758 app reviews: grievances are rewards, refunds and support',
          'Five apps, India Play Store, 2 Oct to 19 Nov 2026. 118 fraud-keyword reviews all read and coded: 60 reward deception, 15 failed payments, 11 blocked/support, 10 spam/privacy, 9 general, 7 praise, 6 unauthorised access. 104 reviews mention device-lock prompts.')
stat(s, 0.6, 1.75, 2.9, '5,758', 'reviews, five payment apps (BHIM, SBI YONO, PhonePe, Paytm, Google Pay)')
stat(s, 3.7, 1.75, 2.9, '50.8%', 'of the 118 fraud-keyword reviews are about unpaid cashback or rewards', BLUE)
stat(s, 6.8, 1.75, 2.9, '6 of 5,758', 'describe unauthorised access or theft (0.1%)', AMBER)
stat(s, 9.9, 1.75, 2.8, '104', 'reviews describe device-lock or security-alert prompts', NAVY)
s.shapes.add_picture(str(FIG / 'figure6.png'), Inches(0.6), Inches(3.6), height=Inches(2.9))
bullets(s, 8.6, 3.7, 4.2, 2.9, ['Ratings|fraud-keyword reviews average 1.36 stars vs 2.93 for others.',
        'Other themes|support 5.3%, blocking and verification 6.3%, failed payments 2.3%.',
        'Method|keyword coding, then all 118 fraud-keyword reviews read by one coder.'], 13)
source(s, 'Self-selected public reviews; not a measure of scam prevalence. Source: authors\\' coding of Google Play reviews.')

# 10 --------------------------------------------------------------- discussion""")

rep("'Qualitative|focused review of World Bank and RBI documents; no interviews or fieldwork.'",
    "'Qualitative|World Bank and RBI documents plus 5,758 public app reviews, keyword-coded and manually classified; no interviews.'")
rep("'Approximate intervals: design variables missing.'", "'Approximate intervals; app reviews are self-selected and single-coded.'")
rep("'Consent-based interviews with merchants, users and budget owners.'", "'Consent-based interviews with merchants, users and budget owners (none yet).'")
open(p, 'w', encoding='utf-8').write(s)
print('ok')

# -*- coding: utf-8 -*-
p = 'Condensed/build_short_paper.py'
s = open(p, encoding='utf-8').read()


def between(a, b, new):
    global s
    i = s.index(a) + len(a); j = s.index(b, i)
    s = s[:i] + new + s[j:]


between("H2('3.3 Data collection methods')\n", "H2('3.4 Materials and instruments')", '''P("Seven public sources were used: the India Findex microdata {37}; Findex 2025 country indicators for India and nine peers {38}; Google Play reviews of five payment apps (PhonePe, Google Pay, Paytm, BHIM, SBI YONO; 5,758 reviews, 2 Oct to 19 Nov 2026) {39}; App Store reviews of the same apps (2,090; 30 Apr to 18 Nov) {47}; reviews of eight bank apps in both stores (6,240; 5 Jun to 19 Nov) {48}; three institutional documents {40,41,42}; and five published interview studies {49,50,51,52,53} found by targeted search on 20 November 2026 (not a systematic review). "
  "Reviews were collected with google-play-scraper and Apple's public feed; only app, date, rating and text were kept (no names, emails or phone numbers), and reviews under 15 characters and duplicates were removed. We conducted no interviews or surveys of our own. "
  "**Justification:** public data permit reproduction, reviews give unprompted user language, and published studies supply victim and merchant experience that reviews rarely contain.")
''')

between("**Qualitative.**", 'P("**Financial model.**', ''' Document passages on trust, shared responsibility and credential protection were grouped into themes. Reviews were coded in two steps: dictionaries flagged five themes (fraud, failed payment, support, account blocking or verification, safety language) plus security-friction prompts for bank apps, then every fraud-keyword review was read and placed in one of seven categories by one coder. "
  "Blind AI second passes agreed on 112 of 118 Google Play reviews (94.9%, kappa 0.93), 47 of 57 App Store reviews (82.5%, 0.78) and 57 of 65 bank-app reviews (87.7%, 0.84). A human coder outside the group, blind to the labels, re-coded 40 of the 118 Google Play reviews (38 agreed, 95.0%, kappa 0.93). A further second coder (a person assisted by coding software, as reported by the group), who coded all 122 App Store and bank-app fraud-keyword reviews without seeing the first-pass labels, agreed with the first pass on 102 (83.6%, kappa 0.80; App Store 80.7%, 0.76; bank apps 86.2%, 0.81) and with the AI second pass on 104 (85.2%, 0.82). "
  "Bank and payment apps were compared by chi-square tests (Holm adjustment). Published-study findings were mapped to eight themes from the full texts by one coder; counts are of studies, not respondents.")
''')

between("**Reviews, studies and documents.**", "table('rq',", ''' Review complaints concern rewards, refunds, support, blocks and security prompts far more than theft, on both platforms. This does not measure scam prevalence: victims may not write reviews, and the interview studies describe the social engineering, trust and slow redress that reviews rarely capture; support and redress failures appear in both sources, consistent with the documents {40,41,42}. "
  "In bank apps the tension shows up as friction and weak redress more than fraud: SIM binding, biometric and root-detection prompts were a recurring source of one-star reviews. Against peers, India has near-top account ownership but below-peer phone ownership and digital payment use and the lowest reported request share among economies with a value; recall, reporting and phone-based contact may explain this, and the comparison sets a sample estimate against published values without sampling error. "
  "Table 4 summarises the answers to the research questions.")
''')
open(p, 'w', encoding='utf-8').write(s)
print('patched6')

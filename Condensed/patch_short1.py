# -*- coding: utf-8 -*-
p = 'Condensed/build_short_paper.py'
s = open(p, encoding='utf-8').read()


def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:70], s.count(a))
    s = s.replace(a, b)


def cut(start, end, keep_end=True):
    global s
    i = s.index(start); j = s.index(end, i)
    s = s[:i] + (s[j:] if keep_end else s[j + len(end):])


# --- drop tables / figure
cut("table('src',", "H2('3.4 Materials and instruments')")
cut("table('rev',", "table('cat',")
cut("table('stud',", "H2('4.7 Illustrative financial model outputs')")
cut("table('rq',", "H2('5.1 Academic implications')")
cut("table('canvas',", 'P("**Financial interpretation.**')
cut("figure('peerfig',", "H2('4.5 Public app reviews')")

# --- 3.3 text
rep("Six sources were used (Table 1). All are public; we conducted no interviews, focus groups or surveys of our own.",
    "Seven public sources were used: the India Findex microdata {37}; Findex 2025 country indicators for India and nine peers {38}; Google Play reviews of five payment apps (PhonePe, Google Pay, Paytm, BHIM, SBI YONO; 5,758 reviews, 2 October to 19 November 2026) {39}; App Store reviews of the same apps (2,090; 30 April to 18 November) {47}; reviews of eight bank apps in both stores (6,240; 5 June to 19 November) {48}; three institutional documents {40,41,42}; and five published interview studies {49,50,51,52,53}. A UPI factsheet {46} and World Bank aggregates {45} gave context. We conducted no interviews, focus groups or surveys of our own.")

# --- numbering of table / figure mentions in prose
rep("(Table 2). Published Findex 2025 aggregates", "(Table 1). Published Findex 2025 aggregates")
rep("urban residence had intervals including 1.00 (Table 3).", "urban residence had intervals including 1.00 (Table 2).")
rep("(Table 4, Figure 1). \"", "(Table 3, Figure 1). \"")
rep("Among the seven economies in Table 5,", "Among the seven economies in Table 4,")
rep("compared with 12.7% to 32.4% for peers (Figure 2).", "compared with 12.7% to 32.4% for peers.")
rep("had mean ratings of 1.36, 1.51 and 1.22 (Table 6). \"", "had mean ratings of 1.36, 1.51 and 1.22. Failed payments were 2.3%, 1.5% and 0.4% of reviews, support and complaints 5.3%, 6.4% and 5.5%, account blocking or verification 6.3%, 7.8% and 5.9%, and safety and trust language 5.2%, 6.4% and 3.4%. \"")
rep("poor grievance handling (Table 7). \"", "poor grievance handling (Table 5). \"")
rep("merchant harms in two each (Table 8).\")", "merchant harms in two each. Examples: 45 of 46 participants said trust in the receiver matters {50}; 12 of 24 merchants reported fake payment confirmations {51}; and of 91 victims who reported fraud, 59 could not recover their money {53}.\")")
rep("up to 3 (Table 9).", "up to 3 (Table 9).") if False else None
rep("INR 48.80 and 173.16 lakh in Years 2 and 3 (Table 9). \"", "INR 48.80 and 173.16 lakh in Years 2 and 3 (Table 6). \"")
rep(" The answers to all six research questions are summarised in Table 10.\")", "\")")
rep(" Table 11 gives the business model canvas. \"", " In canvas terms, the customer is the institution, the value is understandable guidance and verified routes to support, revenue is a recurring institutional subscription, and the main costs are a small fixed product and quality team, variable delivery cost and customer acquisition. \"")

# --- trim model table
rep("    ['Age per 10 years | income quintile per step', '0.92 | 0.91', '0.82 to 1.04 | 0.79 to 1.03'],\n    ['In workforce | urban residence', '0.89 | 0.91', '0.61 to 1.32 | 0.63 to 1.30'],\n", "")
rep("Secondary versus primary or less', '0.84', '0.56 to 1.25'],", "Secondary versus primary or less', '0.84', '0.56 to 1.25'],")

# --- figure width
rep("each point is a group). Source: authors' calculations from {37}.\", 4.0)", "each point is a group). Source: authors' calculations from {37}.\", 3.5)")

# --- shorter reference text for long entries
rep("order = []  # keys", "order = []  # keys") if False else None
s = s.replace("order = []\n", """order = []
SHORT = {
 38: "World Bank. (2025). Global Findex Database 2025 country indicators (account.t.d, con1, con18.s, con21.s; 2024) [Data set]. World Bank Data API, source 28.",
 39: "Google Play Store. (2026). Public reviews of PhonePe, Google Pay, Paytm, BHIM and SBI YONO, India, 2 Oct to 19 Nov 2026 [Data set collected by the authors; usernames not stored].",
 42: "Reserve Bank of India. (2020, June 22). Increasing instances of payment frauds: Enhancing public awareness campaigns through multiple channels (RBI/2019-20/256). https://www.rbi.org.in",
 47: "Apple Inc. (2026). App Store customer reviews feed, India: PhonePe, Google Pay, Paytm, BHIM and YONO SBI, 30 Apr to 18 Nov 2026 [Data set collected by the authors; names not stored].",
 48: "Google Play Store and Apple App Store. (2026). Public reviews of eight bank apps, India, 5 Jun to 19 Nov 2026 [Data set collected by the authors; names not stored].",
 52: "Aadil, A., Ahuja, G., Sah, R., & Dhumal, S. (2023). Decoding the extent and exposure of financial fraud among DFS customers (MSC Policy Brief No. 28). MicroSave Consulting.",
 53: "Sengupta, A., Furtado, C., Agrawal, G., Sekhar, N., Sneha, P. P., & Kharbanda, V. (2025). Navigating the digitalisation of finance: User experiences of risks and harms. Centre for Internet and Society. https://cis-india.org/raw/navigating-the-digitalisation-of-finance",
}
REFS.update(SHORT)
""", 1)
rep("p.paragraph_format.space_after = Pt(2); p.paragraph_format.line_spacing = 1.0\n    add_runs(p, f'[{i}] '", "p.paragraph_format.space_after = Pt(1); p.paragraph_format.line_spacing = 1.0\n    add_runs(p, f'[{i}] '")
open(p, 'w', encoding='utf-8').write(s)
print('patched')

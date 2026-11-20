# -*- coding: utf-8 -*-
import shutil
from pathlib import Path
shutil.copy('Condensed/figure8_review_categories.png', 'Group_31_Final_Submission/figures/figure8_review_categories.png')
# --- new references (verified on Crossref / OpenAlex, 20 Nov 2026)
refs = Path('Condensed/references_source.txt')
t = refs.read_text(encoding='utf-8')
if '[Nor] [55]' not in t:
    t += "\n" + "\n".join([
        "[Nor] [55] Stiglitz, J. E., & Weiss, A. (1981). Credit rationing in markets with imperfect information. American Economic Review, 71(3), 393–410.",
        "[Nor] [56] Berger, A. N., & Udell, G. F. (1998). The economics of small business finance: The roles of private equity and debt markets in the financial growth cycle. Journal of Banking & Finance, 22(6–8), 613–673. https://doi.org/10.1016/S0378-4266(98)00038-7",
        "[Nor] [57] Beck, T., & Demirgüç-Kunt, A. (2006). Small and medium-size enterprises: Access to finance as a growth constraint. Journal of Banking & Finance, 30(11), 2931–2943. https://doi.org/10.1016/j.jbankfin.2006.05.009",
        "[Nor] [58] Evans, D. S., & Jovanovic, B. (1989). An estimated model of entrepreneurial choice under liquidity constraints. Journal of Political Economy, 97(4), 808–827. https://doi.org/10.1086/261629",
        "[Nor] [59] Berg, T., Burg, V., Gombović, A., & Puri, M. (2018). On the rise of FinTechs: Credit scoring using digital footprints (NBER Working Paper No. 24551). https://doi.org/10.3386/w24551"])
    refs.write_text(t, encoding='utf-8')

p = 'Condensed/build_short_paper.py'
s = open(p, encoding='utf-8').read()


def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:70], s.count(a))
    s = s.replace(a, b)


def cut(start, end):
    global s
    i = s.index(start); j = s.index(end, i)
    s = s[:i] + s[j:]


# figures may live in the final folder's figures directory
rep("doc.styles['Normal'].paragraph_format.space_after = Pt(5)", "doc.styles['Normal'].paragraph_format.space_after = Pt(3)")
rep("acad = sum(1 for k in order if k <= 36)", "acad = sum(1 for k in order if k <= 36 or k >= 55)")

# --- JEL codes
rep("P('**Keywords:** financial inclusion; mobile banking; digital payments; cybersecurity; fraud exposure; Global Findex; entrepreneurial finance; India')",
    "P('**Keywords:** financial inclusion; mobile banking; digital payments; cybersecurity; fraud exposure; Global Findex; entrepreneurial finance; India. **JEL codes:** G21, G23, L26, O16.')")

# --- intro: entrepreneurial link
rep("For a small business or first-time digital customer, an account helps only if", "For a small merchant, a first-time business owner or any digital customer, an account helps only if")

# --- literature: entrepreneurial finance
rep("H2('2.2 Adoption, trust and fintech')", "H2('2.2 Entrepreneurial finance, adoption, trust and fintech')")
rep('P("Adoption depends on perceived usefulness and ease of use {25};',
    'P("Entrepreneurial finance starts from information asymmetry: lenders ration credit even in equilibrium because higher rates worsen the mix of borrowers {55}; small and young firms rely on different sources as they grow and become more transparent {56}; access to finance constrains small-firm growth {57}; and binding liquidity constraints keep would-be entrepreneurs out of business {58}. '
    'Digital data can ease this constraint, since simple digital-footprint variables match or exceed credit-bureau scores in predicting default, including for unscorable customers {59}. Inclusion therefore matters for entrepreneurship, but the same digital channels expose small merchants to the fraud described below. "\n  "Adoption depends on perceived usefulness and ease of use {25};')

# --- results: replace category table and finance table by figures; drop group table
cut("table('cat',", "H2('4.6 Institutional documents and published studies')")
s = s.replace("H2('4.6 Institutional documents and published studies')", "figure('cat', 'figure8_review_categories.png', \"Classification of fraud-keyword reviews by category and dataset. Source: authors' first-pass classification of {39,47,48}; second-pass agreement is in Section 3.5.\", 5.6)\nH2('4.6 Institutional documents and published studies')", 1)
cut("table('fin',", "# ============================================================ 5 DISCUSSION")
s = s.replace("# ============================================================ 5 DISCUSSION", "figure('fin', 'figure4.png', \"Illustrative annual operating surplus or deficit by scenario (INR lakh; assumptions, not findings; no churn, tax or financing flows).\", 4.6)\n\n# ============================================================ 5 DISCUSSION", 1)
rep("poor grievance handling (Table 5). \"", "poor grievance handling (Figure 2). \"")
rep("INR 48.80 and 173.16 lakh in Years 2 and 3 (Table 6). \"", "INR 48.80 and 173.16 lakh in Years 2 and 3 (Figure 3). \"")

# --- RQ answers table (end of the first Discussion paragraph block)
rep("H2('5.1 Academic implications')", '''table('rq', 'Answers to the research questions', [
    ['Question', 'Answer and main limit'],
    ['Central: more inclusion, more cyber risk?', 'Partly: users report more requests (13.1% vs 4.3%; OR 3.45) but the group-level link is weak (0.38). Descriptive.'],
    ['RQ1 Differences and peers', 'Ownership 89.0%, digital payment 48.5%, lock 57.7%; lower for women and the lowest income quintile. Peer values lack sampling errors.'],
    ['RQ2 Payment use and requests', 'Adjusted OR 3.45 (2.24 to 5.30); robust to extra design effects up to 3. Association, not causation.'],
    ['RQ3 Lock and sending money', 'No protective association (25.0% with lock, 8.9% without); p = 0.11; 45 senders.'],
    ['RQ4 Largest gap', 'Ages 60+ (+33.7 points) and ages 15 to 24 (−32.1). Different denominators.'],
    ['RQ5 Reviews, documents, studies', 'Grievances are rewards, refunds, support, blocks, prompts; theft is rare. Self-selected reviews; small studies.'],
    ['RQ6 Break-even', 'Eight institutions (13 while growing); base case −32.80, 0.00, +52.16 lakh. Inputs are assumptions.'],
], [1.9, 4.6], note="Source: authors' summary of Sections 4 and 5.")
H2('5.1 Academic implications')''')

# --- data availability (inside the Conclusion section)
rep("# ============================================================ REFERENCES", '''P("**Data availability.** The India household microdata are available from the World Bank microdata library {37} under its access terms and are not redistributed here. Country indicators come from the World Bank open data API {38}. The app-review snapshots (no usernames), analysis scripts, results tables and the notebook are in the submission folder (data/, scripts/, results/, analysis.ipynb); fetch_data.py reproduces the downloads.")

# ============================================================ REFERENCES''')
open(p, 'w', encoding='utf-8').write(s)
print('patched4')

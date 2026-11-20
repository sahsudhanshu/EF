# -*- coding: utf-8 -*-
"""Condensed (10-12 page) version of the Group 31 paper, in the TA's structure.
Run from C:\\Users\\Sudhanshu\\Desktop\\EF :  python Condensed/build_short_paper.py
Reference entries are read from Condensed/references_source.txt.
Citations are written with the OLD reference numbers of the full paper, {n}, and renumbered by first appearance."""
import re
from pathlib import Path
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

OUT = Path('Condensed/Group_31_Research_Paper_Short.docx')
FIG = Path('Group_31_Final_Submission/figures')
FONT = 'Times New Roman'

# ---- references: parsed from the full paper's list ("[n] text")
REFS = {}
for line in Path('Condensed/references_source.txt').read_text(encoding='utf-8').splitlines():
    m = re.match(r'\[Nor\] \[(\d+)\] (.+)', line)
    if m:
        REFS[int(m.group(1))] = m.group(2)
order = []
SHORT = {
 40: "World Bank. (n.d.). Trust. In Inclusive digital financial services: A reference guide for policymakers and regulators. digitalfinance.worldbank.org",
 41: "World Bank. (n.d.). Financial inclusion and consumer protection. Responsible Financial Access. responsiblefinance.worldbank.org",
 38: "World Bank. (2025). Global Findex Database 2025 country indicators (account.t.d, con1, con18.s, con21.s; 2024) [Data set]. World Bank Data API, source 28.",
 39: "Google Play Store. (2026). Public reviews of PhonePe, Google Pay, Paytm, BHIM and SBI YONO, India, 2 Oct to 19 Nov 2026 [Data set collected by the authors; usernames not stored].",
 42: "Reserve Bank of India. (2020, June 22). Increasing instances of payment frauds: Enhancing public awareness campaigns through multiple channels (RBI/2019-20/256).",
 47: "Apple Inc. (2026). App Store customer reviews feed, India: PhonePe, Google Pay, Paytm, BHIM and YONO SBI, 30 Apr to 18 Nov 2026 [Data set collected by the authors; names not stored].",
 48: "Google Play Store and Apple App Store. (2026). Public reviews of eight bank apps, India, 5 Jun to 19 Nov 2026 [Data set collected by the authors; names not stored].",
 52: "Aadil, A., Ahuja, G., Sah, R., & Dhumal, S. (2023). Decoding the extent and exposure of financial fraud among DFS customers (MSC Policy Brief No. 28). MicroSave Consulting.",
 53: "Sengupta, A., Furtado, C., Agrawal, G., Sekhar, N., Sneha, P. P., & Kharbanda, V. (2025). Navigating the digitalisation of finance: User experiences of risks and harms. Centre for Internet and Society. cis-india.org",
}
REFS.update(SHORT)
for _k, _a, _b in [(38, '(2025)', '(2025a)'), (9, '(2025)', '(2025b)'), (41, '(n.d.)', '(n.d.-a)'), (40, '(n.d.)', '(n.d.-b)')]:
    REFS[_k] = REFS[_k].replace(_a, _b, 1)


OVERRIDE = {9: 'World Bank, 2025b', 38: 'World Bank, 2025a', 37: 'Development Research Group, 2025', 39: 'Google Play Store, 2026',
            40: 'World Bank, n.d.-b', 41: 'World Bank, n.d.-a', 42: 'Reserve Bank of India, 2020', 47: 'Apple Inc., 2026',
            48: 'Google Play Store & Apple App Store, 2026', 45: 'World Bank, n.d.-c', 46: 'Press Information Bureau, 2026'}


def label(k):
    """APA parenthetical label, e.g. 'Suri & Jack, 2016' or 'Demirguc-Kunt et al., 2017'."""
    if k in OVERRIDE:
        return OVERRIDE[k]
    t = REFS[k]
    head = t[:t.index(' (')]
    year = re.match(r'\((\d{4}|n\.d\.)', t[len(head) + 1:]).group(1)
    names = re.findall(r"(?:^|, |& )([^,&]+?), (?:[A-Z]\.(?:[ -]|(?=,)|$))+", head + ',')
    if not names:
        names = [head.rstrip('.')]
    if len(names) == 1:
        a = names[0]
    elif len(names) == 2:
        a = names[0] + ' & ' + names[1]
    else:
        a = names[0] + ' et al.'
    return f'{a}, {year}'


def cite(m):
    labs = []
    for k in m.group(1).split(','):
        k = int(k)
        assert k in REFS, k
        if k not in order:
            order.append(k)
        labs.append(label(k))
    return '(' + '; '.join(sorted(set(labs), key=lambda x: x.lower())) + ')'


def cites(t):
    return re.sub(r'\{(\d+(?:,\d+)*)\}', cite, t)


doc = Document()
sec = doc.sections[0]
sec.page_width, sec.page_height = Inches(8.5), Inches(11)
for a in ('left_margin', 'right_margin'):
    setattr(sec, a, Inches(1))
for a in ('top_margin', 'bottom_margin'):
    setattr(sec, a, Inches(0.9))


def set_font(style):
    style.font.name = FONT; style.font.size = Pt(12)
    rpr = style.element.get_or_add_rPr()
    rf = rpr.find(qn('w:rFonts'))
    if rf is None:
        rf = OxmlElement('w:rFonts'); rpr.append(rf)
    for att in ('w:ascii', 'w:hAnsi', 'w:eastAsia', 'w:cs'):
        rf.set(qn(att), FONT)
    for att in ('w:asciiTheme', 'w:hAnsiTheme', 'w:eastAsiaTheme', 'w:cstheme'):
        if rf.get(qn(att)) is not None:
            del rf.attrib[qn(att)]
    style.font.color.rgb = None


for s in doc.styles:
    try:
        if s.type in (1, 2):
            set_font(s)
    except Exception:
        pass
doc.styles['Normal'].paragraph_format.space_after = Pt(3)
doc.styles['Normal'].paragraph_format.line_spacing = 1.0
for h in ('Heading 1', 'Heading 2', 'Title', 'Caption'):
    st = doc.styles[h]
    st.font.size = Pt(12); st.font.bold = True; st.font.italic = False
    st.paragraph_format.space_before = Pt(6 if h != 'Caption' else 2)
    st.paragraph_format.space_after = Pt(4)
    st.paragraph_format.keep_with_next = h != 'Caption'
_ppr = doc.styles['Title'].element.get_or_add_pPr()
for b in _ppr.findall(qn('w:pBdr')):
    _ppr.remove(b)


def add_runs(p, text, bold=False, italic=False):
    text = cites(text)
    text = re.sub(r'(?<=\S)  +(?=\S)', ' ', text)
    for i, part in enumerate(re.split(r'\*\*(.+?)\*\*', text)):
        if not part:
            continue
        r = p.add_run(part)
        r.font.name = FONT; r.font.size = Pt(12)
        r._element.rPr.rFonts.set(qn('w:eastAsia'), FONT)
        r.bold = bold or (i % 2 == 1); r.italic = italic


def P(text, align='j', bold=False, after=None):
    p = doc.add_paragraph(); add_runs(p, text, bold=bold)
    p.alignment = {'j': WD_ALIGN_PARAGRAPH.JUSTIFY, 'c': WD_ALIGN_PARAGRAPH.CENTER, 'l': WD_ALIGN_PARAGRAPH.LEFT}[align]
    if after is not None:
        p.paragraph_format.space_after = Pt(after)
    return p


def H1(t): return doc.add_heading(t, level=1)
def H2(t): return doc.add_heading(t, level=2)


T = {}; F = {}
_t = [0]; _f = [0]


def table(key, title, rows, widths, note=None, bold_first=False):
    _t[0] += 1; T[key] = _t[0]
    cap = doc.add_paragraph(style='Caption')            # label ABOVE the table
    add_runs(cap, f'Table {_t[0]}: {title}', bold=True); cap.paragraph_format.keep_with_next = True
    tb = doc.add_table(rows=len(rows), cols=len(rows[0])); tb.style = 'Table Grid'
    tb.alignment = WD_TABLE_ALIGNMENT.CENTER; tb.autofit = False
    for ri, row in enumerate(rows):
        for ci, val in enumerate(row):
            c = tb.cell(ri, ci); c.width = Inches(widths[ci])
            p = c.paragraphs[0]; p.paragraph_format.space_after = Pt(0); p.paragraph_format.line_spacing = 1.0
            add_runs(p, str(val), bold=(ri == 0 or (bold_first and ci == 0)))
            if ri == 0:
                shd = OxmlElement('w:shd'); shd.set(qn('w:val'), 'clear'); shd.set(qn('w:color'), 'auto'); shd.set(qn('w:fill'), 'D9D9D9')
                c._tc.get_or_add_tcPr().append(shd)
        tb.rows[ri]._tr.get_or_add_trPr().append(OxmlElement('w:cantSplit'))
        if ri < len(rows) - 1:
            for c in tb.rows[ri].cells:
                for pp in c.paragraphs:
                    pp.paragraph_format.keep_with_next = True
    tb.rows[0]._tr.get_or_add_trPr().append(OxmlElement('w:tblHeader'))
    if note:
        n = P(note, align='l'); n.paragraph_format.space_before = Pt(2)
    else:
        sp = doc.add_paragraph(); sp.paragraph_format.space_after = Pt(0); sp.paragraph_format.line_spacing = Pt(5)


def figure(key, fname, title, width):
    _f[0] += 1; F[key] = _f[0]
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.keep_with_next = True
    p.paragraph_format.space_after = Pt(2)
    p.add_run().add_picture(str(FIG / fname), width=Inches(width))
    cap = doc.add_paragraph(style='Caption')            # label BELOW the figure
    add_runs(cap, f'Figure {_f[0]}: {title}', bold=True); cap.paragraph_format.space_after = Pt(6)


fp = sec.footer.paragraphs[0]; fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = fp.add_run(); r.font.name = FONT; r.font.size = Pt(12)
for typ, txt in (('begin', None), (None, 'PAGE'), ('end', None)):
    if typ:
        e = OxmlElement('w:fldChar'); e.set(qn('w:fldCharType'), typ); r._r.append(e)
    else:
        e = OxmlElement('w:instrText'); e.set(qn('xml:space'), 'preserve'); e.text = txt; r._r.append(e)

# ============================================================ TITLE
tp = doc.add_paragraph(style='Title'); tp.alignment = WD_ALIGN_PARAGRAPH.CENTER
add_runs(tp, 'Mobile Banking: Financial Inclusion vs Cybersecurity Risks in India', bold=True)
P("Evidence from the Global Findex Database 2025 (India survey, fielded in 2024), public app reviews and published interview studies, with implications for entrepreneurs", align='c', after=2)
P('Rushal Verma (IIT2024045), Sudhanshu (IIT2024081) and Vichanshu Raj (IIT2024083)', align='c', after=0)
P('Group 31, Entrepreneurial Finance | Indian Institute of Information Technology, Allahabad', align='c')

H1('Abstract')
ABSTRACT = ("This study asks whether the spread of mobile banking and digital payments in India comes with higher cybersecurity risk, for whom, and what this implies for entrepreneurs serving first-time digital users. "
 "We analyse the India survey of the Global Findex Database 2025 (fielded in 2024; 3,000 adults) with survey weights and an exploratory logistic model, compare India with peer economies, code 14,088 public reviews of 13 payment and bank apps from two app stores, and synthesise five published interview studies. "
 "Account ownership was 89.0%, but only 48.5% made or received a digital payment and 57.7% of phone owners reported a device lock. "
 "Payment users reported more unsolicited money requests than non-users (13.1% against 4.3%; adjusted odds ratio 3.45), yet exposure was also high in the lowest income quintile and protection lagged inclusion at older ages. "
 "Reviews rarely described theft; complaints concerned rewards, refunds, account blocks and security prompts. An illustrative model for an institution-funded safety service breaks even at eight paying institutions. "
 "The data cannot show causation, and the commercial assumptions need pilot validation.")
P(ABSTRACT)
WC = len(ABSTRACT.split()); assert 150 <= WC <= 200, WC
P('**Keywords:** financial inclusion; mobile banking; digital payments; cybersecurity; fraud exposure; Global Findex; entrepreneurial finance; India. **JEL codes:** G21, G23, L26, O16.')

# ============================================================ 1 INTRODUCTION
H1('1. Introduction')
H2('1.1 Background')
P("Access to formal finance is linked with household resilience, enterprise formation and poverty reduction {1,2}, and mobile phones and digital payments have changed how it is delivered {3,4}, in India with public digital identity and payment infrastructure {5,6}. "
  "For a small merchant, a first-time business owner or any digital customer, an account helps only if it can be used reliably and without undue risk. Financial inclusion here means use of formal financial services: account ownership measures access, digital payment use measures activity. Reported cybersecurity exposure means a report of an unsolicited call or message asking for money, a sign of a possible scam attempt and not verified fraud. The World Bank's Global Findex is the main cross-country source for the first two measures {7,8,9}.")
H2('1.2 Problem and importance')
P("Mobile banking can bring people into the formal system, but each new user is also a possible target and may lack the safeguards of experienced users; deception exploits ordinary behaviour {10,11}, and trust shapes adoption {12,13}.  "
  "This matters because trust and safety shape whether new users keep using digital channels {12,13}, and because institutions and entrepreneurs that serve them need to know where safeguards are weakest.")
H2('1.3 Research gap')
P("The literature is strong on mobile-money benefits and on phishing, but rarely joins them in a recent national survey of India, and little work turns such patterns into an entrepreneurial question: what service could be built, who would pay, and what would make it viable. This study addresses that gap with the Global Findex India survey, public app reviews and published interview studies, and a transparent, assumption-labelled venture model.")
H2('1.4 Research questions')
P("We ask where inclusion and cybersecurity risk move together, where they do not, and what institutions and entrepreneurs could do. The six questions are: RQ1: How do account ownership, digital payment use and device protection differ by gender, age and income, and how does India compare with peer economies? "
  "RQ2: Are payment users more likely than non-users to report unsolicited money requests, after adjustment? "
  "RQ3: Among people who report a request, is a device lock associated with fewer reporting that they sent money? "
  "RQ4: Which groups show the largest gap between digital payment use and device protection? "
  "RQ5: What do public app reviews, institutional documents and published interview studies reveal about fraud grievances, security friction and support? "
  "RQ6: What price, cost and customer numbers would let an institution-funded safety service break even? "
  "The paper is organised as follows. Section 2 reviews the literature, Section 3 sets out the methodology, Section 4 reports the results, Section 5 discusses their academic, policy and managerial implications and limitations, and Section 6 concludes.")

# ============================================================ 2 LITERATURE REVIEW
H1('2. Literature review')
P("This review covers inclusion and mobile money, adoption and trust, security behaviour and fraud, and cyber-risk economics (35 academic sources), and ends with the gap this study fills.")
H2('2.1 Inclusion, mobile money and development')
P("Deeper finance disproportionately raises the incomes of the poorest {14}, and account access supports inclusive growth depending on how accounts are used {1}. Measurement advanced with the Global Findex {7} and its rounds {8,9}, which separated ownership from usage. "
  "The best causal evidence is from Kenya: M-PESA helped households share risk {18} and lifted around 2% of households out of poverty, more in female-headed households {2}. Mobile transfers improved diets in Niger {19}, debit cards raised savings in Mexico {20}, diffusion varies by institutional context {21}, and digital inclusion is linked with growth {22}. "
  "In India, biometric payments reduced leakage {5} and demonetisation was used to study digital payments {6}; gains are not automatic, as microcredit raised business investment but not average consumption {23}. Benefits arise when services are used, so this study measures use, not ownership alone.")
H2('2.2 Entrepreneurial finance, adoption, trust and fintech')
P("Entrepreneurial finance starts from information asymmetry: lenders ration credit even in equilibrium because higher rates worsen the mix of borrowers {55}; small and young firms rely on different sources as they grow and become more transparent {56}; access to finance constrains small-firm growth {57}; and binding liquidity constraints keep would-be entrepreneurs out of business {58}. Digital data can ease this constraint, since simple digital-footprint variables match or exceed credit-bureau scores in predicting default, including for unscorable customers {59}. Inclusion therefore matters for entrepreneurship, but the same digital channels expose small merchants to the fraud described below. "
  "Adoption depends on perceived usefulness and ease of use {25}; for mobile banking, credibility, self-efficacy and cost shape intention {12}. Fintech changes industry structure and user expectations {4} and is a driver of inclusion that needs digital identity and interoperable payments {27}, but digital finance has persistent unresolved issues {13}. Safety and trust are conditions for continued use, not extras.")
H2('2.3 Security behaviour, phishing and fraud')
P("Users reject protections that conflict with their tasks {28}. Well-designed fake websites deceive many participants {10}; awareness of phishing risk is unrelated to perceived vulnerability, so people manage familiar risks but not unfamiliar ones {29}; and fraud victims are diverse, with scams exploiting authority, small sums, pressure and trust {11,30}. "
  "Awareness campaigns often fail to change behaviour {31}, though short online education reduced fraud susceptibility in a U.S. experiment, lasting three months only with a reminder {32}.")
H2('2.4 Cyber risk, incentives and the research gap')
P("Security is under-provided because incentives and externalities separate those who bear losses from those who can prevent them {33}; optimal spending depends on vulnerability and potential loss {34}; and cyber risk is a market failure and source of instability {35}. "
  "Three conclusions follow: inclusion benefits depend on use {1,2,18}; adoption depends on trust while security failures exploit ordinary behaviour {10,11,12}; and safety is a shared responsibility that markets under-supply {33,35}. "
  "Missing is a recent national view for India that places adoption, device protection and reported scam exposure side by side, adds what users say in their own words, and links the pattern to a venture and its viability. This study addresses that gap.")

# ============================================================ 3 METHODOLOGY
H1('3. Methodology')
H2('3.1 Research Design')
P("The design is cross-sectional, observational and descriptive-analytical: weighted descriptives and group comparisons (RQ1, RQ4); a weighted logistic model (RQ2) and lock-status comparison (RQ3); a peer comparison; qualitative analysis of documents, app reviews and published interview studies (RQ5); and a deterministic financial model (RQ6). "
  "**Justification:** a population survey is the only source recording adoption and exposure for the same adults; interviews of our own were not feasible, so published studies serve as secondary evidence; and scenario modelling is the standard test of a venture before commercial data exist.")
H2('3.2 Sampling Method and Participants')
P("We use the India file of the Global Findex Database 2025 (survey year 2024, IND_2024_FINDEX_v02_M) {37}: 3,000 respondents aged 15 or older, a nationally representative adult sample drawn by the World Bank and Gallup. All percentages use the survey weight (wgt); n and counts are unweighted. The data describe individuals, not businesses. **Justification:** it is the standard public inclusion benchmark and the only source linking payments to phone-safety items in India.")
H2('3.3 Data Collection Methods')
P("Seven public sources were used: the India Findex microdata {37}; Findex 2025 country indicators for India and nine peers {38}; Google Play reviews of five payment apps (PhonePe, Google Pay, Paytm, BHIM, SBI YONO; 5,758 reviews, 2 Oct to 19 Nov 2026) {39}; App Store reviews of the same apps (2,090; 30 Apr to 18 Nov) {47}; reviews of eight bank apps in both stores (6,240; 5 Jun to 19 Nov) {48}; three institutional documents {40,41,42}; and five published interview studies {49,50,51,52,53} found by targeted search on 20 November 2026 (not a systematic review). "
  "Reviews were collected with google-play-scraper and Apple's public feed; only app, date, rating and text were kept (no names, emails or phone numbers), and reviews under 15 characters and duplicates were removed. We conducted no interviews or surveys of our own. "
  "**Justification:** public data permit reproduction, reviews give unprompted user language, and published studies supply victim and merchant experience that reviews rarely contain.")
H2('3.4 Materials and Instruments')
P("Python (pandas, numpy, matplotlib) was used; scripts, an audit file and the coding scheme are in the submission folder. Variables: account, anydigpayment (made or received a digital payment in the past year), con1 (phone), con18 (lock; 2,141 valid), con21 (unsolicited request; 2,145 phone owners) and con22 (sent money; 219 recipients). "
  "**Justification:** open tools keep every step reproducible, and the stored keyword dictionaries and coding scheme make the review coding auditable.")
P("**Data availability.** The India household microdata are available from the World Bank microdata library {37} under its access terms and are not redistributed here. Country indicators come from the World Bank open data API {38}. The app-review snapshots, scripts, results tables and notebook are in the submission folder (data/, scripts/, results/, analysis.ipynb).")
H2('3.5 Data Analysis')
P("**Survey.** A weighted share is the sum of weights of positive responses over the sum of weights of valid responses, with each subgroup using its own denominator. For RQ2 the outcome is a reported request among phone owners, with payment use, gender, age, education, income quintile, workforce status and urban residence as predictors, estimated by weighted maximum likelihood with an independent-observation sandwich covariance; the public file has no strata or cluster identifiers, so intervals are approximate, and a Kish design effect and assumed extra effects of 1.5, 2 and 3 serve as sensitivity checks. "
  "For RQ4 each group's payment-use share (all adults) is set beside its lock share (phone owners) and, for the central question, its exposure across 18 groups with Spearman rank correlations; denominators differ, so this is descriptive. RQ3 uses a Fisher exact test on unweighted counts, and peer values are compared without tests.")
P("**Qualitative.** Document passages on trust, shared responsibility and credential protection were grouped into themes. Reviews were coded in two steps: dictionaries flagged five themes (fraud, failed payment, support, account blocking or verification, safety language) plus security-friction prompts for bank apps, then every fraud-keyword review was read and placed in one of seven categories by one coder. "
  "Blind AI second passes agreed on 112 of 118 Google Play reviews (94.9%, kappa 0.93), 47 of 57 App Store reviews (82.5%, 0.78) and 57 of 65 bank-app reviews (87.7%, 0.84). A human coder outside the group, blind to the labels, re-coded 40 of the 118 Google Play reviews (38 agreed, 95.0%, kappa 0.93). A further second coder (a person who used software, including AI tools, as an aid but made each coding decision, as reported by the group), who coded all 122 App Store and bank-app fraud-keyword reviews without seeing the first-pass labels, agreed with the first pass on 102 (83.6%, kappa 0.80; App Store 80.7%, 0.76; bank apps 86.2%, 0.81) and with the AI second pass on 104 (85.2%, 0.82). "
  "Bank and payment apps were compared by chi-square tests (Holm adjustment). Published-study findings were mapped to eight themes from the full texts by one coder; counts are of studies, not respondents.")
P("**Financial model.** The model is deterministic and illustrative; no input comes from Findex. Base assumptions are a fee of INR 50,000 per institution per month, variable cost INR 10,000, acquisition cost INR 2 lakh and fixed cost INR 3 lakh a month (growing 20% a year), with fees of INR 40,000 and 60,000 in the conservative and optimistic scenarios. Customers grow linearly from zero with no churn; tax, interest and prelaunch spending are excluded. Amounts are in INR lakh (1 lakh = INR 100,000).")
P("**Justification:** weighting is needed for population statements; the logistic model separates payment use from demographic differences; group comparisons and rank correlations answer the inclusion-versus-risk question without overclaiming; Fisher and chi-square tests suit small counts; two-step coding with second coders makes free text measurable and checks reliability; and scenario and sensitivity analysis shows which assumptions drive viability without false precision.")
H2('3.6 Ethical Considerations')
P("De-identified public microdata are used under the World Bank's access terms and not redistributed; reviews are public with no usernames stored; published studies are summarised, not reproduced. Exposure is reported as reports, not verified fraud, and commercial figures are illustrative with no partner, investor or willingness to pay claimed. Future interviews or pilots would need informed consent and would not collect credentials. **Justification:** public, de-identified data and no stored names let us study a sensitive topic without exposing individuals, and labelling exposure as reports and finance as illustrative keeps claims within the evidence.")

# ============================================================ 4 RESULTS
H1('4. Results')
P("Percentages are survey-weighted unless stated; counts and n are unweighted. This section reports findings without interpretation.")
H2('4.1 Adoption, exposure and device protection')
P("Account ownership was 89.0% and digital payment use 48.5% (a 40.6-point difference); phone ownership was 66.5%. Women's payment use was 42.7% and men's 54.1%. Of phone owners with valid answers, 57.7% reported a device lock. Lock use was 50.3% for women and 62.7% for men, 75.7% at ages 15 to 24 and 22.9% at 60 and above, and 40.6% in the lowest income quintile and 75.2% in the highest. "
  "Among phone owners 9.4% reported an unsolicited request (13.1% of payment users, 4.3% of non-users), and 21.0% of the 219 recipients reported sending money (Table 1; Figures 1 and 2).")
table('ind', 'Adoption, exposure and device protection (weighted)', [
    ['Indicator and group', 'Positive / valid n', 'Weighted share'],
    ['Account ownership | digital payment, all adults', '2,710 | 1,539 / 3,000', '89.0% | 48.5%'],
    ['Digital payment, women | men', '679 / 1,526 | 860 / 1,474', '42.7% | 54.1%'],
    ['Phone lock, all phone owners', '1,321 / 2,141', '57.7%'],
    ['Phone lock, women | men', '505 / 919 | 816 / 1,222', '50.3% | 62.7%'],
    ['Phone lock, ages 15–24 | 60+', '385 / 497 | 38 / 154', '75.7% | 22.9%'],
    ['Phone lock, lowest | highest income quintile', '135 / 298 | 473 / 623', '40.6% | 75.2%'],
    ['Request, phone owners', '219 / 2,145', '9.4%'],
    ['Request, payment users | non-users', '173 / 1,283 | 46 / 862', '13.1% | 4.3%'],
    ['Sent money, request recipients', '45 / 219', '21.0%'],
], [3.0, 2.0, 1.5], note="Source: authors' calculations from {37}. Positive counts are unweighted.")
figure('acc', 'pfig_access_gender.png', "Account ownership, phone ownership and digital payment use among all adults, and digital payment use and phone lock by gender (survey-weighted). Source: authors' calculations from {37}.", 6.2)
figure('lock', 'pfig_lock_groups.png', "Device-lock use among phone owners by group (survey-weighted; teal and amber bars show the two highest and lowest groups). Source: authors' calculations from {37}.", 6.0)
H2('4.2 Adjusted association and lock status')
P("In the adjusted model (2,145 phone owners; 219 positive) the odds ratio for payment users versus non-users was 3.45 (approximate 95% interval 2.24 to 5.30) and for women versus men 0.47 (0.32 to 0.69); tertiary versus primary education or less was 1.70 (1.03 to 2.80), and age, income, workforce and urban residence had intervals including 1.00 (Table 2). With variance inflated for an assumed extra design effect of 3, the payment-user interval was 1.64 to 7.26 and the women interval 0.24 to 0.92, but the tertiary interval included 1.00 from an extra effect of 1.5. "
  "For RQ3, 25.0% of recipients whose phone had a lock (39 of 170) and 8.9% of those without (6 of 49) reported sending money; the Fisher exact test gave p = 0.11 (Figure 3).")
table('model', 'Exploratory weighted logistic model for unsolicited requests', [
    ['Predictor and comparison', 'Adjusted odds ratio', 'Approx. 95% interval'],
    ['Payment user versus non-user', '3.45', '2.24 to 5.30'],
    ['Woman versus man', '0.47', '0.32 to 0.69'],
    ['Tertiary versus primary education or less', '1.70', '1.03 to 2.80'],
], [3.0, 1.5, 2.0], note="Source: authors' calculations from {37}. Intervals assume independent respondents and are not design-based.")
figure('exp', 'pfig_exposure.png', "Reported unsolicited money requests by digital payment use, and sending money after a request by lock status (survey-weighted percentages; counts are unweighted). Source: authors' calculations from {37}.", 6.2)
H2('4.3 Inclusion, exposure and protection by group')
P("Payment use exceeded lock use most at ages 60 and above (56.6% against 22.9%; +33.7 points) and fell short of it most at ages 15 to 24 (43.5% against 75.7%; −32.1; Figure 5). Across 18 overlapping groups the rank correlation was 0.38 between payment use and exposure and 0.63 between payment use and lock use (Figure 4). "
  "Exposure was highest among tertiary-educated adults (17.9%, payment use 74.5%), the lowest income quintile (12.5%, payment use 34.8%) and men (11.8%), and lowest at ages 60 and above (4.1%) and among women (5.7%).")
figure('inc', 'figure7_inclusion_vs_risk.png', "Inclusion and reported exposure by group (survey-weighted; each point is a group). Source: authors' calculations from {37}.", 3.5)
figure('gap', 'pfig_gap_groups.png', "Digital payment use (all adults) beside phone-lock use (phone owners) by group. Source: authors' calculations from {37}; the two shares have different denominators.", 6.2)
H2('4.4 Peer economies')
P("Among the seven economies in Table 3 and Figure 6, India's account ownership (89.0%) was second to China's (89.4%) and its phone ownership (66.5%) second lowest, above Pakistan (62.9%). India's lock share (57.6%) compared with 46.4% to 78.0% for peers. "
  "India's request share (9.4%, our microdata; the API publishes no value) compared with 12.7% to 32.4% for peers.")
table('peer', 'India compared with peer economies, 2024 (percent)', [
    ['Economy', 'Account', 'Own phone', 'Phone lock', 'Request'],
    ['India', '89.0', '66.5', '57.6', '9.4†'],
    ['China', '89.4', '96.6', 'n/a', 'n/a'],
    ['Indonesia | Bangladesh', '56.3 | 43.3', '80.3 | 82.4', '69.1 | 47.5', '18.5 | 12.7'],
    ['Pakistan | Brazil', '27.3 | 86.4', '62.9 | 92.1', '46.4 | 78.0', '18.8 | 32.4'],
    ['South Africa', '81.1', '87.0', '68.5', '13.5'],
    ['Lower middle income | World', '70.4 | 78.7', '75.1 | 85.7', '57.1 | n/a', '15.0 | n/a'],
], [2.3, 1.0, 1.1, 1.1, 1.0], note="Source: {38}. Account and phone: % of adults; lock and request: % of phone owners. † Our weighted microdata estimate (n = 2,145). n/a = not published.")
figure('peers', 'figure5.png', "India and peer economies on account ownership, phone ownership, phone lock and unsolicited requests (2024). Source: {38}; India's request share from authors' calculations.", 4.6)
H2('4.5 Public app reviews')
P("The datasets hold 5,758 Google Play and 2,090 App Store reviews of five payment apps and 6,240 reviews of eight bank apps (mean ratings 2.90, 3.31 and 2.49). Fraud-keyword reviews were 2.0%, 2.7% and 1.0% of reviews (mean ratings 1.36, 1.51 and 1.22); support, account-blocking and safety-language themes were each 3% to 8% of reviews in every dataset, and failed payments 0.4% to 2.3%. "
  "After every fraud-keyword review was read, 50.8% of Google Play payment-app reviews concerned rewards or cashback not honoured, against 29.8% on the App Store and 4.6% for bank apps, while 38.5% of bank-app reviews concerned blocked accounts, mis-selling, charges or poor grievance handling (Figure 7). "
  "Reviews of unauthorised access or theft numbered 6 (0.1%), 2 (0.1%) and 3 (below 0.1%). Security-friction prompts matched 2.4% of bank-app reviews (mean rating 1.59) and 3.9% of payment-app reviews (2.09); 104 Google Play payment-app reviews (1.8%) described device-lock, security-alert or developer-option prompts, 86 of them for BHIM. "
  "Bank and payment apps differed after Holm adjustment (p < 0.001) for fraud keywords, failed payments, safety language and security friction, but not for support (p = 0.87) or account blocking (p = 0.12). "
  "The second coder labelled 8 of the 122 App Store and bank-app reviews as unauthorised access or theft (first pass 5; about 0.1% of 8,330 reviews); 10 of its 20 disagreements with the first pass were reviews the first pass had labelled general accusations. A Hindi and Hinglish extension (41 more reviews) would raise unauthorised or unexplained-debit reports on Google Play from 6 to 12 (0.2%).")
figure('cat', 'figure8_review_categories.png', "Classification of fraud-keyword reviews by category and dataset. Source: authors' first-pass classification of {39,47,48}; second-pass agreement is in Section 3.5.", 5.1)
H2('4.6 Institutional documents and published studies')
P("The documents yield three themes: trust linked with risk awareness and timely dispute resolution {40}; consumer protection alongside financial capability {41}; and RBI calls for awareness campaigns and protection of credentials such as OTPs and PINs {42}. "
  "Of eight themes in the five published studies, social engineering, trust in the counterparty or bank, and low awareness appeared in all five; weak support or redress and reliance on family or informal channels in four; differences by gender, age or vulnerability in three; and protective advice and design cues and merchant harms in two each. Examples: 45 of 46 participants said trust in the receiver matters {50}; 12 of 24 merchants reported fake payment confirmations {51}; and of 91 victims who reported the fraud to authorities, 59 could not recover their money {53} (Figure 8).")
figure('stud', 'pfig_studies.png', "Themes reported by the five published interview studies (counts are of studies, not respondents). Source: authors' coding of {49,50,51,52,53}.", 5.8)
H2('4.7 Illustrative financial model outputs')
P("Contribution per institution is INR 40,000 a month (80%) and simple acquisition payback is 5 months. Steady-state break-even is 8 paying institutions, or 13 when one new institution is acquired each month. The base case records a deficit of INR 32.80 lakh in Year 1, zero in Year 2 and a surplus of INR 52.16 lakh in Year 3; the conservative case is in deficit throughout (INR 36.80, 30.00 and 17.44 lakh) and the optimistic case reaches INR 48.80 and 173.16 lakh in Years 2 and 3. "
  "Cutting the fee to INR 40,000 raises break-even to 10 institutions, raising variable cost to INR 15,000 raises it to 9, and an acquisition cost of INR 3 lakh extends payback to 7.5 months; across all fee and cost combinations tested the requirement is 6 to 12 (Figure 9).")

figure('fin', 'pfig_finance.png', "Illustrative annual operating surplus or deficit by scenario (INR lakh; assumptions, not findings; no churn, tax or financing flows). Source: authors' calculations.", 5.8)

# ============================================================ 5 DISCUSSION
H1('5. Discussion')
P("**Inclusion versus cybersecurity risk.** Payment users reported more unsolicited requests than non-users and the association survived adjustment, so inclusion in digital payments goes with greater reachability by scammers, plausibly because digital users are reachable through more channels {30}. "
  "Across groups the link was weak to moderate (rank correlation 0.38): exposure was highest among the most included (tertiary-educated) but also in the lowest income quintile, and lowest among older adults and women. Protection rose with inclusion (0.63) except among older adults, whose payment use far exceeds lock use. "
  "Risk therefore concentrates where inclusion outruns safeguards and where people have little margin for loss. A lock limits access to a handset, not deception {10,11,28}; the RQ3 comparison rests on 45 senders and is not significant.")
P("**Reviews, studies and documents.** Review complaints concern rewards, refunds, support, blocks and security prompts far more than theft, on both platforms. This does not measure scam prevalence: victims may not write reviews, and the interview studies describe the social engineering, trust and slow redress that reviews rarely capture; support and redress failures appear in both sources, consistent with the documents {40,41,42}. "
  "In bank apps the tension shows up as friction and weak redress more than fraud: SIM binding, biometric and root-detection prompts were a recurring source of one-star reviews. Against peers, India has near-top account ownership but below-peer phone ownership and digital payment use and the lowest reported request share among economies with a value; recall, reporting and phone-based contact may explain this, and the comparison sets a sample estimate against published values without sampling error. "
  "Table 4 summarises the answers to the research questions.")
table('rq', 'Answers to the research questions', [
    ['Question', 'Answer and main limit'],
    ['Central: more inclusion, more cyber risk?', 'Partly: users report more requests (13.1% vs 4.3%; OR 3.45) but the group-level link is weak (0.38). Descriptive.'],
    ['RQ1 Differences and peers', 'Ownership 89.0%, digital payment 48.5%, lock 57.7%; lower for women and the lowest income quintile. Peer values lack sampling errors.'],
    ['RQ2 Payment use and requests', 'Adjusted OR 3.45 (2.24 to 5.30); robust to extra design effects up to 3. Association, not causation.'],
    ['RQ3 Lock and sending money', 'No protective association (25.0% with lock, 8.9% without); p = 0.11; 45 senders.'],
    ['RQ4 Largest gap', 'Ages 60+ (+33.7 points) and ages 15 to 24 (−32.1). Different denominators.'],
    ['RQ5 Reviews, documents, studies', 'Grievances are rewards, refunds, support, blocks, prompts; theft is rare. Self-selected reviews; small studies.'],
    ['RQ6 Break-even', 'Eight institutions (13 while growing); base case −32.80, 0.00, +52.16 lakh. Inputs are assumptions.'],
], [1.9, 4.6], note="Source: authors' summary of Sections 4 and 5.")
H2('5.1 Academic implications')
P("The study joins the economics of inclusion {1,2,18} with the behavioural study of scams {10,11,31} and with entrepreneurial finance {55,57}, pairing national statistics with safety indicators and user-generated text to show where access and safe use diverge. It shows how to label intervals when design variables are missing and suggests that technology-acceptance models {12,25} include perceived safety and device safeguards.")
H2('5.2 Policy implications')
P("Each implication is a hypothesis to test. Inclusion targets should track active and safe use, not only ownership {40,41}. Awareness efforts such as the RBI's {42} should be judged on behaviour change and designed for older, lower-income and women users, since generic campaigns often fail and education persisted in one experiment only with reminders {31,32}. Providers should own warnings, refunds and complaint handling, regulators clear reporting channels, and users credential hygiene {35}; security prompts should be tested so they do not lock out users.")
H2('5.3 Managerial implications')
P("The results suggest a narrow pilot of a multilingual payment-safety companion distributed through banks, payment providers or merchant networks, paid for by the institution and free to users: short audio and visual explanations, a pre-payment checklist and verified routes to support and official reporting. It would not hold money, guarantee recovery or ask for an OTP or PIN. "
  "In canvas terms the institution is the customer, revenue is a recurring subscription and costs are a small fixed team, delivery and acquisition. Campaigns {42}, in-app warnings, the national helpline and in-house builds already cover parts of the problem, so the service must add measurable value through local-language journeys with comprehension checks and faster routes to verified support. "
  "Proposed plan: months 1–2 discovery with one sponsor, months 3–5 a controlled pilot with prespecified outcomes, scale from month 6 only after a paid commitment. No pilot has been run.")
P("**Financial interpretation.** Eight institutions cover fixed costs only in steady state; about 13 are needed while growing. A 20% lower fee adds two institutions, and the base case has no cushion in Year 2, so churn or slow sales would produce a deficit; the conservative case does not break even in three years. "
  "An illustrative INR 75 lakh seed (staged equity or grant) would cover the Year 1 deficit (32.80), prelaunch build (10.00) and pilot evaluation (5.00), a working-capital reserve (12.00) and contingency (15.20), but in the conservative case deficits plus prelaunch costs reach INR 81.80 lakh by Year 2 and exceed it. Main risks are weak willingness to pay, support cost above the margin and dependence on one partner; these conclusions follow security-investment economics {33,34} and hold only if prices and costs are validated with real buyers.")
H2('5.4 Future scope and limitations')
P("**Limitations.** The survey is cross-sectional and self-reported; requests are not verified fraud, cells such as the 45 senders are small, intervals are approximate (the tertiary-education result does not survive assumed clustering), and the data describe individuals, not enterprises. "
  "Reviews are self-selected, cover different windows, and were keyword-coded by one coder with AI second passes and second-coder checks on samples; a Hindi and Hinglish extension changed no conclusion. We conducted no interviews or surveys of our own, and the five published studies were selected by us and are small. Peer values are aggregates without sampling errors, and all financial inputs are unvalidated assumptions without churn, tax or financing flows.")
P("**Future scope.** Priorities are consent-based interviews to test willingness to pay, design-based estimation, peer-country microdata, an evaluated and powered pilot {32}, and a venture model with churn and cash flow.")

# ============================================================ 6 CONCLUSION
H1('6. Conclusion')
P("This paper asked whether the spread of mobile banking in India comes with higher cybersecurity risk, and for whom. Account ownership is widespread (89.0%), but digital payment use (48.5%) and device protection (57.7%) are lower and unevenly distributed by gender, age and income. Payment users reported more unsolicited requests than non-users (13.1% against 4.3%; odds ratio 3.45), yet across groups exposure rose only weakly with inclusion, was high among the poorest, and protection lagged inclusion at older ages: risk concentrates where inclusion outruns safeguards. "
  "App reviews on both platforms and five published studies show that grievances concern rewards, refunds, account blocks, support and security prompts far more than reported theft, while social engineering and slow redress dominate the interview evidence. "
  "For entrepreneurs and institutions the evidence supports a staged pilot of an accessible, institution-funded safety service; the illustrative model breaks even at eight paying institutions but is highly sensitive to price, support and acquisition costs and is not evidence of demand. Pilot evidence on willingness to pay and effectiveness is the next step.")


# ============================================================ REFERENCES
H1('References')
for k in sorted(order, key=lambda x: re.sub(r'[^a-z0-9 ]', '', REFS[x].lower().replace('ü', 'u'))):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.35); p.paragraph_format.first_line_indent = Inches(-0.35)
    p.paragraph_format.space_after = Pt(2); p.paragraph_format.line_spacing = 1.0
    add_runs(p, REFS[k])
doc.core_properties.title = 'Mobile Banking: Financial Inclusion vs Cybersecurity Risks'
doc.core_properties.author = 'Group 31'
doc.save(OUT)
acad = sum(1 for k in order if k <= 36 or k >= 55)
print('saved', OUT, '| abstract words', WC, '| refs', len(order), '| academic', acad, '| tables', _t[0], '| figures', _f[0])

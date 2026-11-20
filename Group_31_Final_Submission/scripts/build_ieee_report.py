"""Condensed IEEE-style version of the Group 31 term paper (two columns, 10 pt).
Run from the project root:  python Group_31/revised/build_ieee_report.py
Reads the reference list from build_structured_paper.py; writes Group_31/revised/IEEE_Report.docx"""
import ast
import re
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt

R = Path('Group_31/revised')
OUT = R / 'IEEE_Report.docx'
FONT = 'Times New Roman'
src = (R / 'build_structured_paper.py').read_text(encoding='utf-8')
REFS = ast.literal_eval(re.search(r"REFS = (\{.*?\n\})\norder", src, re.S).group(1))
order = []


def cites(text):
    def one(m):
        nums = []
        for k in m.group(1).split(','):
            assert k in REFS, k
            if k not in order:
                order.append(k)
            nums.append(order.index(k) + 1)
        return '[' + ', '.join(str(n) for n in sorted(nums)) + ']'
    return re.sub(r'\{([a-z0-9_,]+)\}', one, text)


doc = Document()
st = doc.styles['Normal']
st.font.name = FONT; st.font.size = Pt(10)
st.element.rPr.rFonts.set(qn('w:eastAsia'), FONT)
st.paragraph_format.space_after = Pt(4); st.paragraph_format.line_spacing = 1.0
sec = doc.sections[0]
sec.page_width, sec.page_height = Inches(8.5), Inches(11)
for a in ('left_margin', 'right_margin'):
    setattr(sec, a, Inches(0.7))
sec.top_margin = Inches(0.7); sec.bottom_margin = Inches(0.8)


def run(p, text, size=10, bold=False, italic=False):
    r = p.add_run(text); r.font.name = FONT; r.font.size = Pt(size); r.bold = bold; r.italic = italic
    r._element.rPr.rFonts.set(qn('w:eastAsia'), FONT)
    return r


def para(text, align='j', size=10, bold=False, italic=False, after=4):
    p = doc.add_paragraph()
    text = cites(text)
    for i, part in enumerate(re.split(r'\*\*(.+?)\*\*', text)):
        if part:
            run(p, part, size, bold or i % 2 == 1, italic)
    p.alignment = {'j': WD_ALIGN_PARAGRAPH.JUSTIFY, 'c': WD_ALIGN_PARAGRAPH.CENTER, 'l': WD_ALIGN_PARAGRAPH.LEFT}[align]
    p.paragraph_format.space_after = Pt(after)
    return p


def heading(t):
    p = para(t, 'c', 10, True, after=3); p.paragraph_format.space_before = Pt(6); p.paragraph_format.keep_with_next = True


# ---- title block (single column)
p = para('Mobile Banking: Financial Inclusion vs Cybersecurity Risks', 'c', 18, True, after=2)
para("Evidence from India's 2024 Global Findex, public app reviews and published interview studies, with implications for entrepreneurs", 'c', 11, True, after=4)
para('Rushal Verma (IIT2024045), Vichanshu Raj (IIT2024083) and Sudhanshu (IIT2024081)', 'c', 11, after=0)
para('Group 31, Entrepreneurial Finance | Condensed version of the full term paper (Research_Report.pdf)', 'c', 10, italic=True, after=6)

# ---- two-column body
body = doc.add_section(WD_SECTION.CONTINUOUS)
cols = OxmlElement('w:cols'); cols.set(qn('w:num'), '2'); cols.set(qn('w:space'), '360')
body._sectPr.append(cols)

para("**Abstract**—This study asks whether the spread of mobile banking and digital payments in India comes with higher cybersecurity risk, and for whom, and what this implies for entrepreneurs who serve first-time digital users. We analyse the 2024 India Global Findex survey of 3,000 adults with survey weights and an exploratory logistic model, compare India with peer economies, code 14,088 public reviews of 13 payment and bank apps from two app stores, and synthesise five published interview studies. Account ownership was 89.0%, but only 48.5% made or received a digital payment and 57.7% of phone owners reported a device lock. Payment users reported more unsolicited money requests than non-users (13.1% against 4.3%; adjusted odds ratio 3.45), yet exposure was also high in the lowest income quintile and protection lagged inclusion at older ages. Reviews rarely described theft: payment-app complaints concerned rewards and refunds, bank-app complaints concerned account blocks, charges and security prompts. An illustrative model for an institution-funded safety service breaks even at eight paying institutions. The data cannot show causation, and the commercial assumptions need pilot validation.", size=9, bold=False)
para("**Index Terms**—financial inclusion, mobile banking, digital payments, cybersecurity, fraud exposure, Global Findex, India.", size=9, italic=True)

heading('I. INTRODUCTION')
para("Access to formal finance supports household resilience and enterprise formation {dks17,suri}. Mobile phones and instant payments have widened access in India, but owning an account, using it digitally and using it safely are different things. Mobile banking can include people who were outside the formal system, but each new user is also a new target; we ask where inclusion and cybersecurity risk move together and where they do not. We ask six questions. RQ1: how do ownership, payment use and device protection differ by gender, age and income, and against peer economies? RQ2: do payment users report more unsolicited money requests after adjustment? RQ3: among recipients, is a device lock linked to fewer reporting that they sent money? RQ4: which groups show the largest gap between payment use and device protection? RQ5: what do app reviews, institutional documents and published interview studies reveal about fraud grievances, friction and support? RQ6: what price, cost and customer numbers let an institution-funded safety service break even?")

heading('II. DATA AND METHODS')
para("**Survey.** We analyse the India file of the Global Findex 2025 (2024 survey; 3,000 adults aged 15 and over) {fxdata} and use the survey weight for all percentages. Exposure is a phone owner's report of an unknown call or message asking for money; it is not verified fraud. An exploratory weighted logistic model (2,145 phone owners) adjusts for gender, age, education, income, work and urban residence. The public file has no strata or cluster identifiers, so intervals are robust but not design-based, and we add a design-effect sensitivity check.")
para("**Peers and reviews.** Published Findex indicators for seven economies come from the World Bank API {wdi}. We collected public reviews of PhonePe, Google Pay, Paytm, BHIM and SBI YONO (5,758 Google Play, 2,090 App Store) {reviews,appstore} and of eight bank apps (4,279 Google Play, 1,961 App Store) {bankreviews}, flagged five themes with keyword dictionaries, and manually classified all fraud-keyword reviews into seven categories. A blind AI second pass agreed on 94.9% of the 118 Google Play payment-app reviews (87.7% of 65 bank-app reviews), and a human coder agreed on 95.0% of a sample of 40 (kappa 0.93). Inclusion and exposure were compared across 18 demographic groups.")
para("**Published studies and venture model.** We coded five published qualitative studies {mungara,asiaccs,jain,microsave,cis} against eight themes; we conducted no interviews ourselves. A deterministic model with three scenarios and sensitivity analysis uses illustrative, unvalidated inputs.")

heading('III. RESULTS')
rows = [['Measure', 'Result'],
        ['Account ownership', '89.0% of adults'],
        ['Made or received digital payment', '48.5% (women 42.7%, men 54.1%)'],
        ['Phone lock (phone owners)', '57.7% (women 50.3%, men 62.7%)'],
        ['Unsolicited request, payment users vs non-users', '13.1% vs 4.3%'],
        ['Adjusted odds ratio, payment user', '3.45 (2.24 to 5.30)'],
        ['Sent money, lock vs no lock (n = 219)', '25.0% vs 8.9%'],
        ['Largest payment-minus-lock gap', 'Ages 60+: +33.7 points'],
        ['Group-level rank correlation, payment use vs exposure', '0.38 (vs lock use: 0.63)'],
        ['Payment-app fraud-keyword reviews about rewards', '50.8% of 118'],
        ['Bank-app fraud-keyword reviews about blocks, charges, grievances', '38.5% of 65'],
        ['Unauthorised-access reviews', 'Payment apps 6 of 5,758 and 2 to 4 of 2,090; bank apps 3 to 4 of 6,240'],
        ['Break-even institutions', '8 steady state; 13 while growing']]
cap = para('TABLE I. KEY RESULTS (SURVEY-WEIGHTED UNLESS STATED)', 'c', 8, True, after=2); cap.paragraph_format.keep_with_next = True
tb = doc.add_table(rows=len(rows), cols=2); tb.style = 'Table Grid'; tb.alignment = WD_TABLE_ALIGNMENT.CENTER; tb.autofit = False
for ci, w in enumerate((1.75, 1.6)):
    tb.columns[ci].width = Inches(w)
for ri, row in enumerate(rows):
    for ci, val in enumerate(row):
        c = tb.cell(ri, ci); c.width = Inches((1.75, 1.6)[ci]); c.text = ''
        pp = c.paragraphs[0]; pp.paragraph_format.space_after = Pt(0)
        run(pp, val, 8, ri == 0)
        if ri == 0:
            shd = OxmlElement('w:shd'); shd.set(qn('w:val'), 'clear'); shd.set(qn('w:fill'), 'D9D9D9'); c._tc.get_or_add_tcPr().append(shd)
doc.add_paragraph().paragraph_format.space_after = Pt(2)
para("Exposure was highest among tertiary-educated adults (17.9%) and the lowest income quintile (12.5%) and lowest at ages 60+ (4.1%): risk does not rise evenly with inclusion, and older adults' payment use (56.6%) far exceeds their lock use (22.9%). Payment use and lock use were lower for women and for the lowest income quintile (34.8% and 40.6%, against 67.4% and 75.2% in the highest). The payment-user and gender results survive assumed extra design effects of up to three. Of 219 request recipients, 45 reported sending money. India ranked second on account ownership and second lowest on phone ownership among seven economies. The App Store showed the same review pattern as Google Play. Bank-app reviews were about blocked accounts, charges, support and security-friction prompts (SIM binding, biometrics, root checks) rather than rewards. In the five published studies, social engineering, trust and low awareness appeared in all five, and weak support or redress in four. Base-case surplus was -32.80, 0.00 and +52.16 INR lakh over three years.")

heading('IV. DISCUSSION')
para("Ownership overstates inclusion: use and safe use are lower and unevenly distributed. Higher exposure among payment users suggests digital activity makes people reachable; it does not show that payments cause fraud. A device lock protects a handset, not judgement, and the higher share of senders among locked phones rests on only 45 senders. Reviews show where trust breaks down (rewards, refunds, support, verification), while interview studies describe the scams that reviews rarely mention, which is consistent with scam victims seldom writing reviews. Together they support testing an accessible, institution-funded safety service with verified cues and routes to support in a staged pilot {asiaccs,mungara}.")

heading('V. LIMITATIONS')
para("The survey is cross-sectional and self-reported; requests are not verified fraud; intervals are approximate. Reviews are self-selected, coded with AI assistance and checked by a human on 40 reviews only. Interview evidence is secondary. Financial inputs are assumptions, and no pilot or willingness-to-pay evidence exists.")

heading('VI. CONCLUSION')
para("India combines near-universal accounts with lower digital use and uneven device protection. The evidence supports a staged pilot, not a forecast. Next steps are consent-based interviews with merchants, users and budget owners, a pilot with pre-specified outcomes, and design-based estimation if identifiers become available.")

heading('REFERENCES')
for i, k in enumerate(order, 1):
    p = doc.add_paragraph(); p.paragraph_format.left_indent = Inches(0.25); p.paragraph_format.first_line_indent = Inches(-0.25)
    p.paragraph_format.space_after = Pt(1); p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run(p, f'[{i}] {REFS[k]}', 7.5)

# page-number footer
fp = sec.footer.paragraphs[0]; fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = fp.add_run(); r.font.name = FONT; r.font.size = Pt(9)
for typ, txt in (('begin', None), (None, 'PAGE'), ('end', None)):
    if typ:
        e = OxmlElement('w:fldChar'); e.set(qn('w:fldCharType'), typ); r._r.append(e)
    else:
        e = OxmlElement('w:instrText'); e.set(qn('xml:space'), 'preserve'); e.text = txt; r._r.append(e)
doc.core_properties.author = 'Group 31'
doc.core_properties.title = 'Mobile Banking: Financial Inclusion vs Cybersecurity Risks (condensed)'
doc.save(OUT)
print('saved', OUT, '| refs', len(order))

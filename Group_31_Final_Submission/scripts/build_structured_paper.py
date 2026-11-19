# -*- coding: utf-8 -*-
"""Builds the TA-structure version of the Group 31 paper (Times New Roman 12, table labels above, figure labels below).
Run from C:\\Users\\Sudhanshu\\Desktop\\EF :  python Group_31/revised/build_structured_paper.py
All numbers come from the audited weighted results / illustrative finance model already in Group_31/revised."""
import re
from pathlib import Path
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

R = Path('Group_31/revised')
OUT = R / 'Group_31_Research_Paper.docx'
FONT = 'Times New Roman'

# ---------------------------------------------------------------- references
REFS = {
 'fx25': "World Bank. (2025). The Global Findex Database 2025: Connectivity and financial inclusion in the digital economy. https://www.worldbank.org/en/publication/globalfindex/report",
 'fxdata': "Development Research Group, Finance and Private Sector Development Unit, World Bank. (2025). India – The Global Findex Database 2025, 2024 survey (Ref. IND_2024_FINDEX_v02_M) [Microdata]. https://doi.org/10.48529/c9vy-pq51",
 'dash': "World Bank. (n.d.). India: Global snapshot of indicators and enabling regulations [Digital payment definition and published gender aggregates]. https://digitalfinance.worldbank.org/country/india",
 'wbtrust': "World Bank. (n.d.). Trust. In Inclusive digital financial services: A reference guide for policymakers and regulators. https://digitalfinance.worldbank.org/topics/digital-financial-literacy/trust",
 'wbcp': "World Bank. (n.d.). Financial inclusion and consumer protection. Responsible Financial Access. https://responsiblefinance.worldbank.org/en/responsible-finance",
 'rbi': "Reserve Bank of India. (2020, June 22). Increasing instances of payment frauds – Enhancing public awareness campaigns through multiple channels (RBI/2019-20/256). https://www.rbi.org.in/commonman/Upload/English/Notification/PDFs/256CIRCULARE6521761166042728106B78DFA3D78A1.PDF",
 'gpay': "Kenghe, A. (2019, July 31). What's under the hood: Security on Google Pay. Google India Blog (used as a documented example of in-app warnings, not an effectiveness evaluation). https://india.googleblog.com/2019/07/whats-under-hood-security-on-google-pay.html",
 'mha': "Ministry of Home Affairs. (2022, April 6). Cyber Frauds Helpline. Press Information Bureau, Government of India (Release ID 1814120). https://www.pib.gov.in/PressReleasePage.aspx?PRID=1814120",
 'wbblog': "World Bank. (n.d.). Digital technology is unlocking financial inclusion. Development Talk (World Bank Blogs; summary of Global Findex 2025 global and low- and middle-income aggregates). https://blogs.worldbank.org/en/developmenttalk/digital-technology-is-unlocking-financial-inclusion",
 'wdi': "World Bank. (2025). Global Findex Database 2025 country indicators (account.t.d, con1, con18.s, con21.s; 2024) [Data set]. World Bank Data API, source 28. https://api.worldbank.org/v2/country/all/indicator/account.t.d?source=28&date=2024&format=json",
 'npci': "National Payments Corporation of India. (n.d.). UPI live members: List of banks live on UPI (approximately 758 live bank and PPI entries, of which 111 are PSPs and 647 are issuers; snapshot date not stated). https://www.npci.org.in/product/upi/all-members",
 'reviews': "Google Play Store. (2026). Public user reviews of PhonePe, Google Pay, Paytm, BHIM and SBI YONO, India store, 2 October to 19 November 2026 [Data set collected by the authors with the google-play-scraper package; usernames not stored].",
 'suri': "Suri, T., & Jack, W. (2016). The long-run poverty and gender impacts of mobile money. Science, 354(6317), 1288–1292. https://doi.org/10.1126/science.aah5309",
 'jack': "Jack, W., & Suri, T. (2014). Risk sharing and transactions costs: Evidence from Kenya's mobile money revolution. American Economic Review, 104(1), 183–223. https://doi.org/10.1257/aer.104.1.183",
 'aker10': "Aker, J. C., & Mbiti, I. M. (2010). Mobile phones and economic development in Africa. Journal of Economic Perspectives, 24(3), 207–232. https://doi.org/10.1257/jep.24.3.207",
 'dks17': "Demirgüç-Kunt, A., Klapper, L., & Singer, D. (2017). Financial inclusion and inclusive growth: A review of recent empirical evidence (Policy Research Working Paper No. 8040). World Bank. https://doi.org/10.1596/1813-9450-8040",
 'dk12': "Demirgüç-Kunt, A., & Klapper, L. (2012). Measuring financial inclusion: The Global Findex Database (Policy Research Working Paper No. 6025). World Bank. https://doi.org/10.1596/1813-9450-6025",
 'singer15': "Demirgüç-Kunt, A., Klapper, L., Singer, D., & Van Oudheusden, P. (2015). The Global Findex Database 2014: Measuring financial inclusion around the world (Policy Research Working Paper No. 7255). World Bank. https://doi.org/10.1596/1813-9450-7255",
 'fx17': "Demirgüç-Kunt, A., Klapper, L., Singer, D., & Ansar, S. (2018). The Global Findex Database 2017: Measuring financial inclusion and the fintech revolution. World Bank. https://doi.org/10.1596/978-1-4648-1259-0",
 'bdl': "Beck, T., Demirgüç-Kunt, A., & Levine, R. (2004). Finance, inequality, and poverty: Cross-country evidence (NBER Working Paper No. 10979). https://doi.org/10.3386/w10979",
 'lm': "Lusardi, A., & Mitchell, O. S. (2011). Financial literacy around the world: An overview (NBER Working Paper No. 17107). https://doi.org/10.3386/w17107",
 'sarma': "Sarma, M., & Pais, J. (2011). Financial inclusion and development. Journal of International Development, 23(5), 613–628. https://doi.org/10.1002/jid.1698",
 'mns': "Muralidharan, K., Niehaus, P., & Sukhtankar, S. (2016). Building state capacity: Evidence from biometric smartcards in India. American Economic Review, 106(10), 2895–2929. https://doi.org/10.1257/aer.20141346",
 'davis': "Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. MIS Quarterly, 13(3), 319–340. https://doi.org/10.2307/249008",
 'venk': "Venkatesh, V., Morris, M. G., Davis, G. B., & Davis, F. D. (2003). User acceptance of information technology: Toward a unified view. MIS Quarterly, 27(3), 425–478. https://doi.org/10.2307/30036540",
 'arner': "Arner, D. W., Buckley, R. P., Zetzsche, D. A., & Veidt, R. (2020). Sustainability, FinTech and financial inclusion. European Business Organization Law Review, 21(1), 7–35. https://doi.org/10.1007/s40804-020-00183-y",
 'ozili': "Ozili, P. K. (2018). Impact of digital finance on financial inclusion and stability. Borsa Istanbul Review, 18(4), 329–340. https://doi.org/10.1016/j.bir.2017.12.003",
 'anderson08': "Anderson, K. B., Durbin, E., & Salinger, M. A. (2008). Identity theft. Journal of Economic Perspectives, 22(2), 171–192. https://doi.org/10.1257/jep.22.2.171",
 'am06': "Anderson, R., & Moore, T. (2006). The economics of information security. Science, 314(5799), 610–613. https://doi.org/10.1126/science.1130992",
 'adams': "Adams, A., & Sasse, M. A. (1999). Users are not the enemy. Communications of the ACM, 42(12), 40–46. https://doi.org/10.1145/322796.322806",
 'downs': "Downs, J. S., Holbrook, M. B., & Cranor, L. F. (2006). Decision strategies and susceptibility to phishing. In Proceedings of the Second Symposium on Usable Privacy and Security (p. 79). ACM. https://doi.org/10.1145/1143120.1143131",
 'dhamija': "Dhamija, R., Tygar, J. D., & Hearst, M. (2006). Why phishing works. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (pp. 581–590). ACM. https://doi.org/10.1145/1124772.1124861",
 'luarn': "Luarn, P., & Lin, H.-H. (2005). Toward an understanding of the behavioral intention to use mobile banking. Computers in Human Behavior, 21(6), 873–891. https://doi.org/10.1016/j.chb.2004.03.003",
 'gomber': "Gomber, P., Kauffman, R. J., Parker, C., & Weber, B. W. (2018). On the Fintech revolution: Interpreting the forces of innovation, disruption, and transformation in financial services. Journal of Management Information Systems, 35(1), 220–265. https://doi.org/10.1080/07421222.2018.1440766",
 'aker16': "Aker, J. C., Boumnijel, R., McClelland, A., & Tierney, N. (2016). Payment mechanisms and antipoverty programs: Evidence from a mobile money cash transfer experiment in Niger. Economic Development and Cultural Change, 65(1), 1–37. https://doi.org/10.1086/687578",
 'agarwal': "Agarwal, S., Ghosh, P., Li, J., & Ruan, T. (2020). Digital payments and consumption: Evidence from the 2016 demonetization in India. SSRN. https://doi.org/10.2139/ssrn.3641508",
 'bachas': "Bachas, P., Gertler, P., Higgins, S., & Seira, E. (2021). How debit cards enable the poor to save more. Journal of Finance, 76(4), 1913–1957. https://doi.org/10.1111/jofi.13021",
 'button': "Button, M., Nicholls, C. M., Kerr, J., & Owen, R. (2014). Online frauds: Learning from victims why they fall for these scams. Australian & New Zealand Journal of Criminology, 47(3), 391–408. https://doi.org/10.1177/0004865814521224",
 'gl': "Gordon, L. A., & Loeb, M. P. (2002). The economics of information security investment. ACM Transactions on Information and System Security, 5(4), 438–457. https://doi.org/10.1145/581271.581274",
 'banerjee': "Banerjee, A., Duflo, E., Glennerster, R., & Kinnan, C. (2015). The miracle of microfinance? Evidence from a randomized evaluation. American Economic Journal: Applied Economics, 7(1), 22–53. https://doi.org/10.1257/app.20130533",
 'khera': "Khera, P., Ng, S., Ogawa, S., & Sahay, R. (2021). Is digital financial inclusion unlocking growth? (IMF Working Paper No. 2021/167). International Monetary Fund. https://doi.org/10.5089/9781513584669.001",
 'lashitew': "Lashitew, A. A., van Tulder, R., & Liasse, Y. (2019). Mobile phones for financial inclusion: What explains the diffusion of mobile money innovations? Research Policy, 48(5), 1201–1215. https://doi.org/10.1016/j.respol.2018.12.010",
 'kashyap': "Kashyap, A. K., & Wetherilt, A. (2019). Some principles for regulating cyber risk. AEA Papers and Proceedings, 109, 482–487. https://doi.org/10.1257/pandp.20191058",
 'kopp': "Kopp, E., Kaffenberger, L., & Wilson, C. (2017). Cyber risk, market failures, and financial stability (IMF Working Paper No. 2017/185). International Monetary Fund. https://doi.org/10.5089/9781484313787.001",
 'burke': "Burke, J., Kieffer, C., Mottola, G., & Perez-Arce, F. (2022). Can educational interventions reduce susceptibility to financial fraud? Journal of Economic Behavior & Organization, 198, 250–266. https://doi.org/10.1016/j.jebo.2022.03.028",
 'robinson': "Robinson, J., Park, J., & Blumenstock, J. (2023). The impact of digital credit in developing economies: A review of recent evidence. SSRN. https://doi.org/10.2139/ssrn.4540063",
 'bada': "Bada, M., Sasse, A. M., & Nurse, J. R. C. (2019). Cyber security awareness campaigns: Why do they fail to change behaviour? arXiv:1901.02672. https://arxiv.org/abs/1901.02672",
}
order = []  # keys in order of first citation


def cite(m):
    nums = []
    for k in m.group(1).split(','):
        assert k in REFS, k
        if k not in order:
            order.append(k)
        nums.append(order.index(k) + 1)
    return '[' + ', '.join(str(n) for n in sorted(nums)) + ']'


def cites(text):
    return re.sub(r'\{([a-z0-9_,]+)\}', cite, text)


# ---------------------------------------------------------------- document helpers
doc = Document()
sec = doc.sections[0]
sec.page_width, sec.page_height = Inches(8.5), Inches(11)
for a in ('left_margin', 'right_margin', 'top_margin', 'bottom_margin'):
    setattr(sec, a, Inches(1))


def set_font(style):
    style.font.name = FONT
    style.font.size = Pt(12)
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
        if s.type in (1, 2):  # paragraph / character
            set_font(s)
    except Exception:
        pass
nm = doc.styles['Normal']
nm.paragraph_format.space_after = Pt(6)
nm.paragraph_format.line_spacing = 1.15
for h in ('Heading 1', 'Heading 2', 'Heading 3', 'Title', 'Caption'):
    st = doc.styles[h]
    st.font.size = Pt(12); st.font.bold = True; st.font.italic = False
    st.paragraph_format.space_before = Pt(12 if h != 'Caption' else 4)
    st.paragraph_format.space_after = Pt(6)
    st.paragraph_format.keep_with_next = h != 'Caption'


_ppr = doc.styles['Title'].element.get_or_add_pPr()
for b in _ppr.findall(qn('w:pBdr')):
    _ppr.remove(b)


def add_runs(p, text, size=12, bold=False, italic=False):
    text = cites(text)
    for i, part in enumerate(re.split(r'\*\*(.+?)\*\*', text)):
        if not part:
            continue
        r = p.add_run(part)
        r.font.name = FONT; r.font.size = Pt(size)
        r._element.rPr.rFonts.set(qn('w:eastAsia'), FONT)
        r.bold = bold or (i % 2 == 1)
        r.italic = italic


def P(text, align=None, bold=False, italic=False, after=None, indent=False):
    p = doc.add_paragraph()
    add_runs(p, text, bold=bold, italic=italic)
    if align == 'c':
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    elif align == 'j':
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if after is not None:
        p.paragraph_format.space_after = Pt(after)
    return p


def H1(t): return doc.add_heading(t, level=1)
def H2(t): return doc.add_heading(t, level=2)


T = dict(defs=1, fin=2, adopt=3, lock=4, model=5, send=6, gap=7, unit=8, proj=9, bridge=10, sens=11, peers=12, themes=13, manual=14, canvas=15, alt=16, seed=17, risk=18)
F = dict(gender=1, income=2, exposure=3, surplus=4, peers=5, themes=6)
_t = [0]; _f = [0]


def table(key, title, rows, widths, note=None, bold_first_col=False):
    _t[0] += 1
    assert T[key] == _t[0], (key, _t[0])
    cap = doc.add_paragraph(style='Caption')  # label ABOVE the table
    add_runs(cap, f'Table {T[key]}: {title}', bold=True)
    cap.paragraph_format.keep_with_next = True
    tb = doc.add_table(rows=len(rows), cols=len(rows[0]))
    tb.style = 'Table Grid'
    tb.alignment = WD_TABLE_ALIGNMENT.CENTER
    tb.autofit = False
    for ri, row in enumerate(rows):
        for ci, val in enumerate(row):
            c = tb.cell(ri, ci)
            c.width = Inches(widths[ci])
            p = c.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.0
            add_runs(p, str(val), bold=(ri == 0 or (bold_first_col and ci == 0)))
            if ri == 0:
                tcPr = c._tc.get_or_add_tcPr()
                shd = OxmlElement('w:shd'); shd.set(qn('w:val'), 'clear'); shd.set(qn('w:color'), 'auto'); shd.set(qn('w:fill'), 'D9D9D9')
                tcPr.append(shd)
        trPr = tb.rows[ri]._tr.get_or_add_trPr()
        cs = OxmlElement('w:cantSplit'); trPr.append(cs)
    # repeat header row
    th = OxmlElement('w:tblHeader'); tb.rows[0]._tr.get_or_add_trPr().append(th)
    if note:
        n = P(note, italic=False)
        n.paragraph_format.space_before = Pt(4)
    else:
        doc.add_paragraph().paragraph_format.space_after = Pt(2)


def figure(key, fname, title):
    _f[0] += 1
    assert F[key] == _f[0]
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.keep_with_next = True
    p.add_run().add_picture(str(R / 'figures' / fname), width=Inches(5.6))
    cap = doc.add_paragraph(style='Caption')  # label BELOW the figure
    add_runs(cap, f'Figure {F[key]}: {title}', bold=True)
    cap.paragraph_format.space_after = Pt(10)


# footer page number
fp = sec.footer.paragraphs[0]; fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = fp.add_run(); r.font.name = FONT; r.font.size = Pt(12)
for typ, txt in (('begin', None), (None, 'PAGE'), ('end', None)):
    if typ:
        e = OxmlElement('w:fldChar'); e.set(qn('w:fldCharType'), typ); r._r.append(e)
    else:
        e = OxmlElement('w:instrText'); e.set(qn('xml:space'), 'preserve'); e.text = txt; r._r.append(e)

# ================================================================= TITLE BLOCK
tp = doc.add_paragraph(style='Title'); tp.alignment = WD_ALIGN_PARAGRAPH.CENTER
add_runs(tp, 'Mobile Banking, Financial Inclusion and Cybersecurity Risk in India: A Survey-Weighted Analysis of the 2024 Global Findex and an Institutional Payment-Safety Service Proposal', bold=True)
P('Rushal Verma, Vichanshu Raj and Sudhanshu', align='c', after=0)
P('Group 31, Entrepreneurial Finance', align='c', after=0)
P('20 November 2026', align='c')

# ================================================================= ABSTRACT
H1('Abstract')
ABSTRACT = ("This study examines how financial inclusion, digital payment use and reported cybersecurity exposure relate to one another in India, "
 "and what this implies for entrepreneurs who serve first-time digital users. We analyse the 2024 India Global Findex survey of 3,000 adults using survey weights and an exploratory logistic model, "
 "compare India with peer economies, review 35 academic papers and several institutional sources, and code 5,758 public reviews of five payment apps. "
 "Account ownership was 89.0%, but only 48.5% made or received a digital payment, and 57.7% of phone owners reported a device lock. "
 "Unsolicited money requests were reported by 13.1% of payment-using phone owners and 4.3% of non-users (adjusted odds ratio 3.45). "
 "App reviews rarely described third-party fraud; complaints centred on unpaid rewards, failed payments and weak support. "
 "An illustrative financial model for a bank-sold safety service breaks even at eight paying institutions under stated assumptions. "
 "The data cannot show causation or verified losses, and the commercial assumptions need pilot validation.")
P(ABSTRACT, align='j')
wc = len(ABSTRACT.split())
assert 150 <= wc <= 200, wc
P('**Keywords:** financial inclusion; mobile banking; digital payments; cybersecurity; fraud exposure; Global Findex; entrepreneurial finance; India')

# ================================================================= 1 INTRODUCTION
H1('1. Introduction')
H2('1.1 Background')
P("Access to formal finance is widely linked with household resilience, enterprise formation and poverty reduction {dks17,suri}. Over the past decade, mobile phones and digital payment networks have changed how that access is delivered, "
  "allowing people to pay, save and transfer money without visiting a branch {aker10,gomber}. India is a prominent example: its public digital identity and payment infrastructure have been studied for effects on service delivery and household consumption {mns,agarwal}. "
  "For a small business owner or a first-time digital customer, a bank account is useful only if it can be used reliably to receive sales proceeds, pay suppliers and manage cash, and only if it can be used without undue risk.", align='j')
P("Three terms are used throughout. Financial inclusion is the use of formal financial services. Account ownership measures access, whereas digital payment use measures activity. Reported cybersecurity exposure, in this study, means a person's report of an unsolicited call or message asking for money; it is a measure of exposure to a possible scam attempt, not verified fraud. "
  "The World Bank's Global Findex is the most widely used cross-country source for the first two measures {dk12,fx17,fx25}.", align='j')
H2('1.2 Problem statement and importance')
P("Account ownership, active digital use and safe digital use are different dimensions of inclusion. A population that holds accounts but uses them little, or uses them without basic safeguards, can be left exposed even as headline inclusion rises. "
  "Evidence from fraud and phishing research shows that deception exploits ordinary behaviour rather than ignorance alone {dhamija,button}, so the risk grows as new, less experienced users enter digital channels. "
  "For entrepreneurs and financial institutions the issue is practical: perceived credibility and trust influence whether customers adopt mobile banking {luarn}, and digital finance brings benefits alongside unresolved issues {ozili}.", align='j')
H2('1.3 Research gap')
P("The existing literature is strong on the economic benefits of mobile money and on the behavioural causes of phishing, but the two strands are rarely joined in a single, recent, nationally broad survey of India. "
  "Studies of digital inclusion seldom report device-level safeguards or reported scam exposure, and security research seldom reports representative adoption patterns by gender, age and income. "
  "Little work also translates such respondent-level patterns into an entrepreneurial finance question: what service could be built, who would pay for it, and what financial conditions would make it viable. This paper addresses these gaps with the 2024 India Global Findex microdata and a transparent, assumption-labelled venture model.", align='j')
H2('1.4 Research questions')
P("**RQ1.** How do account ownership, digital payment use and device protection differ across women and men, age groups and income quintiles in India, and how does India compare with peer economies?", after=2)
P("**RQ2.** Are digital payment users more likely than non-users to report unsolicited money requests, after adjusting for demographic and economic characteristics?", after=2)
P("**RQ3.** Among people who report an unsolicited money request, is having a device lock associated with a lower share reporting that they sent money?", after=2)
P("**RQ4.** Which groups show the largest gap between digital payment use and device protection?", after=2)
P("**RQ5.** What do public app reviews and institutional documents reveal about fraud-related grievances, security friction and support experiences?", after=2)
P("**RQ6.** What financial conditions (price, costs and customer numbers) would allow an institution-funded payment-safety service to break even, and how sensitive is that result to its assumptions?")

# ================================================================= 2 LITERATURE REVIEW
H1('2. Literature review')
P("This review covers the economics of financial inclusion and mobile money, technology adoption and trust in mobile banking, security behaviour and fraud, the economics of cyber risk, and the entrepreneurial and policy literature on digital financial services. "
  "It follows the history of the field, compares findings across sources and ends by identifying the gap this study fills. It draws on 35 academic and policy sources; institutional documents used for context are cited in Sections 3 to 5.", align='j')

H2('2.1 Financial inclusion, development and measurement')
P("Cross-country work established that deeper finance disproportionately raises the incomes of the poorest and reduces inequality {bdl}, and later reviews found that account access supports inclusive growth, although the effects depend on how accounts are used {dks17}. "
  "Measurement advanced with the first Global Findex in 2011 {dk12} and its repeated rounds {singer15,fx17,fx25}, which separated account ownership from usage. "
  "Index-based studies had earlier ranked countries on banking penetration, availability and usage and associated inclusion with income, literacy, urbanisation and infrastructure {sarma}. "
  "Financial illiteracy is widespread across the countries studied {lm}. Taken together, these sources justify treating ownership and use as separate outcomes, which this study does.", align='j')

H2('2.2 Mobile money, digital payments and development outcomes')
P("The best-known causal evidence comes from Kenya. M-PESA helped households share risk and sustain consumption after shocks {jack}, and long-run analysis found that mobile money access lifted around 2% of households out of poverty, with larger effects among female-headed households through occupational shifts into business {suri}. "
  "More broadly, mobile phones reduce search and coordination costs and improve market information in low-income settings {aker10}. "
  "A cash-transfer experiment in Niger found that mobile transfers improved household dietary diversity, partly through time savings relative to manual distribution {aker16}, and debit cards for Mexican cash-transfer recipients raised savings, partly by reducing transaction costs {bachas}. "
  "Cross-country work explains differences in mobile-money diffusion by institutional context {lashitew}, and macro evidence links digital financial inclusion with economic growth {khera}. "
  "In India, biometric identity-based payments reduced leakage in a large public programme {mns}, and the 2016 demonetisation has been used to study how digital payments affect consumption {agarwal}. "
  "Not every financial innovation delivers large gains, however: a randomised evaluation of microcredit in Hyderabad found higher business investment but no significant average gain in consumption, health or education {banerjee}, and a review of digital credit highlights both promise and risk {robinson}. "
  "The comparison shows that benefits arise when services are actually used, which again motivates measuring use rather than ownership alone.", align='j')

H2('2.3 Technology adoption, trust and fintech')
P("The technology acceptance model explains adoption through perceived usefulness and ease of use {davis}, and the unified theory extended it with social influence and facilitating conditions {venk}. "
  "For mobile banking specifically, credibility, self-efficacy and cost shape intention to use {luarn}. Fintech research frames digital finance as a force that changes industry structure and user expectations {gomber}, "
  "and legal and policy scholarship argues that fintech is a key driver of financial inclusion and sustainable development, supported by digital identity and interoperable payment infrastructure {arner}. "
  "Digital finance has benefits for users, providers and governments, but persistent issues must be addressed for it to work well {ozili}. Together, these sources imply that safety and perceived trust are conditions for continued use, not optional extras.", align='j')

H2('2.4 Security behaviour, phishing and fraud victimisation')
P("Usable-security research argues that users reject protections that conflict with their tasks, and that blaming users is unproductive {adams}. "
  "Experiments show that well-designed fraudulent websites deceive many participants {dhamija} and interviews with non-expert users show that awareness of phishing risk is not linked to perceived vulnerability, so people manage familiar risks but not unfamiliar ones {downs}. "
  "Interviews and focus groups with online-fraud victims find that victims are diverse and that scams exploit authority, small sums, pressure and trust {button}. Identity-theft research discusses the prevalence and cost of victimisation and the institutional setting that makes it possible {anderson08}. "
  "Awareness campaigns often fail to change behaviour unless they are designed around how people act {bada}, although a survey experiment with a representative sample of U.S. adults found that short online educational interventions reduced susceptibility to financial fraud, with effects persisting for at least three months only if a reminder was provided {burke}. "
  "This literature supports testing practical, accessible guidance rather than assuming that general advice protects customers.", align='j')

H2('2.5 Cyber risk, incentives and policy')
P("Information-security economics explains why security is often under-provided: incentives, externalities and information asymmetries separate those who bear losses from those who can prevent them {am06}. "
  "Economic models of security investment show that optimal spending depends on vulnerability and potential loss, and need not target the most vulnerable assets {gl}. Financial-sector studies treat cyber risk as a source of market failure and potential instability {kopp}, and propose principles for regulating it {kashyap}. "
  "These sources motivate a shared-responsibility view in which institutions, regulators and users all contribute to safe digital finance.", align='j')

H2('2.6 Synthesis and research gap')
P("Three conclusions emerge. First, inclusion benefits depend on use, not just ownership {suri,dks17,jack}. Second, adoption depends on trust, and security failures exploit ordinary behaviour {luarn,dhamija,button}. Third, security is a shared responsibility that markets alone under-supply {am06,kopp}. "
  "What is missing is a recent national survey view that places adoption, device protection and reported scam exposure side by side for India and connects the pattern to an entrepreneurial offering and its financial viability. "
  "This study addresses that gap: it estimates the respondent-level patterns, and then evaluates a proposed institution-funded service using explicit, testable assumptions.", align='j')

# ================================================================= 3 METHODOLOGY
H1('3. Methodology')
P("The study combines a secondary analysis of survey microdata with a focused review of institutional documents and a scenario-based financial model. "
  "A quantitative, observational design was chosen because the research questions concern the distribution of, and association between, adoption and reported exposure in a national population; "
  "an experiment or interview study was not feasible within a term project. Each choice is justified below.", align='j')

H2('3.1 Research design')
P("The design is cross-sectional, observational and descriptive-analytical. It has five components: (i) weighted descriptive statistics and subgroup comparisons for RQ1; (ii) an exploratory weighted logistic regression for RQ2 and a weighted comparison of sending money by lock status for RQ3; (iii) a side-by-side comparison of payment use and device protection by group for RQ4; (iv) a peer-economy comparison of published Findex aggregates and a qualitative analysis of documents and public app reviews for RQ1 and RQ5; and (v) a deterministic, assumption-based financial model with scenarios and sensitivity analysis for RQ6. "
  "**Justification:** a population survey is the only available source that records adoption and exposure for the same adults; scenario modelling is the standard way to test the viability of a venture before any commercial data exist.", align='j')

H2('3.2 Sampling method and participants')
P("The study uses the India file of the Global Findex Database 2025 (survey conducted in 2024, version IND_2024_FINDEX_v02_M) {fxdata,fx25}. The file contains 3,000 respondents aged 15 or older and 199 variables. "
  "Respondents were sampled by the World Bank and Gallup as a nationally representative adult sample; we did not draw or recruit participants. The supplied positive survey weight (wgt) corrects for sampling and non-response, and all percentages in this paper are weighted. "
  "Sample sizes and counts of positive responses are unweighted. The data describe individuals, not a representative sample of businesses. "
  "**Justification:** the survey is the standard, publicly available benchmark for financial inclusion and is the only source that links payments to phone-safety items in India.", align='j')

H2('3.3 Data collection methods')
P("Four data sources were used. (1) **Survey microdata.** The India microdata were downloaded from the World Bank microdata library on 4 November 2026 under its access conditions {fxdata}. "
  "(2) **Peer-economy aggregates.** Published Global Findex 2025 country values for 2024 (account ownership, mobile phone ownership, phone lock and unsolicited money requests) were retrieved from the World Bank open data API for India, China, Indonesia, Bangladesh, Pakistan, Brazil, South Africa, South Asia, lower-middle-income economies and the world {wdi}; the script fetch_data.py reproduces the download. "
  "(3) **Public app reviews.** The newest English-language reviews in the India Google Play store for PhonePe, Google Pay, Paytm, BHIM and SBI YONO were collected with the google-play-scraper package (up to 3,000 per app; 15,000 retrieved) {reviews}. Only app, date, rating and text were stored; usernames were not, and email addresses and phone numbers in text were masked. "
  "Reviews shorter than 15 characters and duplicates were removed, leaving 5,758 reviews posted between 2 October and 19 November 2026. "
  "(4) **Institutional documents.** Three documents were selected for relevance to trust, shared responsibility and fraud awareness: the World Bank's discussion of trust {wbtrust}, its responsible financial access overview {wbcp} and the Reserve Bank of India's awareness circular {rbi}. "
  "A documented in-app warning feature {gpay}, the national cyber-fraud helpline {mha}, published global aggregates {wbblog} and the NPCI list of live UPI members {npci} were used only for context. "
  "No interviews, focus groups or surveys of our own were conducted. **Justification:** public microdata and open APIs permit transparent reproduction, and public reviews give unprompted user language that the Findex questionnaire cannot provide.", align='j')

H2('3.4 Materials and instruments')
P("Analysis used Python (pandas and numpy for weighted calculations and the logistic model, matplotlib for figures) and python-docx for document production. "
  "The analysis script, a full-precision audit file and the illustrative finance script are included with the submission for reproducibility. Table " + str(T['defs']) + " lists the survey variables.", align='j')
table('defs', 'Survey measures, coding and eligible denominators', [
    ['Measure', 'Variable and coding', 'Denominator'],
    ['Account ownership', 'account = 1', 'All 3,000 adults'],
    ['Made or received a digital payment', 'anydigpayment = 1 (past year)', 'All 3,000 adults'],
    ['Phone ownership', 'con1 = 1', 'All 3,000 adults'],
    ['Phone has a PIN, password or fingerprint lock', 'con18 = 1', '2,141 phone owners with yes/no answers (4 uncertain excluded)'],
    ['Unsolicited money request', 'con21 = 1 (past 12 months)', '2,145 phone owners'],
    ['Sent money after a request', 'con22 = 1', '219 respondents reporting a request'],
], [2.2, 1.9, 2.4], note="Source: authors' definitions based on {fxdata}. For account and anydigpayment, the World Bank's derived zero category includes no, do not know and refusal; for raw connectivity items only yes/no codes are retained.")

H2('3.5 Data analysis')
P("**Descriptive analysis.** A weighted share is 100 × (sum of weights of positive responses) / (sum of weights of eligible valid responses). Each subgroup is recalculated with its own eligible denominator, and percentages and percentage-point gaps are rounded independently from full precision, so a gap can differ by 0.1 point from subtracting rounded values. "
  "**Adoption-protection comparison (RQ4).** For each group we place the weighted digital-payment share (all adults in the group) beside the weighted device-lock share (phone owners in the group) and report their difference in percentage points. The two shares use different denominators, so the difference is descriptive and is not a statistical test. The World Bank dashboard indicator for women (36%) and men (54%) measures making specified digital payments {dash}, whereas the microdata indicator used here covers making or receiving digital payments; the two are different measures and are not mixed.", align='j')
P("**Exploratory logistic model.** The outcome is con21 (unsolicited request) among phone owners. Predictors are digital payment use, gender, age (per ten years), education, income quintile, workforce status and urban residence; age and income enter linearly. All 2,145 eligible observations have complete inputs. "
  "The model is estimated by weighted maximum likelihood with an independent-observation sandwich covariance. The public file lacks strata and primary sampling unit identifiers, so the reported intervals are approximate and not design-based.", align='j')
P("**Peer comparison.** Published aggregates are set beside our India estimates without statistical testing, because sampling errors and country microdata are not available. India's unsolicited-request share is not published in the API, so the value from our microdata (9.4%) is used and marked.", align='j')
P("**Qualitative analysis.** Two qualitative sources were analysed. First, passages in the three institutional documents {wbtrust,wbcp,rbi} on adoption barriers, protection mechanisms and responsibilities were extracted and grouped into themes. "
  "Second, the 5,758 app reviews were coded in two steps. A dictionary of regular expressions flagged five themes (fraud, scam or unauthorised transactions; money deducted or failed payment; support and complaint handling; account blocking, verification or login barriers; safety and trust language), and a review could carry several themes. "
  "Because keyword matches can mislead, all 118 reviews that matched the fraud keywords were then read in full and assigned to one of seven manually defined categories. A further dictionary counted reviews describing device-lock or security-alert prompts. "
  "The first pass was done by a single coder. To check consistency, all 118 reviews were then re-classified in a second pass made without sight of the first labels; the two passes agreed on 112 of 118 reviews (94.9%; Cohen's kappa 0.93), and the six disagreements did not change the unauthorised-access total (6 in both passes) or the reward and cashback total (60 against 59). Both passes were AI-assisted and no independent human rater was used, so this shows consistency of the coding rules, not external validity. The full classification and the second-pass labels are supplied so that they can be audited. Review text is treated as unprompted user opinion, not as verified evidence of fraud.", align='j')
P("**Financial model.** The financial model is deterministic and illustrative. No input is estimated from Findex. Amounts are in INR lakh (1 lakh = INR 100,000). Table " + str(T['fin']) + " lists the base assumptions. "
  "Three scenarios (conservative, base, optimistic) assume zero starting institutions, linear growth within each year, no churn and constant scenario pricing of INR 40,000, 50,000 and 60,000 per month. "
  "Annual revenue = 12 × average institutions × monthly fee. Annual cost = fixed cost + 12 × average institutions × monthly variable cost + new institutions × acquisition cost. Fixed cost grows 20% per year. Tax, interest, depreciation and prelaunch spending are excluded from operating results.", align='j')
table('fin', 'Base financial assumptions (illustrative, not survey findings)', [
    ['Input', 'Assumption', 'Treatment in the model'],
    ['Monthly subscription per institution', 'INR 50,000', 'Recurring revenue; no setup fee'],
    ['Monthly variable delivery cost per institution', 'INR 10,000', 'Hosting, messaging, incremental support'],
    ['Acquisition cost per new institution', 'INR 2 lakh', 'Sales, demonstration, onboarding; expensed when acquired'],
    ['Product and engineering team', 'INR 1.70 lakh per month', 'Fixed operating cost'],
    ['Content and localisation maintenance', 'INR 0.40 lakh per month', 'Fixed operating cost'],
    ['Quality and security oversight', 'INR 0.35 lakh per month', 'Fixed operating cost'],
    ['Administration and core tools', 'INR 0.55 lakh per month', 'Fixed operating cost'],
    ['Total fixed cost, Year 1', 'INR 3.00 lakh per month', 'INR 36 lakh per year; grows 20% annually'],
], [2.4, 1.7, 2.4], note="Source: authors' planning assumptions to be validated with budget-owning institutions.")
P("**Justification:** weighting is required for population statements; an adjusted model separates payment use from demographic differences; and scenario plus sensitivity analysis shows which assumptions drive viability while avoiding false precision.", align='j')

H2('3.6 Ethical considerations')
P("The study uses de-identified, publicly released microdata under the World Bank's access terms; no attempt was made to identify respondents, and no personal data were collected. Raw data are not redistributed with this paper. "
  "App reviews are public; no usernames were stored, and short quotations are anonymous. Responses on unsolicited requests are described as reports, not verified fraud, and the model is not presented as a customer risk score or as grounds for price discrimination. The commercial figures are labelled illustrative, and no partner, investor or willingness-to-pay is claimed. "
  "Any future interviews or pilots would require informed consent and review, and would not collect account credentials.", align='j')
P("**Justification summary:** each method links to a research question: weighted descriptives (RQ1 and RQ4), adjusted association (RQ2), lock-status comparison (RQ3), review coding (RQ5), scenario and sensitivity modelling (RQ6), with ethics and limits stated so that conclusions stay within what the data can support.", align='j')

# ================================================================= 4 RESULTS
H1('4. Results')
P("All percentages are survey-weighted. Counts and valid n are unweighted. This section reports findings without interpretation.", align='j')

H2('4.1 Adoption and exposure')
P("Account ownership was 89.0% and digital payment use was 48.5% among all 3,000 adults; the difference is 40.6 percentage points. Phone ownership was 66.5%. Digital payment use was 42.7% for women and 54.1% for men, a gap of 11.5 percentage points. "
  "Among phone owners, 9.4% reported an unsolicited money request: 13.1% of payment users and 4.3% of non-users. Of 219 request recipients, 21.0% reported sending money (Table " + str(T['adopt']) + ", Figure " + str(F['gender']) + ").", align='j')
table('adopt', 'Adoption and exposure indicators (weighted)', [
    ['Indicator', 'Group', 'Positive count', 'Valid n', 'Weighted share'],
    ['Account ownership', 'All adults', '2,710', '3,000', '89.0%'],
    ['Digital payment', 'All adults', '1,539', '3,000', '48.5%'],
    ['Phone ownership', 'All adults', '2,145', '3,000', '66.5%'],
    ['Digital payment', 'Women', '679', '1,526', '42.7%'],
    ['Digital payment', 'Men', '860', '1,474', '54.1%'],
    ['Unsolicited request', 'All phone owners', '219', '2,145', '9.4%'],
    ['Unsolicited request', 'Phone-owning payment users', '173', '1,283', '13.1%'],
    ['Unsolicited request', 'Phone-owning non-users', '46', '862', '4.3%'],
    ['Sent money', 'Request recipients', '45', '219', '21.0%'],
], [1.6, 1.9, 1.0, 0.8, 1.2], note="Source: authors' calculations from {fxdata}. The positive count is not the numerator of the weighted share. 'Unsolicited request' means an unknown call or message asking for money.")
figure('gender', 'figure1.png', "Gender differences in financial access and use (survey-weighted; women n = 1,526, men n = 1,474). Source: authors' calculations from {fxdata}.")

P("Published Global Findex 2025 aggregates, reported by the World Bank, were 79% of adults with an account worldwide and 75% in low- and middle-income economies, and 61% of adults in low- and middle-income economies making or receiving a digital payment {wbblog}. "
  "Our India estimates were 89.0% for account ownership and 48.5% for making or receiving a digital payment: 10 percentage points above the worldwide account rate, 14 points above the low- and middle-income rate, and 12.5 points below the low- and middle-income digital-payment rate.", align='j')
H2('4.2 Device protection across groups')
P("Of phone owners with valid responses, 57.7% reported a device lock. The share was 50.3% for women and 62.7% for men; 67.4% for payment users and 44.6% for non-users; 75.7% at ages 15–24 and 22.9% at ages 60 and above; and 40.6% in the lowest income quintile and 75.2% in the highest (Table " + str(T['lock']) + ", Figure " + str(F['income']) + ").", align='j')
table('lock', 'Device-lock use among phone owners with valid responses', [
    ['Group', 'Lock yes (count)', 'Valid n', 'Weighted share'],
    ['All phone owners', '1,321', '2,141', '57.7%'],
    ['Women', '505', '919', '50.3%'],
    ['Men', '816', '1,222', '62.7%'],
    ['Digital-payment users', '905', '1,282', '67.4%'],
    ['Digital-payment non-users', '416', '859', '44.6%'],
    ['Age 15–24', '385', '497', '75.7%'],
    ['Age 25–39', '591', '893', '62.7%'],
    ['Age 40–59', '307', '597', '43.6%'],
    ['Age 60+', '38', '154', '22.9%'],
    ['Lowest income quintile', '135', '298', '40.6%'],
    ['Highest income quintile', '473', '623', '75.2%'],
], [2.4, 1.4, 1.2, 1.5], note="Source: authors' calculations from {fxdata}. Each row has its own valid denominator; four phone owners with uncertain responses are excluded. Rows overlap and must not be added.")
figure('income', 'figure2.png', "Income differences in payment use and device protection (survey-weighted; payment use: lowest quintile n = 515, highest n = 712; lock use: lowest n = 298, highest n = 623). Source: authors' calculations from {fxdata}.")

H2('4.3 Adjusted association with request exposure')
P("The unadjusted difference in reported requests between payment users and non-users was 8.8 percentage points (Figure " + str(F['exposure']) + "). In the adjusted model (2,145 phone owners; 219 positive outcomes), the odds ratio for payment users versus non-users was 3.45 (approximate 95% interval 2.24 to 5.30) and for women versus men 0.47 (0.32 to 0.69). "
  "Tertiary versus primary education or less had an odds ratio of 1.70 (1.03 to 2.80). Age, income, workforce status and urban residence had intervals that included 1.00 (Table " + str(T['model']) + ").", align='j')
table('model', 'Exploratory weighted logistic model for unsolicited money requests', [
    ['Predictor and comparison', 'Adjusted odds ratio', 'Approximate 95% interval'],
    ['Payment user versus non-user', '3.45', '2.24 to 5.30'],
    ['Woman versus man', '0.47', '0.32 to 0.69'],
    ['Age per 10-year increase', '0.92', '0.82 to 1.04'],
    ['Secondary versus primary or less', '0.84', '0.56 to 1.25'],
    ['Tertiary versus primary or less', '1.70', '1.03 to 2.80'],
    ['Income quintile, per one-step increase', '0.91', '0.79 to 1.03'],
    ['In workforce versus out', '0.89', '0.61 to 1.32'],
    ['Urban versus rural', '0.91', '0.63 to 1.30'],
    ['Intercept (baseline parameter)', '0.12', '0.06 to 0.24'],
], [3.0, 1.6, 1.9], note="Source: authors' calculations from {fxdata}. Outcome: con21 = 1. Robust intervals assume independent respondents and do not reflect the full clustered, stratified design; no design-based significance is claimed.")
figure('exposure', 'figure3.png', "Unsolicited money requests by digital-payment use among phone owners (survey-weighted; users 173 of 1,283, non-users 46 of 862). Source: authors' calculations from {fxdata}.")

H2('4.4 Sending money by device-lock status')
P("For RQ3: among 219 request recipients, 25.0% of those whose phone had a lock (39 of 170) and 8.9% of those without (6 of 49) reported sending money (Table " + str(T['send']) + ").", align='j')
table('send', 'Sending money among respondents who reported a request', [
    ['Lock status among request recipients', 'Sent money (count)', 'Valid n', 'Weighted share'],
    ['Phone has a lock', '39', '170', '25.0%'],
    ['Phone has no lock', '6', '49', '8.9%'],
    ['All request recipients', '45', '219', '21.0%'],
], [2.6, 1.5, 1.0, 1.4], note="Source: authors' calculations from {fxdata}. The two groups partition the 219 request recipients.")

H2('4.5 Digital payment use and device protection by group')
P("Table " + str(T['gap']) + " places each group's payment-use share beside its device-lock share. The largest positive difference (payment use above lock use) was for ages 60 and above, at 33.7 percentage points (56.6% payment use against 22.9% lock use). "
  "The largest negative difference was for ages 15–24, at −32.1 points (43.5% against 75.7%). For women the difference was −7.6 points and for men −8.5 points. In the lowest income quintile it was −5.8 points and in the highest −7.9 points. At ages 25–39 it was −11.4 points and at ages 40–59 it was 3.0 points.", align='j')
table('gap', 'Digital payment use and device-lock use by group (weighted)', [
    ['Group', 'Payment use (all adults in group)', 'Payment-use n', 'Device lock (phone owners)', 'Lock n', 'Difference (points)'],
    ['Women', '42.7%', '1,526', '50.3%', '919', '−7.6'],
    ['Men', '54.1%', '1,474', '62.7%', '1,222', '−8.5'],
    ['Age 15–24', '43.5%', '722', '75.7%', '497', '−32.1'],
    ['Age 25–39', '51.3%', '1,134', '62.7%', '893', '−11.4'],
    ['Age 40–59', '46.6%', '858', '43.6%', '597', '3.0'],
    ['Age 60+', '56.6%', '286', '22.9%', '154', '33.7'],
    ['Lowest income quintile', '34.8%', '515', '40.6%', '298', '−5.8'],
    ['Highest income quintile', '67.4%', '712', '75.2%', '623', '−7.9'],
], [1.5, 1.1, 0.8, 1.1, 0.7, 1.0], note="Source: authors' calculations from {fxdata}. Difference = payment-use share minus device-lock share, computed from full-precision values and rounded independently. The two shares have different denominators; the difference is descriptive only.")

H2('4.6 Illustrative financial model outputs')
P("All figures in this subsection are calculated from the assumptions in Table " + str(T['fin']) + "; they are not survey results. Base monthly contribution per institution is INR 40,000 (80% margin) and simple acquisition payback is 5 months. "
  "Against the NPCI list of about 758 live UPI bank and PPI entries {npci}, the Year 3 closing institution counts (18, 40 and 65) equal 2.4%, 5.3% and 8.6% of that list. Steady-state break-even is 8 paying institutions, or 13 institutions when one new institution is acquired every month (Table " + str(T['unit']) + ").", align='j')
table('unit', 'Base-case unit economics and break-even', [
    ['Measure', 'Calculation', 'Result'],
    ['Monthly contribution per institution', '50,000 − 10,000', 'INR 40,000'],
    ['Contribution margin', '40,000 / 50,000', '80%'],
    ['Simple acquisition payback', '2 lakh / 0.40 lakh', '5 months'],
    ['Steady-state break-even', '3 lakh / 0.40 lakh = 7.5', '8 institutions'],
    ['Break-even with one new institution monthly', '(3 + 2) lakh / 0.40 lakh = 12.5', '13 institutions'],
], [2.6, 2.2, 1.7], note='Source: authors\' calculations from illustrative assumptions.')
P("Projected annual results for the three scenarios are in Table " + str(T['proj']) + " and Figure " + str(F['surplus']) + ". The base case records a deficit of INR 32.80 lakh in Year 1, a surplus of zero in Year 2 and INR 52.16 lakh in Year 3. "
  "The conservative case records deficits in all three years. The optimistic case records a deficit of INR 24.00 lakh in Year 1 and surpluses of INR 48.80 lakh and INR 173.16 lakh in Years 2 and 3.", align='j')
table('proj', 'Illustrative revenue and operating cost projection (INR lakh)', [
    ['Scenario', 'Year', 'Average institutions', 'Closing institutions', 'Revenue', 'Total cost', 'Surplus / (deficit)'],
    ['Conservative', '1', '2', '4', '9.60', '46.40', '(36.80)'],
    ['', '2', '7', '10', '33.60', '63.60', '(30.00)'],
    ['', '3', '14', '18', '67.20', '84.64', '(17.44)'],
    ['Base', '1', '4', '8', '24.00', '56.80', '(32.80)'],
    ['', '2', '14', '20', '84.00', '84.00', '0.00'],
    ['', '3', '30', '40', '180.00', '127.84', '52.16'],
    ['Optimistic', '1', '6', '12', '43.20', '67.20', '(24.00)'],
    ['', '2', '22', '32', '158.40', '109.60', '48.80'],
    ['', '3', '48.5', '65', '349.20', '176.04', '173.16'],
], [1.1, 0.6, 0.95, 0.95, 0.8, 0.8, 1.0], note="Source: authors' calculations from illustrative assumptions. Brackets denote deficits. Fixed cost is INR 36.00, 43.20 and 51.84 lakh in Years 1–3.")
figure('surplus', 'figure4.png', "Illustrative annual operating surplus or deficit by scenario (INR lakh). Calculated from the assumptions in Tables " + str(T['fin']) + " and " + str(T['proj']) + "; not an empirical result or forecast.")
table('bridge', 'Base-case operating cost components (INR lakh)', [
    ['Cost component', 'Year 1', 'Year 2', 'Year 3'],
    ['New institutions acquired (count)', '8', '12', '20'],
    ['Fixed operating cost', '36.00', '43.20', '51.84'],
    ['Variable delivery cost', '4.80', '16.80', '36.00'],
    ['Acquisition cost', '16.00', '24.00', '40.00'],
    ['Total operating cost', '56.80', '84.00', '127.84'],
], [2.9, 1.2, 1.2, 1.2], note="Source: authors' calculations from illustrative assumptions.")
P("Table " + str(T['sens']) + " reports the minimum number of institutions for steady-state operating break-even for three fees and three variable-cost levels. With a fixed cost of INR 3 lakh per month, the requirement ranges from 6 to 12 institutions. "
  "At a variable cost of INR 10,000, reducing the fee from INR 50,000 to INR 40,000 raises the requirement from 8 to 10. At the base fee, raising variable cost to INR 15,000 raises it to 9. Raising acquisition cost to INR 3 lakh extends simple payback from 5 to 7.5 months and break-even with one new institution monthly to 15 institutions.", align='j')
table('sens', 'Sensitivity of steady-state break-even institution count', [
    ['Monthly variable cost per institution', 'Fee INR 40,000', 'Fee INR 50,000', 'Fee INR 60,000'],
    ['INR 8,000', '10', '8', '6'],
    ['INR 10,000', '10', '8', '6'],
    ['INR 15,000', '12', '9', '7'],
], [2.6, 1.3, 1.3, 1.3], note="Source: authors' calculations. Formula: round up [INR 300,000 / (monthly fee − monthly variable cost)]. All cells use unvalidated assumptions.")

H2('4.7 Peer-economy comparison')
P("Among the seven economies in Table " + str(T['peers']) + ", India's account ownership (89.0%) was the second highest after China (89.4%), and above Brazil (86.4%) and South Africa (81.1%). Its phone ownership (66.5%) was the second lowest, above only Pakistan (62.9%). "
  "The share of phone owners with a lock was 57.6% in India, against 47.5% in Bangladesh, 46.4% in Pakistan, 68.5% in South Africa, 69.1% in Indonesia and 78.0% in Brazil; the lower-middle-income value was 57.1%. "
  "The share of phone owners reporting an unsolicited money request was 9.4% in India (our microdata), against 12.7% in Bangladesh, 13.5% in South Africa, 15.0% for lower-middle-income economies, 18.5% in Indonesia, 18.8% in Pakistan and 32.4% in Brazil (Figure " + str(F['peers']) + "). "
  "China and the world aggregate have no published lock or request values.", align='j')
table('peers', 'India compared with peer economies, 2024 (percent)', [
    ['Economy', 'Account (% adults)', 'Own phone (% adults)', 'Phone lock (% phone owners)', 'Unsolicited money request (% phone owners)'],
    ['India', '89.0', '66.5', '57.6', '9.4†'],
    ['China', '89.4', '96.6', 'n/a', 'n/a'],
    ['Indonesia', '56.3', '80.3', '69.1', '18.5'],
    ['Bangladesh', '43.3', '82.4', '47.5', '12.7'],
    ['Pakistan', '27.3', '62.9', '46.4', '18.8'],
    ['Brazil', '86.4', '92.1', '78.0', '32.4'],
    ['South Africa', '81.1', '87.0', '68.5', '13.5'],
    ['South Asia', '77.6', '67.8', '55.2', 'n/a'],
    ['Lower middle income', '70.4', '75.1', '57.1', '15.0'],
    ['World', '78.7', '85.7', 'n/a', 'n/a'],
], [1.4, 1.0, 1.0, 1.4, 1.7], note="Source: World Bank Global Findex 2025 indicators {wdi}. † India's request share is our weighted microdata estimate (9.4%, n = 2,145), because the API publishes no value; the published India lock share (57.6%) differs slightly from our 57.7%. n/a = not published.")
figure('peers', 'figure5.png', "India compared with peer economies on account ownership, phone ownership, phone lock and unsolicited money requests (2024). Source: {wdi}; India's request share from authors' calculations.")

H2('4.8 Qualitative document review')
P("The review produced three themes. **Trust and support:** the World Bank's discussion of trust links trust with awareness of risks and with timely dispute resolution {wbtrust}. "
  "**Shared responsibility:** the World Bank's responsible financial access overview places consumer protection alongside financial capability {wbcp}. "
  "**Awareness and credential protection:** the Reserve Bank of India's circular calls for public-awareness campaigns through multiple channels and highlights protecting credentials such as OTPs and PINs {rbi}. "
  "None of the documents reports primary data from the respondents in this study, and none evaluates the proposed service.", align='j')

H2('4.9 Public app-review analysis')
P("The cleaned dataset contains 5,758 reviews: BHIM 2,273, SBI YONO 1,656, PhonePe 761, Paytm 591 and Google Pay 477. The mean rating was 2.90. At least one theme matched 18.5% of reviews. "
  "Reviews matching the fraud keywords numbered 118 (2.0%) and had a mean rating of 1.36, against 2.93 for the other reviews. Table " + str(T['themes']) + " and Figure " + str(F['themes']) + " give the five themes.", align='j')
table('themes', 'Keyword themes in 5,758 app reviews', [
    ['Theme', 'Reviews', 'Share of reviews', 'Mean rating', 'One-star share'],
    ['Fraud, scam or unauthorised transactions', '118', '2.0%', '1.36', '85.6%'],
    ['Money deducted or failed payment', '133', '2.3%', '1.44', '82.0%'],
    ['Support and complaint handling', '306', '5.3%', '1.49', '81.4%'],
    ['Account blocking, verification or login barriers', '365', '6.3%', '1.58', '75.1%'],
    ['Safety and trust language', '302', '5.2%', '3.21', '35.8%'],
], [2.5, 0.8, 1.1, 0.9, 1.1], note="Source: authors' keyword coding of {reviews}. A review can match several themes.")
figure('themes', 'figure6.png', "Share of app reviews mentioning each keyword theme. Source: authors' coding of {reviews}.")
P("Of the 118 fraud-keyword reviews, manual reading assigned 60 (50.8%) to rewards, cashback or offers not honoured, 15 (12.7%) to money debited, failed payments or missing refunds, 11 (9.3%) to blocked accounts, mis-selling or poor grievance handling, "
  "10 (8.5%) to spam, permissions, privacy or intrusive security controls, 9 (7.6%) to general accusations without an incident, 7 (5.9%) to praise or no complaint, and 6 (5.1%) to unauthorised access, theft or hacking, reported or feared (Table " + str(T['manual']) + "). "
  "The six reviews of unauthorised access or theft are 0.1% of all 5,758 reviews.", align='j')
table('manual', 'Manual classification of the 118 fraud-keyword reviews', [
    ['Category', 'Reviews', 'Share'],
    ['Reward, cashback or offer not honoured (called scam or fraud)', '60', '50.8%'],
    ['Money debited, payment failed or refund missing', '15', '12.7%'],
    ['Blocked account, mis-selling or poor grievance handling', '11', '9.3%'],
    ['Spam, permissions, privacy or intrusive security controls', '10', '8.5%'],
    ['General accusation, no specific incident', '9', '7.6%'],
    ['Praise or no complaint', '7', '5.9%'],
    ['Unauthorised access, theft or hacking (reported or feared)', '6', '5.1%'],
    ['Total', '118', '100.0%'],
], [4.2, 0.9, 0.9], note="Source: authors' classification of {reviews}; first pass by one coder; blind second pass agreed on 112 of 118 (kappa 0.93), no independent human rater.")
P("A separate dictionary found 104 reviews (1.8%) describing device-lock or security-alert prompts, 86 for BHIM and 18 for SBI YONO, with a mean rating of 1.88. "
  "Typical wording reports the app asking the user to enable a device lock that is already set.", align='j')

# ================================================================= 5 DISCUSSION
H1('5. Discussion')
P("The results answer the research questions as follows. For RQ1, ownership is high (89.0%) but digital use is much lower (48.5%); digital payment use is lower among women and lower-income adults, and device protection is lower among women, older adults and lower-income adults (payment use is highest, not lowest, at ages 60 and above). "
  "This is consistent with the argument that inclusion has to be judged by use and not ownership alone {dks17,fx17}, and with evidence that gender and income gaps persist even where access has expanded {fx17,fx25}. "
  "Relative to published aggregates {wbblog}, India's account ownership is higher than the worldwide and low- and middle-income rates while its digital payment use is lower than the low- and middle-income rate, which suggests that the gap between access and use is wider here than in comparable economies. Against peer economies (Table " + str(T['peers']) + "), India combines near-top account ownership with below-peer phone ownership, a middling lock share and the lowest reported unsolicited-request share among economies with a value, which may reflect lower phone-based contact, differences in recall or reporting, or the smaller share of phone owners. The data cannot separate these explanations. This comparison is indicative only: it sets our weighted sample estimate (n = 3,000) against published aggregates without reflecting sampling uncertainty. The survey cannot say why: lower payment use among women could reflect access to phones, confidence, social norms or the fact that the indicator counts receipts as well as payments.", align='j')
P("For RQ2, payment users reported more unsolicited requests than non-users, and the association remained after adjustment (odds ratio 3.45). One plausible reading is that people who transact digitally are reachable through more channels and are more worthwhile targets {anderson08}. "
  "It does not show that digital payments cause fraud, because phone activity, contact lists and reporting behaviour are unmeasured. The lower odds for women are surprising given their lower digital use; they may reflect fewer contacts or less willingness to report, which the data cannot separate. "
  "The device-lock result is similarly descriptive. A lock restricts physical access to a handset but does not protect against deception, which usable-security research shows works through trust and routine rather than technical failure {adams,dhamija,button}; "
  "for RQ3, the higher share of senders among locked phones in Table " + str(T['send']) + " rests on 45 senders and should not be read as a protective or harmful effect of locking. "
  "For RQ4, the largest mismatch is at the oldest ages, where payment use is relatively high (which may include receiving transfers, since the indicator counts receipts) while device protection is lowest; among the youngest the pattern is reversed. Because the two shares use different denominators, this identifies where to test guidance rather than measuring a precise risk gap. For RQ5, the app reviews show that user grievances are dominated by unpaid rewards (about half of fraud-keyword reviews), failed or unrefunded payments and weak support or account-blocking experiences, while reviews describing unauthorised access or theft are very rare (6 of 5,758). Two readings are plausible: genuine scam victims may not write app-store reviews, or the apps' reviewers focus on service failures. The reviews therefore do not measure scam prevalence, but they do show where trust breaks down (refunds, support and verification), which fits the trust and dispute-resolution themes in the documents {wbtrust}. They also show that safety controls can create friction: 104 reviews describe device-lock or security-alert prompts, mostly for one app, so a lock requirement that cannot be met or recognised can block legitimate use. The document review points the same way: guidance that links trust, dispute resolution, shared responsibility and credential protection supports a service built around understandable advice and verified routes to support {wbtrust,wbcp,rbi}. Its accessibility implication (audio, local-language and assisted channels) is our design inference from the group differences in Section 4, not a reported user preference. For RQ6, the model indicates that viability depends mainly on price, support cost and acquisition efficiency, not on the technical concept, in line with the economics of security investment {gl}.", align='j')

H2('5.1 Academic implications')
P("The study connects two literatures that are usually kept apart: the economics of financial inclusion {suri,jack,dks17} and the behavioural study of scams {dhamija,button,bada}. "
  "It shows that national inclusion statistics can be paired with simple safety indicators to describe where access and safe use diverge, and it clarifies a measurement point that is easy to miss: the make-or-receive payment indicator differs from the dashboard's made-payment indicator {dash}. "
  "Because the public file lacks design variables, the work also illustrates how interval estimates should be labelled exploratory when survey structure is unavailable. "
  "Finally, it suggests that technology-acceptance models {davis,venk,luarn} should include perceived safety and device safeguards as explanatory variables for continued use among new adopters.", align='j')

H2('5.2 Policy implications')
P("Three policy implications follow, each framed as a hypothesis for testing. First, inclusion targets should track active use and safe use, not only account ownership, consistent with the World Bank's linking of trust and consumer protection with capability {wbtrust,wbcp}. "
  "Second, awareness efforts such as those encouraged by the Reserve Bank of India {rbi} should be evaluated on behaviour change and designed for older, lower-income and women users, because generic campaigns often fail to change behaviour and education effects persisted in one experiment only when a reminder was provided {bada,burke}. "
  "Third, shared responsibility implies that providers, regulators and users each carry duties: providers for in-flow warnings and complaint handling, regulators for clear reporting channels such as the national helpline {mha}, and users for credential hygiene {kashyap,kopp}. "
  "The findings do not support differential pricing or profiling of demographic groups.", align='j')

H2('5.3 Managerial implications')
P("For entrepreneurs and institutional managers, the results suggest a narrowly scoped institutional pilot: a multilingual payment-safety companion distributed through banks, payment providers or merchant networks. "
  "The paying customer would be the institution; end users would not pay. The service would offer short audio and visual explanations, a pre-payment checklist and verified routes to the institution's support and official reporting channels. "
  "It would not hold money, authorise payments, guarantee recovery or request credentials such as an OTP or PIN. Table " + str(T['canvas']) + " sets out the business model canvas.", align='j')
table('canvas', 'Proposed business model canvas', [
    ['Canvas element', 'Proposed design and validation need'],
    ['Customer segments', 'Institutional buyers serving first-time digital users and small merchants. End-user pilot priorities: women, older users, people needing assisted access. These are not proven market segments.'],
    ['Value proposition', 'Understandable safety guidance and easier navigation to trusted support. Buyers receive aggregated learning and support-use measures. Fraud reduction and savings must be demonstrated.'],
    ['Channels', 'Partner app or web links, branch and business-correspondent onboarding, merchant-network training; test low-bandwidth audio.'],
    ['Customer relationships', 'Named institutional account contact, staff training, quarterly reviews, agreed service scope.'],
    ['Revenue streams', 'Recurring institutional subscription. No end-user charge, advertising, data sale or transaction commission is assumed.'],
    ['Key activities', 'Content localisation, usability testing, secure integration, link verification, partner onboarding, measurement of comprehension and support use.'],
    ['Key resources', 'Small product team, reusable content library, language reviewers, secure hosting, partner-approved directory of support channels.'],
    ['Key partners', 'Pilot bank or merchant network; language and accessibility specialists; independent security reviewers. Official channels are referral destinations, not assumed partners.'],
    ['Cost structure', 'Fixed product and quality team; variable institution-level delivery cost; customer acquisition; prelaunch development and pilot evaluation.'],
], [1.6, 4.9], bold_first_col=True, note="Source: authors' proposal.")
P("Existing alternatives already cover parts of the problem, so the service must add measurable value (Table " + str(T['alt']) + "). The comparison is a functional review of documented alternatives, not a scored market survey.", align='j')
table('alt', 'Alternatives and proposed differentiation', [
    ['Alternative', 'Established role', 'Additional value to test'],
    ['Bank and RBI awareness campaigns {rbi}', 'Broad education through multiple channels', 'Partner-specific local-language journeys, comprehension checks, follow-up'],
    ['In-app warnings such as Google Pay {gpay}', 'Warnings inside payment flows', 'Practice outside the transaction flow; assisted onboarding. Effectiveness must be tested'],
    ['Bank support and official reporting {mha}', 'Complaint handling; national portal and helpline 1930', 'Help users find verified routes quickly; never duplicate official investigation'],
    ['Institution builds it internally', 'Make-or-buy alternative', 'Reusable localised content must beat the buyer\'s internal cost and quality'],
], [2.0, 2.0, 2.5], note="Source: authors' review of {rbi,gpay,mha}.")
P("**Go-to-market.** A staged plan is proposed. In months 1–2 (discovery and design), secure one sponsor institution and a named budget owner, and conduct consent-based usability sessions using simulated scenarios. In months 3–5 (controlled pilot), compare the companion with existing guidance and prespecify outcomes: comprehension on unseen scenarios, identification of official support, completion and legitimate-task delay. "
  "From month 6 (commercial gate), scale only after a paid commitment, manageable support load and acceptable security review. These are proposed steps; no pilot has been run.", align='j')
P("**Financial interpretation.** Under the stated assumptions, eight institutions cover fixed costs only in steady state, while growth requires about 13 because acquisition is expensed (Table " + str(T['unit']) + "). "
  "Pricing power matters: a 20% lower fee increases the requirement by two institutions, and discounting consumes the margin that funds acquisition (Table " + str(T['sens']) + "). The base case offers no cushion in Year 2, so churn or slow sales would turn it to deficit; "
  "the conservative case does not break even within three years. Revenue is also not cash: procurement and collection delays could create a gap even when operating results improve. "
  "These conclusions follow the logic of security-investment economics and incentive problems {gl,am06}, and they hold only if prices and costs are validated with real buyers.", align='j')
table('seed', 'Illustrative seed budget and use of funds', [
    ['Use of funds', 'INR lakh', 'Purpose'],
    ['Year 1 base operating deficit', '32.80', 'Net operating gap from Table ' + str(T['proj'])],
    ['Prelaunch product and integration', '10.00', 'One-time build before Year 1'],
    ['Prelaunch pilot and evaluation', '5.00', 'User research, testing, independent review'],
    ['Working-capital reserve', '12.00', 'Delayed collections and delivery timing'],
    ['Contingency and runway reserve', '15.20', 'Slower sales, underestimated costs'],
    ['Total seed requirement', '75.00', 'Illustrative planning envelope'],
], [2.6, 1.0, 2.9], note="Source: authors' proposal. Release the INR 15 lakh prelaunch allocation against prototype and pilot milestones. In the conservative case, cumulative operating deficits plus prelaunch costs reach INR 81.80 lakh by the end of Year 2, exceeding the seed amount.")
P("The proposed INR 75 lakh seed would be staged equity or grant support; no funding offer, valuation or dilution is assumed. Table " + str(T['risk']) + " lists the principal venture risks and the evidence needed to address them.", align='j')
table('risk', 'Key venture risks and responses', [
    ['Risk', 'Practical response and evidence required'],
    ['Weak willingness to pay or long procurement', 'Obtain a paid pilot or renewal commitment from a budget owner; stage hiring; track sales-cycle length.'],
    ['Support costs exceed subscription margin', 'Measure delivery hours by institution; negotiate service limits; review variable cost.'],
    ['Incorrect advice or compromised links', 'Partner-approved content, regular link checks, security review, incident-response process.'],
    ['Exclusion or payment friction', 'Test local-language audio and assisted access; measure accessibility failures and legitimate-task delay.'],
    ['Dependence on one partner or easy imitation', 'Reusable integrations; diversify paid relationships; demonstrate quality before claiming advantage.'],
], [2.4, 4.1], note="Source: authors' proposal. No bank, merchant network or investor is represented as an agreed partner; no total addressable market is measured.")

H2('5.4 Future scope and limitations')
P("**Limitations.** The survey is cross-sectional and self-reported, so it cannot establish causation, timing or verified losses. Unsolicited requests are not confirmed fraud, and sending money is not a measured loss amount. "
  "Phone-owner and request-recipient analyses concern subsets of the sample, and subgroup cells such as the 45 senders are small. Intervals are approximate because design variables are missing. The data describe individuals, not enterprises. "
  "The qualitative component rests on a secondary document review and on public app reviews, which are self-selected, cover seven weeks, come from five apps with unequal review counts, are English-language and keyword-coded by a single coder with only an AI-assisted consistency check in place of an independent human second rater, and are not linked to Findex respondents. No interviews or surveys of our own were conducted. Peer values are published aggregates without sampling errors. All financial inputs are unvalidated assumptions with no churn, tax or financing flows.", align='j')
P("**Future scope.** Priority extensions are (i) consent-based interviews with merchants, first-time users and institutional budget owners to test willingness to pay; (ii) design-based estimation if strata and cluster identifiers become available; (iii) pooling Findex rounds {singer15,fx17,fx25} and extending the comparison from published aggregates to country-level microdata for peer economies; "
  "(iv) an evaluated pilot with pre-specified outcomes and a power calculation before treating verified loss as an outcome {burke}; and (v) extending the venture model with churn, taxes, receivable timing and month-by-month cash flow.", align='j')

# ================================================================= 6 CONCLUSION
H1('6. Conclusion')
P("This paper set out to understand how mobile banking inclusion and cybersecurity exposure coexist in India, and what that means for an entrepreneurial response. Using the 2024 India Global Findex, it found that account ownership is widespread (89.0%) but digital payment use (48.5%) and device protection (57.7% of phone owners) are lower and unevenly distributed by gender, age and income. "
  "Payment users reported more unsolicited money requests than non-users (13.1% versus 4.3%), and the association remained after adjustment (odds ratio 3.45). "
  "The literature shows that benefits of digital finance depend on use and trust, and that scams exploit ordinary behaviour; the results are consistent with both ideas, although they do not prove causation.", align='j')
P("For entrepreneurs and institutions, the evidence supports testing an accessible, institution-funded payment-safety service in a staged pilot. An illustrative model reaches steady-state break-even at eight paying institutions and a three-year surplus in the base case, but the result is highly sensitive to price, support cost, acquisition cost and renewal, and it is not evidence of demand. "
  "App reviews added that user grievances concern rewards, refunds, support and verification far more than third-party fraud, and a peer comparison placed India near the top on account ownership but below peers on phone ownership. The contribution of the study is therefore a transparent description of where access and safe use diverge, and a validated-assumption-first path from that pattern to a testable venture. Pilot evidence on willingness to pay, retention and effectiveness is the necessary next step.", align='j')

# ================================================================= REFERENCES
H1('References')
P("Academic references were checked against Crossref bibliographic records on 20 November 2026; institutional web sources were last checked on 7 November 2026. References are numbered in order of first citation.", after=4)
assert len(order) == len(REFS), set(REFS) - set(order)
for i, k in enumerate(order, 1):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.4)
    p.paragraph_format.first_line_indent = Inches(-0.4)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.0
    add_runs(p, f'[{i}] ' + REFS[k])

doc.core_properties.title = 'Mobile Banking, Financial Inclusion and Cybersecurity Risk in India'
doc.core_properties.author = 'Group 31'
doc.save(OUT)
acad = [k for k in order if k not in ('fx25', 'fxdata', 'dash', 'wbtrust', 'wbcp', 'rbi', 'gpay', 'mha')]
print('saved', OUT, '| abstract words', wc, '| refs', len(order), '| academic', len(acad), '| tables', _t[0], '| figures', _f[0])

# -*- coding: utf-8 -*-
"""Presentation for the condensed paper. Run from C:\\Users\\Sudhanshu\\Desktop\\EF :  python Condensed/build_short_deck.py"""
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION, XL_LABEL_POSITION, XL_TICK_LABEL_POSITION

FIG = Path('Group_31_Final_Submission/figures')
OUT = Path('Condensed/Group_31_Presentation_Short.pptx')
NAVY = RGBColor(0x12, 0x2B, 0x45); TEAL = RGBColor(0x1B, 0x8A, 0x7E); BLUE = RGBColor(0x2A, 0x5F, 0xA5)
AMBER = RGBColor(0xD9, 0x8A, 0x1F); RED = RGBColor(0xB8, 0x3B, 0x3B); INK = RGBColor(0x22, 0x2B, 0x36); GREY = RGBColor(0x6B, 0x75, 0x80)
PALE = RGBColor(0xF1, 0xF5, 0xF8); WHITE = RGBColor(255, 255, 255); LIGHT = RGBColor(0xC9, 0xD8, 0xE6)
HEAD = 'Georgia'; BODY = 'Calibri'

prs = Presentation(); prs.slide_width = Inches(13.333); prs.slide_height = Inches(7.5)
blank = prs.slide_layouts[6]
N = [0]


def box(s, x, y, w, h, fill=None, line=None):
    sh = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    if fill is None: sh.fill.background()
    else: sh.fill.solid(); sh.fill.fore_color.rgb = fill
    if line is None: sh.line.fill.background()
    else: sh.line.color.rgb = line; sh.line.width = Pt(1)
    sh.shadow.inherit = False
    return sh


def text(s, x, y, w, h, t, size=16, bold=False, color=INK, font=BODY, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP):
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h)); tf = tb.text_frame; tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = Inches(0.05); tf.margin_top = tf.margin_bottom = Inches(0.03)
    p = tf.paragraphs[0]; p.alignment = align
    r = p.add_run(); r.text = t; r.font.size = Pt(size); r.font.bold = bold; r.font.color.rgb = color; r.font.name = font
    return tb


def bullets(s, x, y, w, h, items, size=16, gap=9):
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h)); tf = tb.text_frame; tf.word_wrap = True
    for i, it in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph(); p.space_after = Pt(gap)
        head, _, rest = it.partition('|')
        if rest:
            r = p.add_run(); r.text = head + ' '; r.font.bold = True; r.font.size = Pt(size); r.font.color.rgb = NAVY; r.font.name = BODY
            r = p.add_run(); r.text = rest; r.font.size = Pt(size); r.font.color.rgb = INK; r.font.name = BODY
        else:
            r = p.add_run(); r.text = '•  ' + it; r.font.size = Pt(size); r.font.color.rgb = INK; r.font.name = BODY
    return tb


def slide(kicker, title, notes):
    s = prs.slides.add_slide(blank); N[0] += 1
    box(s, 0, 0, 13.333, 7.5, WHITE); box(s, 0, 0, 0.18, 7.5, NAVY)
    text(s, 0.6, 0.32, 9, 0.35, kicker.upper(), 12, True, TEAL)
    text(s, 0.6, 0.65, 12.1, 0.9, title, 28, True, NAVY, HEAD)
    text(s, 12.1, 7.02, 0.8, 0.3, str(N[0]), 11, False, GREY, align=PP_ALIGN.RIGHT)
    text(s, 0.6, 7.02, 9, 0.3, 'Group 31  |  Entrepreneurial Finance  |  Mobile banking: financial inclusion vs cybersecurity risks', 10, False, GREY)
    s.notes_slide.notes_text_frame.text = notes
    return s


def stat(s, x, y, w, big, small, color=TEAL, h=1.5):
    box(s, x, y, w, h, PALE); box(s, x, y, 0.08, h, color)
    text(s, x + 0.25, y + 0.1, w - 0.3, 0.75, big, 32, True, color, HEAD)
    text(s, x + 0.25, y + 0.85, w - 0.3, h - 0.85, small, 13, False, INK)


def card(s, x, y, w, h, head, body, color=TEAL, hs=17, bs=14):
    box(s, x, y, w, h, PALE); box(s, x, y, w, 0.07, color)
    text(s, x + 0.2, y + 0.18, w - 0.4, 0.6, head, hs, True, NAVY, HEAD)
    text(s, x + 0.2, y + 0.85, w - 0.4, h - 0.9, body, bs)


def src(s, t):
    text(s, 0.6, 6.68, 12.2, 0.3, t, 10.5, False, GREY)


def style_chart(ch, legend=True, size=12):
    ch.has_title = False
    ch.has_legend = legend
    if legend:
        ch.legend.position = XL_LEGEND_POSITION.BOTTOM; ch.legend.include_in_layout = False; ch.legend.font.size = Pt(size)
    ch.value_axis.has_major_gridlines = False; ch.value_axis.tick_labels.font.size = Pt(size - 1)
    ch.category_axis.tick_labels.font.size = Pt(size)


def colour(series, rgbs):
    for sr, c in zip(series, rgbs):
        sr.format.fill.solid(); sr.format.fill.fore_color.rgb = c


# 1 ---------------------------------------------------------------- title
s = prs.slides.add_slide(blank); N[0] += 1
box(s, 0, 0, 13.333, 7.5, NAVY); box(s, 0.9, 4.35, 2.2, 0.06, TEAL)
text(s, 0.9, 1.3, 11.5, 1.8, 'Mobile Banking: Financial Inclusion vs Cybersecurity Risks in India', 42, True, WHITE, HEAD)
text(s, 0.9, 3.25, 11.5, 1.0, "Evidence from the Global Findex Database 2025 (India survey, fielded in 2024), public app reviews and published interview studies, with implications for entrepreneurs", 20, False, LIGHT)
text(s, 0.9, 4.7, 11.5, 1.2, 'Rushal Verma (IIT2024045)   |   Sudhanshu (IIT2024081)   |   Vichanshu Raj (IIT2024083)', 17, False, WHITE)
text(s, 0.9, 5.25, 11.5, 0.5, 'Group 31  |  Entrepreneurial Finance', 15, False, LIGHT)
s.notes_slide.notes_text_frame.text = "Introduce the question in the title: does the spread of mobile banking in India come with higher cybersecurity risk, and for whom? We combine a national survey, 14,088 app reviews and five published interview studies, and end with a venture proposal."

# 2 ---------------------------------------------------------------- introduction
s = slide('1  Introduction', 'Inclusion brings new users, and new targets',
          'Access, use and safe use are different things. Define: inclusion = use of formal services; digital payment use = activity; exposure = report of an unsolicited call or message asking for money, not verified fraud.')
bullets(s, 0.6, 1.8, 6.4, 4.7, [
    'Background|Mobile phones and digital payments changed how people reach finance; India has public digital identity and payment rails.',
    'Problem|Each new user is also a possible target and may lack the safeguards of experienced users.',
    'Gap|Few national studies show adoption, device safeguards and scam exposure together, and fewer turn the pattern into a venture question.'], 17, 12)
box(s, 7.4, 1.85, 5.3, 4.6, PALE)
text(s, 7.7, 2.0, 4.8, 0.4, 'KEY TERMS', 12, True, TEAL)
bullets(s, 7.7, 2.45, 4.8, 3.9, ['Account ownership|measures access.', 'Digital payment use|made or received a digital payment in the past year.', 'Reported exposure|an unsolicited call or message asking for money. Not verified fraud.'], 15, 12)

# 3 ---------------------------------------------------------------- RQs
s = slide('1  Introduction', 'One central question, six research questions',
          'The central question: where do inclusion and cyber risk move together, where do they not, and what can institutions and entrepreneurs do. RQ1-RQ4 refine the progress report; RQ5 and RQ6 were added for the qualitative and venture parts.')
box(s, 0.6, 1.7, 12.1, 0.75, NAVY)
text(s, 0.85, 1.75, 11.6, 0.65, 'Does more inclusion mean more cybersecurity risk, and for whom?', 20, True, WHITE, HEAD, anchor=MSO_ANCHOR.MIDDLE)
rqs = [('RQ1', 'Differences by gender, age and income; how does India compare with peers?'), ('RQ2', 'Do payment users report more unsolicited money requests, after adjustment?'),
       ('RQ3', 'Is a device lock linked to fewer recipients sending money?'), ('RQ4', 'Which groups show the largest gap between payment use and device protection?'),
       ('RQ5', 'What do app reviews, documents and interview studies reveal about grievances?'), ('RQ6', 'What price, cost and customer numbers make a safety service break even?')]
for i, (k, q) in enumerate(rqs):
    x = 0.6 + (i % 2) * 6.15; y = 2.7 + (i // 2) * 1.3
    box(s, x, y, 0.95, 1.1, TEAL if i < 5 else AMBER); text(s, x, y + 0.3, 0.95, 0.5, k, 18, True, WHITE, HEAD, PP_ALIGN.CENTER)
    box(s, x + 1.0, y, 5.0, 1.1, PALE); text(s, x + 1.15, y + 0.08, 4.75, 0.95, q, 14.5, False, INK, anchor=MSO_ANCHOR.MIDDLE)

# 4 ---------------------------------------------------------------- literature
s = slide('2  Literature review', '35 academic sources, one gap',
          'Four strands: inclusion and mobile money (Suri and Jack, Jack and Suri), adoption and trust (Davis, Luarn and Lin), security behaviour (Dhamija, Button, Bada, Burke), cyber risk economics (Anderson and Moore, Kopp). The gap is a recent national India view that joins them with a venture lens.')
cols = [('Inclusion and mobile money', 'M-PESA helped households share risk and lifted about 2% out of poverty. Benefits arise when services are used, not just owned.'),
        ('Adoption and trust', 'Usefulness, ease, credibility and self-efficacy drive mobile banking use. Safety is a condition for continued use.'),
        ('Security behaviour', 'Phishing exploits routine behaviour; campaigns often fail; short education helps only with reminders.'),
        ('Cyber risk economics', 'Security is under-provided: those who bear losses are not those who can prevent them.')]
for i, (h, b) in enumerate(cols):
    card(s, 0.6 + i * 3.08, 1.8, 2.92, 3.3, h, b, TEAL, 16, 13.5)
box(s, 0.6, 5.4, 12.1, 1.05, NAVY)
text(s, 0.85, 5.45, 11.6, 0.95, 'Gap: no recent national view of India joins adoption, device protection and scam exposure, adds what users say in their own words, and links the pattern to a venture.', 17, True, WHITE, anchor=MSO_ANCHOR.MIDDLE)

# 5 ---------------------------------------------------------------- data
s = slide('3  Methodology', 'Seven public sources, no data of our own',
          'Cross-sectional observational design. Survey is the only source with adoption and exposure for the same adults. Interviews of our own were not feasible, so published studies are secondary evidence. Reviews: names not stored.')
items = [('3,000', 'adults, India survey in Global Findex 2025 (fielded 2024), weighted', TEAL), ('10', 'economies, Findex 2025 country indicators', BLUE),
         ('5,758', 'Google Play reviews, five payment apps', AMBER), ('2,090', 'App Store reviews, same five apps', AMBER),
         ('6,240', 'reviews of eight bank apps, both stores', AMBER), ('5', 'published interview studies (26 to 3,784 participants)', NAVY)]
for i, (big, small, c) in enumerate(items):
    stat(s, 0.6 + (i % 3) * 4.1, 1.75 + (i // 3) * 1.85, 3.9, big, small, c, 1.6)
bullets(s, 0.6, 5.5, 12.1, 1.1, ['Also three institutional documents (World Bank, RBI). Public data only: no interviews, focus groups or surveys of our own. Names, emails and phone numbers are not stored.'], 14.5)

SHOW_RELIABILITY = True  # False hides the 'Analysis and coding reliability' slide
if SHOW_RELIABILITY:
    # 6 ---------------------------------------------------------------- methods detail
    s = slide('3  Methodology', 'Analysis and coding reliability',
              'Weighted shares, logistic model with approximate intervals (no design variables), Fisher test, Spearman across 18 groups. Reviews: keyword dictionaries then every fraud-keyword review read and coded; second passes check consistency. Be explicit: the first pass is a single coder; second passes are blind; only 40 Google Play reviews had a human outside the group; the 122-review second coder is reported blind to labels.')
    bullets(s, 0.6, 1.75, 5.6, 4.9, ['Survey|weighted shares; logistic model with sandwich errors; Kish design-effect check.',
            'Groups|payment use vs lock vs exposure for 18 groups; Spearman rank correlation.',
            'Tests|Fisher exact (lock vs sending money); chi-square with Holm (bank vs payment apps).',
            'Reviews|dictionaries, then every fraud-keyword review read and placed in one of seven categories.',
            'Finance|deterministic scenario model; all inputs are assumptions.'], 15, 10)
    rows = [['Check', 'Reviews', 'Agreement', 'Kappa'], ['AI blind pass, Google Play', '118', '94.9%', '0.93'], ['AI blind pass, App Store', '57', '82.5%', '0.78'], ['AI blind pass, bank apps', '65', '87.7%', '0.84'],
            ['Human coder, Google Play sample', '40', '95.0%', '0.93'], ['Second coder (person, software-aided), App Store + bank', '122', '83.6%', '0.80']]
    tb = s.shapes.add_table(6, 4, Inches(6.5), Inches(1.9), Inches(6.2), Inches(3.4)).table
    for ci, w in enumerate([2.9, 1.0, 1.2, 1.1]): tb.columns[ci].width = Inches(w)
    for r in range(6):
        for c in range(4):
            cell = tb.cell(r, c); cell.text = rows[r][c]; pp = cell.text_frame.paragraphs[0]; pp.alignment = PP_ALIGN.LEFT if c == 0 else PP_ALIGN.CENTER
            pp.runs[0].font.size = Pt(14); pp.runs[0].font.name = BODY; pp.runs[0].font.bold = (r == 0)
            cell.fill.solid(); cell.fill.fore_color.rgb = NAVY if r == 0 else PALE; pp.runs[0].font.color.rgb = WHITE if r == 0 else INK
    text(s, 6.5, 5.45, 6.2, 0.9, 'Agreement is with the first pass (second coder: 102 of 122). First pass is a single coder. The second coder is a person who used software, including AI tools, as an aid but made each decision (as reported by the group).', 12, False, GREY)

# 7 ---------------------------------------------------------------- results: adoption
s = slide('4  Results: access vs active use', 'Access is not the same as active digital use',
          'Account 89.0, phone 66.5, digital payment 48.5: a 40.6-point gap between owning an account and making or receiving a digital payment. Women 42.7 vs men 54.1 (11.5 points). Denominator: all 3,000 adults, survey-weighted. The survey does not show why women use less.')
cd = CategoryChartData(); cd.categories = ['Account ownership', 'Phone ownership', 'Digital payment use']
cd.add_series('Share of adults (%)', (89.0, 66.5, 48.5))
gf = s.shapes.add_chart(XL_CHART_TYPE.BAR_CLUSTERED, Inches(0.6), Inches(1.65), Inches(7.3), Inches(3.3), cd); ch = gf.chart
style_chart(ch, legend=False, size=14); ch.category_axis.reverse_order = True; ch.value_axis.maximum_scale = 100; ch.plots[0].gap_width = 55
pts = ch.plots[0].series[0].points
for k, c in enumerate([TEAL, BLUE, AMBER]):
    pts[k].format.fill.solid(); pts[k].format.fill.fore_color.rgb = c
ch.plots[0].has_data_labels = True; ch.plots[0].data_labels.number_format = '0.0"%"'; ch.plots[0].data_labels.number_format_is_linked = False; ch.plots[0].data_labels.font.size = Pt(16); ch.plots[0].data_labels.font.bold = True
box(s, 0.6, 5.1, 7.3, 1.35, PALE); box(s, 0.6, 5.1, 0.08, 1.35, TEAL)
text(s, 0.85, 5.15, 6.9, 1.25, 'Core finding: 89.0% owned an account, but only 48.5% made or received a digital payment, a 40.6 percentage-point gap (from unrounded results). Phone ownership is 66.5%.', 15, False, INK, anchor=MSO_ANCHOR.MIDDLE)
text(s, 8.3, 1.7, 4.4, 0.4, 'GENDER DIFFERENCE IN DIGITAL PAYMENT USE', 12, True, TEAL)
stat(s, 8.3, 2.15, 2.1, '42.7%', 'women made or received digital payments', TEAL, 1.85)
stat(s, 10.6, 2.15, 2.1, '54.1%', 'men made or received digital payments', BLUE, 1.85)
bullets(s, 8.3, 4.2, 4.4, 2.3, ['Gap|11.5 percentage points in the sample.', 'Caution|the survey does not show whether access, confidence or social factors cause the gap.'], 14, 8)
src(s, 'Account, phone and digital payment shares refer to all 3,000 surveyed adults; survey-weighted. Source: authors\' calculations, India microdata, Global Findex Database 2025 (2024 survey).')

# 7b --------------------------------------------------------------- device lock by group
s = slide('4  Results: device protection', 'Device-lock adoption differs sharply by group',
          'Lock 57.7 overall (n = 2,141 valid phone owners). Age 15-24 75.7, highest income quintile 75.2, men 62.7, women 50.3, lowest income quintile 40.6, ages 60+ 22.9. Subgroups overlap; denominator is phone owners, not all adults. A lock protects a handset, not judgment.')
cd = CategoryChartData(); cd.categories = ['Age 15–24', 'Highest income quintile', 'Men', 'Women', 'Lowest income quintile', 'Age 60+']
cd.add_series('Phone has a lock (% of phone owners)', (75.7, 75.2, 62.7, 50.3, 40.6, 22.9))
gf = s.shapes.add_chart(XL_CHART_TYPE.BAR_CLUSTERED, Inches(0.6), Inches(1.65), Inches(7.6), Inches(4.85), cd); ch = gf.chart
style_chart(ch, legend=False, size=14); ch.category_axis.reverse_order = True; ch.value_axis.maximum_scale = 100; ch.plots[0].gap_width = 50
pts = ch.plots[0].series[0].points
for k, c in enumerate([TEAL, TEAL, BLUE, BLUE, AMBER, AMBER]):
    pts[k].format.fill.solid(); pts[k].format.fill.fore_color.rgb = c
ch.plots[0].has_data_labels = True; ch.plots[0].data_labels.number_format = '0.0"%"'; ch.plots[0].data_labels.number_format_is_linked = False; ch.plots[0].data_labels.font.size = Pt(15); ch.plots[0].data_labels.font.bold = True
stat(s, 8.6, 1.75, 4.1, '57.7%', 'of phone owners with valid responses report a PIN, password or fingerprint lock (n = 2,141)', NAVY, 1.9)
bullets(s, 8.6, 3.9, 4.1, 2.6, ['Age gap|75.7% at ages 15 to 24 vs 22.9% at 60 and above.', 'Careful|subgroups overlap, and lock shares use phone owners as the denominator, not all adults.'], 14, 8)
src(s, 'Survey-weighted, phone owners with valid responses. Source: authors\' calculations, India microdata, Global Findex Database 2025 (2024 survey).')

# 8 ---------------------------------------------------------------- results: exposure
s = slide('4  Results: exposure', 'Payment users report more unsolicited money requests',
          'Users 13.1 vs non-users 4.3. Adjusted odds ratio 3.45 (2.24 to 5.30); women vs men 0.47. Robust to assumed extra design effects up to 3 except tertiary education. 21.0 percent of 219 recipients sent money (45). Lock vs sending: 25.0 vs 8.9, Fisher p = 0.11.')
cd = CategoryChartData(); cd.categories = ['Payment users', 'Non-users']; cd.add_series('Reported an unsolicited money request (%)', (13.1, 4.3))
gf = s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(0.6), Inches(1.7), Inches(5.4), Inches(4.8), cd); ch = gf.chart
style_chart(ch, legend=False, size=14); colour(ch.plots[0].series, [AMBER]); ch.plots[0].gap_width = 70; ch.value_axis.maximum_scale = 16
ch.plots[0].has_data_labels = True; ch.plots[0].data_labels.number_format = '0.0"%"'; ch.plots[0].data_labels.number_format_is_linked = False; ch.plots[0].data_labels.font.size = Pt(16)
stat(s, 6.4, 1.75, 3.0, '3.45', 'adjusted odds ratio, payment users vs non-users (approx. 95% interval 2.24 to 5.30)', AMBER, 1.9)
stat(s, 9.6, 1.75, 3.1, '0.47', 'women vs men (0.32 to 0.69)', BLUE, 1.9)
bullets(s, 6.4, 3.9, 6.3, 2.7, ['Robustness|payment-user and gender results hold at assumed extra design effects up to 3; tertiary education does not.',
        'Lock and sending money|25.0% with a lock vs 8.9% without; Fisher exact p = 0.11 (45 senders).'], 14.5, 10)
src(s, 'Association, not causation. Requests are not verified fraud. Intervals are approximate (no design variables).')

# 9 ---------------------------------------------------------------- inclusion vs risk
s = slide('4  Results: the central question', 'Inclusion and exposure: a weak link across groups',
          'Across 18 groups the rank correlation is 0.38 between payment use and exposure and 0.63 between payment use and lock use. Exposure highest in tertiary-educated (17.9) and lowest income quintile (12.5); lowest at 60+ (4.1) and women (5.7).')
s.shapes.add_picture(str(FIG / 'figure7_inclusion_vs_risk.png'), Inches(0.6), Inches(1.65), height=Inches(4.95))
bullets(s, 7.6, 1.8, 5.1, 4.8, ['Weak link|rank correlation 0.38 between payment use and exposure across 18 groups.',
        'Protection follows inclusion|rank correlation 0.63 between payment use and lock use.',
        'Where risk concentrates|tertiary-educated (17.9%) and the lowest income quintile (12.5%).',
        'Lowest|ages 60+ (4.1%) and women (5.7%): fewer contacts or less reporting.'], 15, 12)
src(s, 'Groups overlap and denominators differ: descriptive only. Source: authors\' calculations, India microdata, Global Findex Database 2025 (2024 survey).')

# 10 --------------------------------------------------------------- gap by group
s = slide('4  Results: adoption vs protection', 'Protection lags use at older ages',
          'RQ4. Payment use minus lock use. 60+: 56.6 vs 22.9 = +33.7. 15-24: 43.5 vs 75.7 = -32.1. Different denominators, descriptive only.')
cd = CategoryChartData(); cd.categories = ['Women', 'Men', 'Age 15–24', 'Age 25–39', 'Age 40–59', 'Age 60+', 'Income Q1', 'Income Q5']
cd.add_series('Digital payment use (all adults)', (42.7, 54.1, 43.5, 51.3, 46.6, 56.6, 34.8, 67.4)); cd.add_series('Phone lock (phone owners)', (50.3, 62.7, 75.7, 62.7, 43.6, 22.9, 40.6, 75.2))
gf = s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(0.6), Inches(1.7), Inches(8.6), Inches(4.85), cd); ch = gf.chart
style_chart(ch); colour(ch.plots[0].series, [BLUE, TEAL]); ch.plots[0].gap_width = 70; ch.value_axis.maximum_scale = 100
ch.plots[0].has_data_labels = True; ch.plots[0].data_labels.number_format = '0'; ch.plots[0].data_labels.number_format_is_linked = False; ch.plots[0].data_labels.font.size = Pt(10)
stat(s, 9.5, 1.8, 3.2, '+33.7', 'points: ages 60+ (payment use above lock use)', AMBER)
stat(s, 9.5, 3.55, 3.2, '−32.1', 'points: ages 15–24 (lock use above payment use)', BLUE)
src(s, 'Payment use among all adults in the group; lock among phone owners. Source: authors\' calculations.')

# 11 --------------------------------------------------------------- peers
s = slide('4  Results: peer economies', 'India: top-tier accounts, below-peer phone ownership',
          'Findex 2025 indicators for 2024. India account 89.0 (second to China 89.4), phone 66.5 (second lowest), lock 57.6, request 9.4 (our microdata; lowest among economies with a value). Indicative only: published aggregates without sampling errors.')
cd = CategoryChartData(); cd.categories = ['India', 'China', 'Indonesia', 'Bangladesh', 'Pakistan', 'Brazil', 'South Africa']
cd.add_series('Account (% adults)', (89.0, 89.4, 56.3, 43.3, 27.3, 86.4, 81.1)); cd.add_series('Own phone (% adults)', (66.5, 96.6, 80.3, 82.4, 62.9, 92.1, 87.0))
cd.add_series('Phone lock (% phone owners)', (57.6, None, 69.1, 47.5, 46.4, 78.0, 68.5))
gf = s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(0.6), Inches(1.7), Inches(8.6), Inches(4.85), cd); ch = gf.chart
style_chart(ch, size=11); colour(ch.plots[0].series, [TEAL, BLUE, AMBER]); ch.plots[0].gap_width = 60; ch.value_axis.maximum_scale = 100
bullets(s, 9.5, 1.8, 3.3, 4.8, ['Accounts|India second to China.', 'Phones|India second lowest, above only Pakistan.', 'Locks|India 57.6%; peers 46.4% to 78.0%.', 'Requests|India 9.4% (our microdata); peers 12.7% to 32.4%.'], 14.5, 12)
src(s, 'Published Global Findex 2025 aggregates, 2024; China has no published lock value. Source: World Bank Data API.')

# 12 --------------------------------------------------------------- reviews
s = slide('4  Results: what users complain about', 'Reviews: rewards, refunds and blocks, not theft',
          'Fraud-keyword reviews: 118 Google Play, 57 App Store, 65 bank apps, all read and classified. Theft or unauthorised access: 6, 2 and 3 first pass; the 122-review second coder found 8 of 122 (about 0.1 percent of 8,330 reviews). Hindi/Hinglish extension: 6 to 12 on Google Play (0.2 percent).')
cd = CategoryChartData(); cd.categories = ['Reward or cashback not honoured', 'Money debited, failed payment', 'Blocked account, mis-selling, grievance', 'Spam, permissions, intrusive security', 'General accusation', 'Praise or no complaint', 'Unauthorised access or theft']
cd.add_series('Payment apps, Google Play (118)', (50.8, 12.7, 9.3, 8.5, 7.6, 5.9, 5.1)); cd.add_series('Payment apps, App Store (57)', (29.8, 19.3, 17.5, 12.3, 10.5, 7.0, 3.5)); cd.add_series('Bank apps (65)', (4.6, 6.2, 38.5, 20.0, 21.5, 4.6, 4.6))
gf = s.shapes.add_chart(XL_CHART_TYPE.BAR_CLUSTERED, Inches(0.6), Inches(1.65), Inches(8.2), Inches(4.95), cd); ch = gf.chart
style_chart(ch, size=11); colour(ch.plots[0].series, [AMBER, BLUE, TEAL]); ch.plots[0].gap_width = 50; ch.category_axis.reverse_order = True
ch.plots[0].has_data_labels = True; ch.plots[0].data_labels.number_format = '0'; ch.plots[0].data_labels.number_format_is_linked = False; ch.plots[0].data_labels.font.size = Pt(9)
ch.value_axis.maximum_scale = 60
stat(s, 9.1, 1.75, 3.6, '14,088', 'reviews coded across 13 apps and two stores', TEAL, 1.45)
stat(s, 9.1, 3.35, 3.6, '≈ 0.1%', 'of reviews describe unauthorised access or theft', AMBER, 1.45)
bullets(s, 9.1, 5.0, 3.7, 1.6, ['Bank apps|SIM binding, biometric and root checks are a recurring one-star theme (149 reviews).'], 13, 6)
src(s, 'Share (%) of fraud-keyword reviews per category. Self-selected reviews: not a measure of scam prevalence. Source: authors\' coding.')

# 13 --------------------------------------------------------------- documents and studies
s = slide('4  Results: documents and interview studies', 'Published studies: social engineering, slow redress',
          'Five India studies (Mungara 2025, Bajaj 2026, Jain 2021, Aadil 2023, Sengupta 2025). Counts are of studies. Examples: 45 of 46 said trust in the receiver matters; 12 of 24 merchants reported fake payment confirmations; of 91 victims who reported fraud, 59 could not recover money. Documents: World Bank trust and consumer protection, RBI awareness and credential protection.')
th = [('Social engineering', '5 of 5'), ('Trust in counterparty or bank', '5 of 5'), ('Low awareness or literacy', '5 of 5'), ('Weak support or redress', '4 of 5'), ('Family and informal advice', '4 of 5'), ('Gender, age, vulnerability', '3 of 5'), ('Protective advice, design cues', '2 of 5'), ('Merchant and business harms', '2 of 5')]
for i, (a, b) in enumerate(th):
    x = 0.6 + (i % 2) * 3.4; y = 1.75 + (i // 2) * 0.95
    box(s, x, y, 3.25, 0.82, PALE); box(s, x, y, 0.08, 0.82, TEAL if i < 4 else BLUE)
    text(s, x + 0.2, y + 0.04, 2.1, 0.75, a, 13, True, NAVY, anchor=MSO_ANCHOR.MIDDLE); text(s, x + 2.2, y + 0.04, 1.0, 0.75, b, 15, True, TEAL, HEAD, PP_ALIGN.RIGHT, MSO_ANCHOR.MIDDLE)
bullets(s, 7.6, 1.75, 5.1, 3.6, ['Redress|59 of the 91 victims who reported fraud could not recover their money.', 'Merchants|12 of 24 reported fake payment confirmations.', 'Trust|45 of 46 said trust in the receiver matters; a trust badge was rated highest of four nudges.'], 14.5, 10)
box(s, 0.6, 5.7, 12.1, 0.85, NAVY)
text(s, 0.85, 5.73, 11.6, 0.8, 'Documents (World Bank, RBI): trust linked to risk awareness and dispute resolution; consumer protection beside capability; protect credentials such as OTPs and PINs.', 14.5, True, WHITE, anchor=MSO_ANCHOR.MIDDLE)

# 14 --------------------------------------------------------------- discussion
s = slide('5  Discussion', 'Risk concentrates where inclusion outruns safeguards',
          'Mixed answer to the central question. Payment users are more reachable by scammers, but across groups the link is weak; exposure is also high among the poorest; protection lags at older ages. Reviews do not measure scam prevalence; victims may not write reviews; interview studies describe what reviews miss. Policy: judge inclusion by active and safe use; test security prompts so they do not lock out users.')
cards = [('Mixed answer', 'Users report more requests (13.1% vs 4.3%), yet the group-level link is weak (0.38) and exposure is also high among the poorest.', TEAL),
         ('Safeguards lag', 'Payment use far exceeds lock use at ages 60+. A lock protects a handset, not judgment.', AMBER),
         ('Friction is a risk too', 'Security prompts (SIM binding, biometrics, root checks) lock out legitimate users and drive one-star reviews.', BLUE),
         ('Policy', 'Track active and safe use, evaluate awareness on behaviour, and make providers own warnings, refunds and complaints.', NAVY)]
for i, (h, b, c) in enumerate(cards):
    card(s, 0.6 + (i % 2) * 6.15, 1.75 + (i // 2) * 2.45, 5.95, 2.25, h, b, c, 19, 15)

# 15 --------------------------------------------------------------- venture
s = slide('5.3  Managerial implications', 'Venture idea: a multilingual payment-safety companion',
          'Institution pays, user free. Short audio and visual explanations, a pre-payment checklist, verified routes to support and official reporting. It does not hold money, guarantee recovery or ask for an OTP or PIN. Months 1-2 discovery, 3-5 controlled pilot, month 6 commercial gate. No pilot has been run.')
blocks = [('Customer', 'Banks, payment providers and merchant networks pay a subscription.'), ('Value', 'Understandable guidance and verified routes to support; aggregated learning for the buyer.'),
          ('Channels', 'Partner app links, branch and merchant onboarding, low-bandwidth audio.'), ('Alternatives', 'RBI campaigns, in-app warnings, helpline 1930, in-house builds. Must add measurable value.'),
          ('Pilot plan', 'Months 1–2 discovery, 3–5 controlled pilot, month 6+ commercial gate. Not yet run.'), ('Boundary', 'No money handling, no OTP or PIN requests, no recovery guarantee.')]
for i, (h, b) in enumerate(blocks):
    card(s, 0.6 + (i % 3) * 4.1, 1.75 + (i // 3) * 2.45, 3.9, 2.25, h, b, BLUE, 19, 14)

# 16 --------------------------------------------------------------- finance
s = slide('4.7  Financial model (illustrative)', 'Break-even at 8 institutions, 13 while growing',
          'All inputs are assumptions, not findings. Fee 50,000 per month, variable 10,000, acquisition 2 lakh, fixed 3 lakh a month. Base: -32.80, 0.00, +52.16 lakh. Sensitivity: fee 40,000 needs 10; variable 15,000 needs 9; acquisition 3 lakh gives payback 7.5 months and 15 while growing. Seed INR 75 lakh; conservative case exceeds it by Year 2 (81.80 lakh).')
stat(s, 0.6, 1.75, 2.9, '₹40,000', 'monthly contribution per institution (80%)', TEAL, 1.4)
stat(s, 3.7, 1.75, 2.9, '5 months', 'simple acquisition payback', BLUE, 1.4)
stat(s, 6.8, 1.75, 2.9, '8 → 13', 'break-even institutions: steady state → growing', AMBER, 1.4)
stat(s, 9.9, 1.75, 2.8, '₹75 lakh', 'proposed staged seed budget', NAVY, 1.4)
cd = CategoryChartData(); cd.categories = ['Year 1', 'Year 2', 'Year 3']
cd.add_series('Conservative', (-36.80, -30.00, -17.44)); cd.add_series('Base', (-32.80, 0.00, 52.16)); cd.add_series('Optimistic', (-24.00, 48.80, 173.16))
gf = s.shapes.add_chart(XL_CHART_TYPE.LINE_MARKERS, Inches(0.6), Inches(3.4), Inches(7.4), Inches(3.2), cd); ch = gf.chart
style_chart(ch, size=11); ch.category_axis.tick_label_position = XL_TICK_LABEL_POSITION.LOW
for sr, c in zip(ch.plots[0].series, [AMBER, BLUE, TEAL]):
    sr.format.line.color.rgb = c; sr.format.line.width = Pt(2.5); sr.smooth = False
bullets(s, 8.3, 3.5, 4.4, 3.1, ['Base|deficit 32.80 lakh in Year 1, break-even Year 2, surplus 52.16 in Year 3.', 'Conservative|loss-making in all three years.', 'Fee cut to ₹40,000|break-even rises from 8 to 10.', 'Seed|conservative case needs ₹81.80 lakh by Year 2.'], 13.5, 8)
src(s, 'ILLUSTRATIVE ASSUMPTIONS TO BE VALIDATED. Annual operating surplus or deficit in INR lakh; no churn, tax or financing flows.')

# 17 --------------------------------------------------------------- limits
s = slide('5.4  Future scope', 'Limitations and next steps', 'Be upfront: cross-sectional, no verified losses, approximate intervals, self-selected reviews, AI-assisted coding with limited human checks, no interviews of our own, finance inputs are assumptions.')
box(s, 0.6, 1.75, 5.95, 4.75, PALE); text(s, 0.85, 1.9, 5.4, 0.5, 'Limitations', 21, True, NAVY, HEAD)
bullets(s, 0.85, 2.5, 5.5, 3.9, ['Cross-sectional, self-reported; requests are not verified fraud.', 'Approximate intervals: no design variables in the public file.', 'Reviews are self-selected; coding is AI-assisted with human checks on samples only.', 'No interviews or surveys of our own; five published studies selected by us.', 'Finance inputs are assumptions; individuals, not enterprises.'], 14.5, 8)
box(s, 6.75, 1.75, 5.95, 4.75, PALE); text(s, 7.0, 1.9, 5.4, 0.5, 'Next steps', 21, True, NAVY, HEAD)
bullets(s, 7.0, 2.5, 5.5, 3.9, ['Consent-based interviews with merchants, users and budget owners.', 'Evaluated, powered pilot with pre-set outcomes.', 'Design-based estimation and peer-country microdata.', 'Venture model with churn, tax and monthly cash flow.'], 14.5, 8)

# 18 --------------------------------------------------------------- conclusion
s = slide('6  Conclusion', 'Inclusion is broad; safe use is the opportunity', 'Restate: 89.0 vs 48.5; payment users report more requests, OR 3.45, but group-level link is weak; theft is rare in reviews while support, refunds and blocks dominate; pilot a safety service; next step is willingness-to-pay evidence.')
bullets(s, 0.6, 1.8, 7.5, 4.8, ['Access|89.0% own accounts, but 48.5% made or received a digital payment and 57.7% of phone owners have a lock.',
        'Exposure|payment users report more requests (13.1% vs 4.3%; odds ratio 3.45); across groups the link is weak.',
        'Grievances|reviews and studies point to rewards, refunds, blocks, support and security prompts, not reported theft.',
        'Opportunity|a staged, institution-funded safety pilot; viable only if price, cost and renewal assumptions hold.'], 17, 12)
box(s, 8.4, 1.85, 4.3, 4.3, NAVY)
text(s, 8.7, 2.1, 3.7, 3.8, 'Next step: pilot evidence on willingness to pay, retention and effectiveness.', 24, True, WHITE, HEAD, anchor=MSO_ANCHOR.MIDDLE)

prs.save(OUT); print('saved', OUT, len(prs.slides), 'slides')

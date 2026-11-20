# -*- coding: utf-8 -*-
"""Group 31 presentation that mirrors the paper structure. Run from C:\\Users\\Sudhanshu\\Desktop\\EF"""
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION, XL_LABEL_POSITION

R = Path('Group_31/revised'); FIG = R / 'figures'
NAVY = RGBColor(0x12, 0x2B, 0x45); TEAL = RGBColor(0x1B, 0x8A, 0x7E); BLUE = RGBColor(0x2A, 0x5F, 0xA5)
AMBER = RGBColor(0xD9, 0x8A, 0x1F); INK = RGBColor(0x22, 0x2B, 0x36); GREY = RGBColor(0x6B, 0x75, 0x80)
PALE = RGBColor(0xF1, 0xF5, 0xF8); WHITE = RGBColor(255, 255, 255)
HEAD = 'Georgia'; BODY = 'Calibri'

prs = Presentation(); prs.slide_width = Inches(13.333); prs.slide_height = Inches(7.5)
blank = prs.slide_layouts[6]
N = [0]


def box(s, x, y, w, h, fill=None, line=None, shape=MSO_SHAPE.RECTANGLE):
    sh = s.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    if fill is None: sh.fill.background()
    else: sh.fill.solid(); sh.fill.fore_color.rgb = fill
    if line is None: sh.line.fill.background()
    else: sh.line.color.rgb = line; sh.line.width = Pt(1)
    sh.shadow.inherit = False
    return sh


def text(s, x, y, w, h, t, size=18, bold=False, color=INK, font=BODY, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, lines=None):
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h)); tf = tb.text_frame; tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = Inches(0.05); tf.margin_top = tf.margin_bottom = Inches(0.03)
    items = lines if lines is not None else [t]
    for i, it in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align; p.space_after = Pt(6)
        r = p.add_run(); r.text = it; r.font.size = Pt(size); r.font.bold = bold; r.font.color.rgb = color; r.font.name = font
    return tb


def bullets(s, x, y, w, h, items, size=18, color=INK):
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h)); tf = tb.text_frame; tf.word_wrap = True
    for i, it in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph(); p.space_after = Pt(10)
        head, _, rest = it.partition('|')
        if rest:
            r = p.add_run(); r.text = head + ' '; r.font.bold = True; r.font.size = Pt(size); r.font.color.rgb = NAVY; r.font.name = BODY
            r = p.add_run(); r.text = rest; r.font.size = Pt(size); r.font.color.rgb = color; r.font.name = BODY
        else:
            r = p.add_run(); r.text = '•  ' + it; r.font.size = Pt(size); r.font.color.rgb = color; r.font.name = BODY
    return tb


def slide(kicker, title, notes=''):
    s = prs.slides.add_slide(blank); N[0] += 1
    box(s, 0, 0, 13.333, 7.5, WHITE)
    box(s, 0, 0, 0.18, 7.5, NAVY)
    text(s, 0.6, 0.35, 9, 0.35, kicker.upper(), 12, True, TEAL)
    text(s, 0.6, 0.68, 12.1, 0.9, title, 30, True, NAVY, HEAD)
    text(s, 12.2, 7.0, 0.8, 0.3, str(N[0]), 11, False, GREY, align=PP_ALIGN.RIGHT)
    text(s, 0.6, 7.0, 8, 0.3, 'Group 31  |  Entrepreneurial Finance', 11, False, GREY)
    if notes: s.notes_slide.notes_text_frame.text = notes
    return s


def stat(s, x, y, w, big, small, color=TEAL):
    box(s, x, y, w, 1.55, PALE)
    box(s, x, y, 0.08, 1.55, color)
    text(s, x + 0.25, y + 0.12, w - 0.3, 0.8, big, 34, True, color, HEAD)
    text(s, x + 0.25, y + 0.92, w - 0.3, 0.6, small, 13, False, INK)


def pic(s, name, x, y, w):
    s.shapes.add_picture(str(FIG / name), Inches(x), Inches(y), width=Inches(w))


def source(s, t):
    text(s, 0.6, 6.62, 12, 0.35, t, 11, False, GREY)


# 1 ---------------------------------------------------------------- title
s = prs.slides.add_slide(blank); N[0] += 1
box(s, 0, 0, 13.333, 7.5, NAVY); box(s, 0, 5.2, 13.333, 0.06, TEAL)
text(s, 0.9, 1.3, 11.5, 1.9, 'Mobile Banking, Financial Inclusion and Cybersecurity Risk in India', 40, True, WHITE, HEAD)
text(s, 0.9, 3.35, 11.5, 0.9, 'A survey-weighted analysis of the 2024 Global Findex and an institutional payment-safety service proposal', 20, False, RGBColor(0xC9, 0xD8, 0xE6))
text(s, 0.9, 5.5, 8, 1.0, '', 18, False, WHITE, lines=['Rushal Verma (IIT2024045)  |  Vichanshu Raj (IIT2024083)', 'Sudhanshu (IIT2024081)', 'Group 31  |  Entrepreneurial Finance'])
s.notes_slide.notes_text_frame.text = 'Introduce the topic: access to accounts is high in India, but is digital use safe and confident? We analyse the 2024 India Global Findex and test a venture idea.'

# 2 ---------------------------------------------------------------- introduction
s = slide('1  Introduction', 'Access is not the same as confident, safe use',
          'Background, problem, gap. Define terms: inclusion, digital payment use, reported exposure (not verified fraud).')
bullets(s, 0.6, 1.8, 6.2, 4.6, [
    'Background|Mobile phones and digital payments changed how people reach finance; India has a large digital payment infrastructure.',
    'Problem|Owning an account, using it digitally and using it safely are three different things.',
    'Gap|Few studies join national adoption patterns, device safeguards and reported scam exposure, then ask what service an entrepreneur could build.'], 17)
box(s, 7.2, 1.85, 5.5, 4.4, PALE)
text(s, 7.5, 2.0, 5, 0.4, 'KEY TERMS', 12, True, TEAL)
bullets(s, 7.5, 2.45, 4.9, 3.8, [
    'Account ownership|measures access.',
    'Digital payment use|made or received a digital payment in the past year.',
    'Reported exposure|an unsolicited call or message asking for money. Not verified fraud.'], 15)

# 3 ---------------------------------------------------------------- RQs
s = slide('1  Introduction', 'Six research questions', 'Walk through RQ1-RQ6 and note where each is answered.')
rqs = [('RQ1', 'How do ownership, digital payment use and device protection differ by gender, age and income?'),
       ('RQ2', 'Are payment users more likely to report unsolicited money requests, after adjustment?'),
       ('RQ3', 'Among request recipients, is a device lock linked to fewer reporting that they sent money?'),
       ('RQ4', 'Which groups show the largest gap between payment use and device protection?'),
       ('RQ5', 'What do public app reviews, institutional documents and published interviews reveal about fraud grievances, friction and support?'),
       ('RQ6', 'What price, cost and customer numbers let an institution-funded safety service break even?')]
for i, (k, q) in enumerate(rqs):
    y = 1.6 + i * 0.8
    box(s, 0.6, y, 1.1, 0.68, TEAL if i < 5 else AMBER); text(s, 0.6, y + 0.1, 1.1, 0.5, k, 20, True, WHITE, HEAD, PP_ALIGN.CENTER)
    box(s, 1.8, y, 10.9, 0.68, PALE); text(s, 2.0, y + 0.06, 10.5, 0.56, q, 16, False, INK, anchor=MSO_ANCHOR.MIDDLE)

# 4 ---------------------------------------------------------------- literature
s = slide('2  Literature review', '35 academic sources point to one gap',
          'Four strands: finance and development, adoption and trust, security behaviour, cyber risk economics. Gap: nobody joins them for India with a venture lens.')
cols = [('Finance and development', 'Mobile money lifted households out of poverty and helped risk sharing (Suri & Jack; Jack & Suri). Benefits depend on use.'),
        ('Adoption and trust', 'Usefulness, ease and credibility drive mobile banking use (Davis; Venkatesh; Luarn & Lin).'),
        ('Security behaviour', 'Phishing exploits routine behaviour; awareness campaigns often fail (Dhamija; Button; Bada).'),
        ('Cyber risk economics', 'Security is under-supplied because incentives are split (Anderson & Moore; Kopp).')]
for i, (h, b) in enumerate(cols):
    x = 0.6 + i * 3.08
    box(s, x, 1.85, 2.9, 3.2, PALE); box(s, x, 1.85, 2.9, 0.08, TEAL)
    text(s, x + 0.15, 2.05, 2.6, 0.7, h, 17, True, NAVY, HEAD); text(s, x + 0.15, 2.85, 2.6, 2.2, b, 14)
box(s, 0.6, 5.35, 12.1, 1.1, NAVY)
text(s, 0.85, 5.45, 11.6, 0.9, 'Gap: no recent national view of India that places adoption, device protection and reported scam exposure together, then tests a venture response with explicit assumptions.', 17, True, WHITE, anchor=MSO_ANCHOR.MIDDLE)

# 5 ---------------------------------------------------------------- methodology
s = slide('3  Methodology', 'Survey microdata, weighted analysis, scenario model',
          'Cross-sectional observational design. Weights, eligibility and caveats about intervals. No primary fieldwork. Ethics: public de-identified data.')
stat(s, 0.6, 1.8, 3.9, '3,000', 'adults aged 15+, India Global Findex 2024 (199 variables)')
stat(s, 4.7, 1.8, 3.9, 'Weighted', 'all percentages use the survey weight; n is unweighted', BLUE)
stat(s, 8.8, 1.8, 3.9, 'Logistic', 'adjusted model on 2,145 phone owners (approximate intervals)', AMBER)
bullets(s, 0.6, 3.7, 12.1, 2.9, [
    'Design|weighted descriptives (RQ1, RQ4), adjusted association (RQ2), lock-status comparison (RQ3), document and review coding (RQ5), financial scenarios (RQ6).',
    'Qualitative|World Bank and RBI documents, 5,758 Google Play and 2,090 App Store reviews, and five published interview studies; no interviews of our own.',
    'Ethics|public de-identified data, results framed as reports not verified fraud, finance figures labelled illustrative.'], 16)

# 6 ---------------------------------------------------------------- results 1
s = slide('4  Results: adoption', 'Accounts are nearly universal; digital use is not',
          'Account 89.0 vs digital payment 48.5. Women 42.7 vs men 54.1. Phone ownership 66.5. Report only.')
stat(s, 0.6, 1.75, 3.9, '89.0%', 'own an account (n = 3,000)')
stat(s, 4.7, 1.75, 3.9, '48.5%', 'made or received a digital payment', BLUE)
stat(s, 8.8, 1.75, 3.9, '66.5%', 'own a phone', AMBER)
pic(s, 'figure1.png', 0.6, 3.55, 7.4)
box(s, 8.3, 3.6, 4.4, 2.8, PALE)
text(s, 8.5, 3.7, 4.0, 0.4, 'VS PUBLISHED FINDEX 2025', 12, True, TEAL)
bullets(s, 8.5, 4.1, 4.0, 2.3, ['Account|India 89.0% vs 79% world, 75% low- and middle-income.', 'Digital payment|India 48.5% vs 61% low- and middle-income.', 'Reading|wider gap between access and use. Indicative only.'], 13)
source(s, 'Survey-weighted; women n = 1,526, men n = 1,474. Source: authors\' calculations, World Bank Global Findex 2025 India microdata.')

# 7 ---------------------------------------------------------------- results 2
s = slide('4  Results: device protection', 'Phone locks vary sharply by age, gender and income',
          'Lock 57.7 overall. Women 50.3 vs men 62.7. Age 15-24 75.7 vs 60+ 22.9. Income Q1 40.6 vs Q5 75.2.')
cd = CategoryChartData(); cd.categories = ['Women', 'Men', 'Age 15–24', 'Age 60+', 'Lowest income', 'Highest income']
cd.add_series('Phone has a lock (%)', (50.3, 62.7, 75.7, 22.9, 40.6, 75.2))
gf = s.shapes.add_chart(XL_CHART_TYPE.BAR_CLUSTERED, Inches(0.6), Inches(1.7), Inches(7.6), Inches(4.8), cd); ch = gf.chart
ch.has_legend = False; ch.has_title = False; ch.plots[0].gap_width = 60; ch.plots[0].has_data_labels = True
dl = ch.plots[0].data_labels; dl.font.size = Pt(14); dl.number_format = '0.0"%"'; dl.number_format_is_linked = False; dl.position = XL_LABEL_POSITION.OUTSIDE_END
ch.plots[0].series[0].format.fill.solid(); ch.plots[0].series[0].format.fill.fore_color.rgb = TEAL
ch.category_axis.tick_labels.font.size = Pt(14); ch.category_axis.reverse_order = True
ch.value_axis.maximum_scale = 100; ch.value_axis.minimum_scale = 0; ch.value_axis.has_major_gridlines = False; ch.value_axis.tick_labels.font.size = Pt(11)
box(s, 8.6, 1.9, 4.1, 3.0, PALE)
text(s, 8.85, 2.05, 3.7, 0.9, '57.7%', 40, True, TEAL, HEAD); text(s, 8.85, 3.0, 3.7, 1.8, 'of phone owners report a PIN, password or fingerprint lock (n = 2,141 valid responses)', 15)
source(s, 'Survey-weighted, phone owners with valid responses. Source: authors\' calculations, Global Findex 2025 India microdata.')

# 8 ---------------------------------------------------------------- results 3
s = slide('4  Results: exposure', 'Payment users report more unsolicited money requests',
          'Users 13.1 vs non-users 4.3. Adjusted OR 3.45 (2.24 to 5.30). Women vs men OR 0.47. 21.0% of recipients sent money (45 of 219). No causal claim.')
pic(s, 'figure3.png', 0.6, 1.75, 7.6)
stat(s, 8.6, 1.75, 4.1, '3.45', 'adjusted odds ratio, payment user vs non-user (approx. 95% interval 2.24 to 5.30)', AMBER)
stat(s, 8.6, 3.5, 4.1, '0.47', 'women vs men (interval 0.32 to 0.69)', BLUE)
bullets(s, 0.6, 4.3, 7.6, 2.2, ['Sent money|45 of 219 request recipients (21.0%).',
        'Lock status|25.0% sent money among those with a lock (39/170), 8.9% without (6/49). Small cells.'], 15)
source(s, 'Interval assumes independent observations; public file lacks design variables. Reports of requests are not verified fraud.')

# 9 ---------------------------------------------------------------- results 4
s = slide('4  Results: adoption vs protection', 'The largest mismatch is at the oldest ages',
          'RQ4. Payment use minus lock use. 60+: 56.6 vs 22.9 = +33.7. 15-24: 43.5 vs 75.7 = -32.1. Different denominators, descriptive only.')
cd = CategoryChartData(); cd.categories = ['Women', 'Men', '15–24', '25–39', '40–59', '60+', 'Lowest income', 'Highest income']
cd.add_series('Digital payment use (all adults)', (42.7, 54.1, 43.5, 51.3, 46.6, 56.6, 34.8, 67.4))
cd.add_series('Device lock (phone owners)', (50.3, 62.7, 75.7, 62.7, 43.6, 22.9, 40.6, 75.2))
gf = s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(0.6), Inches(1.7), Inches(8.4), Inches(4.8), cd); ch = gf.chart
ch.has_title = False; ch.has_legend = True; ch.legend.position = XL_LEGEND_POSITION.BOTTOM; ch.legend.include_in_layout = False; ch.legend.font.size = Pt(12)
ch.plots[0].gap_width = 70; ch.plots[0].has_data_labels = True; ch.plots[0].data_labels.font.size = Pt(10)
ch.plots[0].data_labels.number_format = '0'; ch.plots[0].data_labels.number_format_is_linked = False
ch.plots[0].series[0].format.fill.solid(); ch.plots[0].series[0].format.fill.fore_color.rgb = BLUE
ch.plots[0].series[1].format.fill.solid(); ch.plots[0].series[1].format.fill.fore_color.rgb = TEAL
ch.value_axis.has_major_gridlines = False; ch.value_axis.maximum_scale = 100; ch.value_axis.tick_labels.font.size = Pt(11); ch.category_axis.tick_labels.font.size = Pt(11)
stat(s, 9.3, 1.9, 3.4, '+33.7', 'points: ages 60+ (payment use above lock use)', AMBER)
stat(s, 9.3, 3.65, 3.4, '−32.1', 'points: ages 15–24 (lock use above payment use)', BLUE)
source(s, 'Different denominators (all adults vs phone owners); the difference is descriptive. Source: authors\' calculations.')

# 9a -------------------------------------------------------------- peers
s = slide('4.7  Results: peer economies', 'India: top-tier accounts, below-peer phone ownership',
          'World Bank Findex 2025 aggregates for 2024. India account 89.0 (second to China 89.4), phone 66.5 (second lowest), lock 57.6, unsolicited requests 9.4 (our microdata; lowest among economies with a value). Indicative only.')
s.shapes.add_picture(str(FIG / 'figure5.png'), Inches(0.6), Inches(1.65), height=Inches(4.95))
bullets(s, 7.9, 1.8, 4.8, 4.6, ['Accounts|India 89.0%, second to China (89.4%); world 78.7%.',
        'Phones|India 66.5%, above only Pakistan (62.9%).',
        'Locks|India 57.6%; peers range 46.4% to 78.0%.',
        'Requests|India 9.4% (our microdata); peers 12.7% to 32.4%.'], 15)
source(s, 'Published aggregates, no sampling errors; India request share from authors\' microdata. Source: World Bank Global Findex 2025 API.')

# 9b -------------------------------------------------------------- qualitative
s = slide('4.8  Results: qualitative review', 'Three themes from institutional guidance',
          'Secondary document review of World Bank and RBI sources. No interviews or fieldwork of our own. Review coding: one coder, a blind AI second pass (112 of 118 agreed, kappa 0.93), and a human coder on 40 reviews (95.0% agreement).')
qs = [('Trust and support', 'World Bank: trust is linked to awareness of risks and timely dispute resolution.'),
      ('Shared responsibility', 'World Bank: consumer protection sits alongside financial capability.'),
      ('Awareness and credentials', 'RBI: awareness campaigns through many channels; protect credentials such as OTPs and PINs.')]
for i, (h, b) in enumerate(qs):
    x = 0.6 + i * 4.1
    box(s, x, 1.9, 3.9, 3.0, PALE); box(s, x, 1.9, 3.9, 0.08, AMBER)
    text(s, x + 0.2, 2.15, 3.5, 0.9, h, 20, True, NAVY, HEAD); text(s, x + 0.2, 3.2, 3.5, 1.7, b, 15)
text(s, 0.6, 5.3, 12.1, 1.0, 'Secondary document review only: no interviews, focus groups or respondent comments of our own. Themes were coded by a single coder, checked by a blind AI second pass (94.9%) and a human coder on 40 reviews (95.0%), and are interpretive.', 15, False, GREY)

# 9c -------------------------------------------------------------- reviews
s = slide('4.9  Results: app reviews', 'App reviews: rewards, refunds and support',
          'Five apps, India Play Store, 2 Oct to 19 Nov 2026. 118 fraud-keyword reviews all read and coded: 60 reward deception, 15 failed payments, 11 blocked/support, 10 spam/privacy, 9 general, 7 praise, 6 unauthorised access. 104 reviews mention device-lock prompts.')
stat(s, 0.6, 1.75, 2.9, '5,758', 'reviews, five payment apps (BHIM, SBI YONO, PhonePe, Paytm, Google Pay)')
stat(s, 3.7, 1.75, 2.9, '50.8%', 'of the 118 fraud-keyword reviews are about unpaid cashback or rewards', BLUE)
stat(s, 6.8, 1.75, 2.9, '6 of 5,758', 'describe unauthorised access or theft (0.1%)', AMBER)
stat(s, 9.9, 1.75, 2.8, '104', 'reviews describe device-lock or security-alert prompts', NAVY)
s.shapes.add_picture(str(FIG / 'figure6.png'), Inches(0.6), Inches(3.6), height=Inches(2.9))
bullets(s, 8.6, 3.7, 4.2, 2.9, ['Ratings|fraud-keyword reviews average 1.36 stars vs 2.93 for others.',
        'Other themes|support 5.3%, blocking and verification 6.3%, failed payments 2.3%.',
        'Method|keyword coding, then all 118 fraud-keyword reviews read, then re-coded blind (94.9% AI; 95.0% human, n=40).'], 13)
source(s, 'Self-selected public reviews; not a measure of scam prevalence. Source: authors\' coding of Google Play reviews.')

# 9d -------------------------------------------------------------- beyond Google Play
s = slide('4.10-4.11  Results: more evidence', 'App Store reviews and published interview studies',
          'App Store: 2,090 reviews, same five apps, 30 Apr to 18 Nov 2026. 57 fraud-keyword reviews: 17 rewards, 11 failed payments, 10 blocked/support, 7 spam, 6 general, 4 praise, 2 unauthorised access (4 in a blind second pass, 82.5% agreement). Published studies: Mungara 2025 (26 interviews), Bajaj 2026 (46), Jain 2021 (24 merchants, 10 agents), Aadil 2023 (50 users, 10 officials), Sengupta 2025 (18 interviews, 7 focus groups, survey of 3,784). Secondary evidence, not our interviews.')
stat(s, 0.6, 1.75, 2.9, '2,090', 'App Store reviews of the same five apps; mean rating 3.31', TEAL)
stat(s, 3.7, 1.75, 2.9, '2 to 4', 'of 2,090 reviews describe unauthorised access or theft (0.1-0.2%)', AMBER)
stat(s, 6.8, 1.75, 2.9, '5', 'published interview studies analysed as secondary evidence', BLUE)
stat(s, 9.9, 1.75, 2.8, '5 of 5', 'studies report that trust shapes decisions', NAVY)
bullets(s, 0.6, 3.6, 6.0, 3.0, ['Same pattern on iOS|rewards, failed payments, support and spam outnumber theft reports.',
        'Scams in interviews|OTP sharing, links, impersonation, fake payment requests, tampered QR codes (5 of 5 studies).',
        'Redress|weak support and slow recovery reported in 4 of 5 studies and in the app reviews.'], 15)
bullets(s, 6.9, 3.6, 5.9, 3.0, ['Design cue|a recipient trust badge rated highest of four nudges (8.26 of 10).',
        'Channels|family and WhatsApp prominent in two studies: test them for distribution.',
        'Limit|secondary evidence from small purposive samples; says nothing about willingness to pay.'], 15)
source(s, 'Counts are of studies, not respondents. Sources: Apple App Store feed; Mungara et al. 2025; Bajaj et al. 2026; Jain et al. 2021; Aadil et al. 2023; Sengupta et al. 2025.')

# 10 --------------------------------------------------------------- discussion
s = slide('5  Discussion', 'What the results mean, and what they do not',
          'Academic, policy, managerial. Emphasise association not causation; locks protect handsets not judgment.')
items = [('Academic', 'Join inclusion economics with scam behaviour; add perceived safety to adoption models.'),
         ('Policy', 'Track active and safe use, not only accounts. Evaluate awareness on behaviour, and target older and lower-income users.'),
         ('Managerial', 'Test a narrow institutional pilot: accessible safety guidance and verified routes to support.'),
         ('Caution', 'Cross-sectional, self-reported. Requests are not verified fraud, and locks do not protect against deception.')]
for i, (h, b) in enumerate(items):
    x = 0.6 + (i % 2) * 6.15; y = 1.8 + (i // 2) * 2.4
    box(s, x, y, 5.95, 2.2, PALE); box(s, x, y, 0.08, 2.2, AMBER if h == 'Caution' else TEAL)
    text(s, x + 0.3, y + 0.15, 5.4, 0.5, h, 20, True, NAVY, HEAD); text(s, x + 0.3, y + 0.75, 5.4, 1.4, b, 15)

# 11 --------------------------------------------------------------- venture
s = slide('5.3  Managerial implications', 'Venture idea: a multilingual payment-safety companion',
          'Institution pays, end user free. Audio/visual explainers, pre-payment checklist, verified routes to support. Does not hold money or ask for credentials.')
blocks = [('Customer', 'Banks, payment providers and merchant networks pay a subscription.'),
          ('Value', 'Accessible safety guidance and verified routes to support; aggregated learning for the buyer.'),
          ('Channels', 'Partner app links, branch and merchant onboarding, low-bandwidth audio.'),
          ('Alternatives', 'RBI campaigns, in-app warnings, official helpline 1930, in-house builds. Must add measurable value.'),
          ('Pilot plan', 'Months 1–2 design, 3–5 controlled pilot, month 6+ commercial gate. Not yet run.'),
          ('Boundary', 'No money handling, no OTP or PIN requests, no recovery guarantee.')]
for i, (h, b) in enumerate(blocks):
    x = 0.6 + (i % 3) * 4.1; y = 1.8 + (i // 3) * 2.4
    box(s, x, y, 3.9, 2.2, PALE); box(s, x, y, 3.9, 0.08, BLUE)
    text(s, x + 0.2, y + 0.2, 3.5, 0.5, h, 19, True, NAVY, HEAD); text(s, x + 0.2, y + 0.8, 3.5, 1.4, b, 14)

# 12 --------------------------------------------------------------- finance
s = slide('4.6  Financial model (illustrative)', 'Break-even at 8 institutions, 13 while growing',
          'All inputs are assumptions, not survey findings. Fee 50,000/month, variable 10,000, CAC 2 lakh, fixed 3 lakh/month. Base: -32.8, 0.0, +52.2 lakh.')
stat(s, 0.6, 1.75, 2.9, '₹40,000', 'monthly contribution per institution (80%)')
stat(s, 3.7, 1.75, 2.9, '5 months', 'simple acquisition payback', BLUE)
stat(s, 6.8, 1.75, 2.9, '8 → 13', 'break-even institutions: steady state → growing', AMBER)
stat(s, 9.9, 1.75, 2.8, '₹75 lakh', 'proposed staged seed budget', NAVY)
pic(s, 'figure4.png', 0.6, 3.6, 7.6)
bullets(s, 8.5, 3.6, 4.3, 3.0, ['Base|deficit 32.80 lakh in Year 1, break-even Year 2, surplus 52.16 lakh Year 3.',
        'Conservative|loss-making in all three years.', 'Optimistic|deficit 24.00 then surplus 48.80 and 173.16 lakh.'], 14)
source(s, 'ILLUSTRATIVE ASSUMPTIONS TO BE VALIDATED. Figure in INR lakh; no churn, tax or financing flows.')

# 13 --------------------------------------------------------------- sensitivity
s = slide('5.3  Managerial implications', 'Price, support cost and acquisition cost decide viability',
          'Table: fee 40k/50k/60k vs variable 8k/10k/15k. Churn would remove the Year 2 cushion. Conservative case exceeds seed by end of Year 2 (81.80 lakh).')
rows = [['Variable cost / fee', '₹40,000', '₹50,000', '₹60,000'], ['₹8,000', '10', '8', '6'], ['₹10,000', '10', '8', '6'], ['₹15,000', '12', '9', '7']]
tb = s.shapes.add_table(4, 4, Inches(0.6), Inches(1.9), Inches(6.4), Inches(2.4)).table
for r in range(4):
    for c in range(4):
        cell = tb.cell(r, c); cell.text = rows[r][c]; p = cell.text_frame.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
        p.runs[0].font.size = Pt(18); p.runs[0].font.name = BODY; p.runs[0].font.bold = (r == 0 or c == 0)
        cell.fill.solid(); cell.fill.fore_color.rgb = NAVY if r == 0 else (RGBColor(0xDC, 0xF0, 0xEC) if (r == 2 and c == 2) else PALE)
        p.runs[0].font.color.rgb = WHITE if r == 0 else INK
text(s, 0.6, 4.4, 6.4, 0.6, 'Minimum paying institutions for steady-state break-even (highlight = base case).', 13, False, GREY)
bullets(s, 7.4, 1.8, 5.3, 4.8, ['Price|a 20% lower fee raises the requirement from 8 to 10 institutions.',
        'Support load|variable cost of ₹15,000 raises it to 9.',
        'Acquisition|₹3 lakh CAC lengthens payback to 7.5 months; break-even while growing becomes 15.',
        'Funding|the conservative case needs ₹81.80 lakh by end of Year 2, above the ₹75 lakh seed.',
        'Risks|willingness to pay, support cost, incorrect advice, exclusion, dependence on one partner.'], 15)

# 14 --------------------------------------------------------------- limitations
s = slide('5.4  Future scope', 'Limitations and next steps', 'Be upfront: no verified losses, no causation, interval caveat, no commercial validation.')
box(s, 0.6, 1.8, 5.95, 4.5, PALE); text(s, 0.85, 1.95, 5.4, 0.5, 'Limitations', 20, True, NAVY, HEAD)
bullets(s, 0.85, 2.55, 5.5, 3.7, ['Cross-sectional, self-reported survey; no causal claims.', 'Requests are not verified fraud; sending money is not a loss amount.',
        'Approximate intervals; app reviews are self-selected; coding checked by an AI pass and a small human sample.', 'Individuals, not businesses; finance inputs unvalidated.'], 15)
box(s, 6.75, 1.8, 5.95, 4.5, PALE); text(s, 7.0, 1.95, 5.4, 0.5, 'Next steps', 20, True, NAVY, HEAD)
bullets(s, 7.0, 2.55, 5.5, 3.7, ['Consent-based interviews with merchants, users and budget owners (none yet).', 'Extend the India comparison to peer-country microdata.',
        'Evaluated pilot with pre-set outcomes and a power calculation.', 'Extend the model with churn, tax and monthly cash flow.'], 15)

# 15 --------------------------------------------------------------- conclusion
s = slide('6  Conclusion', 'Broad inclusion; safe use is the opportunity',
          'Restate: 89.0 vs 48.5; payment users report more requests, OR 3.45; test a pilot before scaling; next step is willingness-to-pay evidence.')
bullets(s, 0.6, 1.8, 7.4, 4.6, ['Access|89.0% own accounts, but 48.5% made or received a digital payment.',
        'Protection|57.7% of phone owners have a lock; lower for women, older and lower-income adults.',
        'Exposure|payment users report more unsolicited requests (13.1% vs 4.3%; odds ratio 3.45).',
        'Opportunity|a staged, institution-funded pilot; viable only if price, cost and renewal assumptions hold.'], 17)
box(s, 8.4, 1.85, 4.3, 4.3, NAVY)
text(s, 8.7, 2.1, 3.7, 3.8, 'Next step: pilot evidence on willingness to pay, retention and effectiveness.', 24, True, WHITE, HEAD, anchor=MSO_ANCHOR.MIDDLE)

out = R.parent / 'slides' / 'Group_31_Presentation_Final.pptx'
prs.save(out); print('saved', out, len(prs.slides), 'slides')

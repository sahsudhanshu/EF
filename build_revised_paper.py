"""Build the editable final paper from audited statistics and explicit assumptions."""
import json,re,shutil
from pathlib import Path
from docx import Document
from docx.shared import Inches,Pt,RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT,WD_CELL_VERTICAL_ALIGNMENT
from docx.opc.constants import RELATIONSHIP_TYPE as RT

OUT=Path('Group_31/revised'); OUT.mkdir(parents=True,exist_ok=True)
A=json.loads(Path('Group_31_analysis_audit.json').read_text())
D={r['comparison']:r for r in A['descriptives']}
M={r['variable']:r for r in A['model']}
F=json.loads((OUT/'financial_model.json').read_text())
def pct(k):return f"{D[k]['weighted_percent']:.1f}%"
def n(k):return f"{D[k]['n']:,}"
def gap(k1,k2):return f"{D[k1]['weighted_percent']-D[k2]['weighted_percent']:.1f}"
def model(k):
    q=M[k];return f"{q['odds_ratio']:.2f}",f"{q['low_95']:.2f} to {q['high_95']:.2f}"

doc=Document();s=doc.sections[0]
s.page_width=Inches(8.5);s.page_height=Inches(11)
s.top_margin=Inches(.68);s.bottom_margin=Inches(.65);s.left_margin=s.right_margin=Inches(.73)
s.header_distance=Inches(.27);s.footer_distance=Inches(.28);s.different_first_page_header_footer=True
for sty in ['Normal','Title','Subtitle','Heading 1','Heading 2','Heading 3','Caption']:
    st=doc.styles[sty];st.font.name='Calibri';st.font.color.rgb=RGBColor(0,0,0)
normal=doc.styles['Normal'];normal.font.size=Pt(11);normal.paragraph_format.line_spacing=1.08;normal.paragraph_format.space_after=Pt(6)
for style,size,before,after in [('Heading 1',17,0,9),('Heading 2',12.5,10,5),('Heading 3',11,8,4)]:
    st=doc.styles[style];st.font.size=Pt(size);st.font.bold=True;st.paragraph_format.space_before=Pt(before);st.paragraph_format.space_after=Pt(after);st.paragraph_format.keep_with_next=True
doc.styles['Caption'].font.size=Pt(9);doc.styles['Caption'].font.italic=False;doc.styles['Caption'].paragraph_format.space_after=Pt(5)
header=s.header.paragraphs[0];header.text='GROUP 31  |  ENTREPRENEURIAL FINANCE';header.runs[0].font.size=Pt(8)
footer=s.footer.paragraphs[0];footer.alignment=2
r=footer.add_run('Group 31  |  ');r.font.size=Pt(8)
field=OxmlElement('w:fldSimple');field.set(qn('w:instr'),'PAGE');footer._p.append(field)
doc.core_properties.title='Mobile Banking Financial Inclusion and Cybersecurity Risk in India'
doc.core_properties.author='Rushal Verma; Vichanshu Raj; Sudhanshu'
doc.core_properties.subject='Entrepreneurial Finance term paper with India 2024 Global Findex analysis'
doc.core_properties.keywords='Group 31, India, Global Findex, financial inclusion, entrepreneurial finance'

def p(text='',boldlead=None,small=False):
    x=doc.add_paragraph();x.paragraph_format.widow_control=True
    if boldlead and text.startswith(boldlead):x.add_run(boldlead).bold=True;x.add_run(text[len(boldlead):])
    else:x.add_run(text)
    if small:
        for r in x.runs:r.font.size=Pt(9)
        x.paragraph_format.line_spacing=1.04;x.paragraph_format.space_after=Pt(5)
    return x
def h(t,l=1):return doc.add_heading(t,l)
def new(t):doc.add_page_break();h(t)
def caption(text):
    x=doc.add_paragraph(text,'Caption');x.paragraph_format.keep_with_next=True;return x
def note(text):return p(text,small=True)
def table(headers,rows,widths=None,size=10):
    t=doc.add_table(rows=1,cols=len(headers));t.alignment=WD_TABLE_ALIGNMENT.CENTER;t.autofit=False
    widths=widths or [7.04/len(headers)]*len(headers)
    for c,w in zip(t.columns,widths):c.width=Inches(w)
    allrows=[headers]+rows
    for i,values in enumerate(allrows):
        cells=t.rows[0].cells if i==0 else t.add_row().cells
        for j,(c,text,w) in enumerate(zip(cells,values,widths)):
            c.width=Inches(w);c.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
            tcpr=c._tc.get_or_add_tcPr();margin=OxmlElement('w:tcMar')
            for side,value in [('top',65),('bottom',65),('left',90),('right',90)]:
                el=OxmlElement('w:'+side);el.set(qn('w:w'),str(value));el.set(qn('w:type'),'dxa');margin.append(el)
            tcpr.append(margin)
            borders=OxmlElement('w:tcBorders')
            for edge in ['top','left','bottom','right']:
                el=OxmlElement('w:'+edge);el.set(qn('w:val'),'single');el.set(qn('w:sz'),'4');el.set(qn('w:color'),'D9D9D9');borders.append(el)
            tcpr.append(borders)
            shade=OxmlElement('w:shd');shade.set(qn('w:fill'),'173A57' if i==0 else ('F0F5F8' if i%2==0 else 'FFFFFF'));tcpr.append(shade)
            cp=c.paragraphs[0];cp.paragraph_format.space_after=Pt(0);cp.paragraph_format.line_spacing=1.02
            if j>0 and len(str(text))<32:cp.alignment=WD_ALIGN_PARAGRAPH.CENTER
            rr=cp.add_run(str(text));rr.font.size=Pt(size);rr.bold=(i==0)
            if i==0:rr.font.color.rgb=RGBColor(255,255,255)
        trpr=t.rows[i]._tr.get_or_add_trPr();nosplit=OxmlElement('w:cantSplit');trpr.append(nosplit)
        if i==0:repeat=OxmlElement('w:tblHeader');trpr.append(repeat)
    p('').paragraph_format.space_after=Pt(0)
    return t
def fig(name,text):
    x=doc.add_paragraph();x.paragraph_format.keep_with_next=True;x.paragraph_format.space_after=Pt(2)
    x.add_run().add_picture(str(OUT/'figures'/name),width=Inches(6.95))
    y=doc.add_paragraph(text,'Caption');y.paragraph_format.keep_with_next=False
def statrow(label,key):
    q=D[key];return [label,f"{q['positives']:,}",f"{q['n']:,}",pct(key)]
def link(par,text,url):
    x=OxmlElement('w:hyperlink');x.set(qn('r:id'),par.part.relate_to(url,RT.HYPERLINK,is_external=True))
    r=OxmlElement('w:r');pr=OxmlElement('w:rPr');col=OxmlElement('w:color');col.set(qn('w:val'),'2463A0');pr.append(col);r.append(pr)
    txt=OxmlElement('w:t');txt.text=text;r.append(txt);x.append(r);par._p.append(x)

# 1 Cover
p('ENTREPRENEURIAL FINANCE').paragraph_format.space_before=Pt(60)
x=doc.add_paragraph('Mobile Banking Financial Inclusion and Cybersecurity Risk in India','Title');x.paragraph_format.space_before=Pt(20);x.paragraph_format.space_after=Pt(24)
for r in x.runs:r.font.size=Pt(30);r.font.bold=True;r.font.color.rgb=RGBColor(0,0,0)
p('Term paper\nGroup 31')
x=p('Rushal Verma\nVichanshu Raj\nSudhanshu');x.paragraph_format.space_before=Pt(25);x.paragraph_format.space_after=Pt(25)
p('7 November 2026')
x=p('India Global Findex 2024 survey\nWeighted respondent analysis and an illustrative venture model');x.paragraph_format.space_before=Pt(40)
note('Database release: Global Findex 2025\nMicrodata version: IND_2024_FINDEX_v02_M')

# 2 Abstract and TOC
new('Abstract')
abstract=f"This paper examines financial inclusion, digital payment use and reported cybersecurity exposure in India using the 2024 Global Findex survey of 3,000 adults. Survey-weighted account ownership was {pct('All adults: account')}, while {pct('All adults: anydigpayment')} made or received a digital payment. Among phone owners, unsolicited money requests were reported by {pct('Phone owners, anydigpayment=1: con21')} of payment users and {pct('Phone owners, anydigpayment=0: con21')} of non-users. An exploratory weighted logistic model estimated an adjusted odds ratio of {model('Digital payment')[0]} (approximate 95% interval {model('Digital payment')[1]}). Device-lock use varied by gender, age and income. A focused review of institutional guidance informs a proposed multilingual safety and reporting service sold to banks or merchant networks. An illustrative financial model examines pricing, acquisition costs, break-even and seed funding across three scenarios. The survey does not identify causal effects or verified fraud losses, and model intervals do not incorporate the full sampling design. Commercial demand and service effectiveness require pilot validation."
assert 140<=len(abstract.split())<=165,len(abstract.split())
p(abstract)
note('Keywords: financial inclusion; digital payments; cybersecurity; entrepreneurial finance; India')
h('Contents',2)
contents=[('Key findings','3'),('1 Introduction and 2 Background','4'),('3 Data and methods and 4 Source consistency','5'),('5 Respondent level results','6-8'),('6 Business model canvas','9'),('7 Alternatives and go to market plan','10'),('8 Illustrative financial model','11-13'),('9 Funding and venture risks','14'),('10 Conclusion and Appendix A','15'),('References','16')]
for label,page in contents:
    x=p(label+'\t'+page);x.paragraph_format.tab_stops.add_tab_stop(Inches(6.9),WD_ALIGN_PARAGRAPH.RIGHT);x.paragraph_format.space_after=Pt(7)

# 3 Executive findings
new('Key findings')
p('Account access is widespread, but digital use and basic device protection remain uneven. The evidence supports a focused pilot of an accessible safety service; it does not establish a market size or demonstrate that the proposed service prevents losses.')
caption('Summary of verified findings and their entrepreneurial implications')
table(['Evidence from the survey','Eligible sample','Implication to test'],[
    [f"Account ownership {pct('All adults: account')}; digital payment use {pct('All adults: anydigpayment')}",'All adults\nn = 3,000','Test whether guided onboarding helps people use services they can already access.'],
    [f"Women’s payment use {pct('female=1: anydigpayment')}; men’s {pct('female=2: anydigpayment')}",'Women n = 1,526\nMen n = 1,474','Include women in co-design and assess accessibility before scaling.'],
    [f"Device lock {pct('Phone owners: con18')}",'Valid phone-owner responses\nn = 2,141','Offer practical device guidance alongside payment education.'],
    [f"Request exposure: users {pct('Phone owners, anydigpayment=1: con21')}; non-users {pct('Phone owners, anydigpayment=0: con21')}",'Phone owners\nUsers n = 1,283\nNon-users n = 862','Test contextual support among active payment users.'],
    [f"Adjusted payment-use odds ratio {model('Digital payment')[0]}\n95% interval {model('Digital payment')[1]}",'Phone owners\nn = 2,145\n219 positive outcomes','Use the association to frame research, rather than predict individual fraud risk.'],
    [f"Sent money after a request {pct('Reported unsolicited request: con22')}",'Request recipients\nn = 219\n45 positive outcomes','Measure actual reporting and loss outcomes in a separate consent-based pilot.'],
],[2.49,1.66,2.89],10.2)
note('All percentages are survey-weighted; n and positive outcomes are unweighted counts. Digital payment means made or received a payment in the past year. Request exposure is an unknown caller or message asking for money, not verified fraud. See Section 3 for the shared interpretation limits and Tables 1-3 for full denominators.')
h('Illustrative commercial decision',2)
p('At an assumed INR 50,000 monthly fee and INR 10,000 monthly variable cost per institution, an INR 3 lakh monthly fixed-cost base requires eight paying institutions for steady-state operating break-even. The proposed seed budget is INR 75 lakh. These are calculated outputs of unvalidated assumptions, not Findex findings or evidence of investor returns.')

# 4 Intro and literature
new('1 Introduction')
p('For a small business, the usefulness of a financial account depends on the ability to receive sales proceeds, pay suppliers and manage cash reliably. Mobile banking and digital payments can support these activities. However, account ownership, active digital use and safe use are different dimensions of inclusion. A venture that addresses only access may leave usability and support needs unresolved.')
p('This paper examines those differences in India using adult-level survey evidence. It asks whether digital-payment users report more unsolicited requests for money, which groups report less device protection, and how these patterns could inform a financially testable service. Global Findex describes individuals rather than a representative sample of enterprises [1, 2]. The entrepreneurial contribution is therefore a proposed business model and validation plan, not an estimate of business demand.')
h('2 Background and qualitative evidence')
p('The Global Findex 2025 release includes financial inclusion and digital connectivity measures collected during 2024 [1]. The distinction between making a payment and making or receiving one matters: receiving a digital transfer does not necessarily imply independent use of a mobile banking app. Section 4 resolves this definition issue in the original draft.')
h('2.1 Focused document review',2)
p('We selected three institutional sources for their relevance to adoption, protection and practical fraud awareness: the World Bank’s discussion of trust [4], its responsible financial access overview [5], and the RBI’s awareness circular [6]. We read each for mechanisms and service-design implications, then grouped the material into the themes below. This is a focused interpretive review, not a systematic literature review. No interviews, focus groups or respondent comments were collected.')
p('Trust and usable support. The World Bank links trust with awareness of risks and timely dispute resolution [4]. This suggests testing whether clear guidance and a familiar partner make support easier to use. The gap between account ownership and payment use does not identify distrust as its cause.',boldlead='Trust and usable support.')
p('Shared responsibility. The World Bank places consumer protection alongside financial capability [5]. RBI guidance highlights awareness campaigns and protection of credentials [6]. Together, these sources motivate a service that connects understandable guidance to provider support, while leaving transaction controls and complaint resolution with the relevant institution.',boldlead='Shared responsibility.')
p('Accessibility. The observed demographic differences motivate testing audio, local-language content and assisted channels. This is our design inference from the quantitative and documentary evidence, not a reported user preference. Testing should examine whether advice is understood without creating unnecessary friction in legitimate payments.',boldlead='Accessibility.')
note('Qualitative evidence is used to develop hypotheses. It is not represented as primary fieldwork or as an evaluation of the proposed service.')

# 5 Methods and source resolution
new('3 Data and methods')
p('The analysis uses the India Global Findex 2025 public microdata for the 2024 survey, reference IND_2024_FINDEX_v02_M [2]. The source file contains 3,000 respondents aged 15 or older and 199 variables. The analysis uses the supplied positive survey weight, wgt. Every reported percentage is a weighted share; every n and positive-response count is an unweighted count.')
caption('Analytical definitions and eligibility rules')
table(['Measure','Variable and coding','Denominator'],[
['Account ownership','account = 1','All 3,000 adults'],
['Made or received a digital payment','anydigpayment = 1; past year','All 3,000 adults'],
['Phone ownership','con1 = 1','All 3,000 adults'],
['Phone has a PIN password or fingerprint lock','con18 = 1','2,141 phone owners with yes/no answers; 4 uncertain responses excluded'],
['Unsolicited money request','con21 = 1; past 12 months','2,145 phone owners'],
['Sent money after a request','con22 = 1','219 respondents reporting a request'],
],[2.00,2.12,2.92],10)
p('For account and anydigpayment, the World Bank’s derived zero category includes no, do not know and refusal. For raw connectivity items, we retain only yes/no codes 1 and 2. Weighted share = 100 × sum of positive-response weights / sum of eligible valid-response weights. Each subgroup is recalculated with its own eligible denominator; charts do not pool denominators across indicators.')
p('The exploratory logistic model uses con21 as the outcome among phone owners. Predictors are digital payment use, gender, age per ten years, education, income quintile, workforce status and urban residence. Age and income enter linearly; the reference categories appear in Table 3. All 2,145 eligible observations have complete model inputs. Weighted maximum likelihood is paired with an independent-observation sandwich covariance estimate.')
p('Shared interpretation limits. The cross-sectional, self-reported survey cannot identify causality or timing. Unsolicited requests are not verified fraud; sending money is not a measured loss amount. Phone-owner and request-recipient analyses concern selected subsets. The public file lacks strata and primary sampling unit identifiers, so model intervals are approximate and not full design-based confidence intervals. Unmeasured activity, recall and selection can affect associations; odds ratios are not risk ratios.',boldlead='Shared interpretation limits.')
h('4 Source consistency')
p('All empirical results use our weighted microdata estimates. The previous dashboard values of 36% for women and 54% for men describe making specified digital payments, whereas our 42.7% and 54.1% estimates use the broader made-or-received indicator; they are different measures, not conflicting estimates of one measure [3]. Mixed-source comparisons have been removed. Percentages and gaps are rounded independently from full precision to one decimal, so a gap can differ by 0.1 point from subtracting displayed shares. Odds ratios use two decimals; underlying results are unchanged.')

# 6 Adoption and exposure
new('5 Respondent level results')
h('5.1 Adoption and exposure',2)
p(f"Table 1 distinguishes the adult population from the two safety-question subgroups. Account ownership exceeds payment use by {gap('All adults: account','All adults: anydigpayment')} percentage points. Figure 1 shows similar account ownership for women and men, alongside differences in phone ownership and payment use.")
caption('Table 1. Adoption and exposure using our weighted microdata estimates')
table(['Indicator and eligible group','Positive\ncount','Valid n','Weighted\nshare'],[
statrow('Account ownership | all adults','All adults: account'),
statrow('Digital payment | all adults','All adults: anydigpayment'),
statrow('Phone ownership | all adults','All adults: con1'),
statrow('Digital payment | women','female=1: anydigpayment'),
statrow('Digital payment | men','female=2: anydigpayment'),
statrow('Request | all phone owners','Phone owners: con21'),
statrow('Request | phone-owning payment users','Phone owners, anydigpayment=1: con21'),
statrow('Request | phone-owning non-users','Phone owners, anydigpayment=0: con21'),
statrow('Sent money | request recipients','Reported unsolicited request: con22'),
],[3.63,1.09,1.08,1.24],10)
note('Source: authors’ calculations from [2]. Positive count is not the numerator of the weighted percentage; the percentage uses survey weights. “Request” means an unsolicited call or message asking for money. The final row is conditional on reporting such a request.')
fig('figure1.png','Figure 1. Gender differences in financial access and use. All indicators use all women (n = 1,526) or all men (n = 1,474), respectively. Survey-weighted percentages; source: authors’ calculations from [2].')
p(f"Women’s payment use was {pct('female=1: anydigpayment')} and men’s was {pct('female=2: anydigpayment')}, a {gap('female=2: anydigpayment','female=1: anydigpayment')} percentage-point difference. Similar account ownership does not imply equal opportunities to use an account digitally. The survey does not establish which barriers explain this difference.")

# 7 Device locks
new('5.2 Device protection across groups')
p(f"Table 2 reports phone-lock use among eligible phone owners. The overall share was {pct('Phone owners: con18')}. Lower reported protection among older and lower-income respondents motivates accessible guidance, subject to the limits in Section 3. Figure 2 pairs the income comparisons with payment use while keeping their denominators separate.")
caption('Table 2. Device-lock use among phone owners with valid responses')
table(['Group','Lock yes\ncount','Valid n','Weighted\nshare'],[
statrow('All phone owners','Phone owners: con18'),
statrow('Women','Phone owners, female=1: con18'),statrow('Men','Phone owners, female=2: con18'),
statrow('Digital-payment users','Phone owners, anydigpayment=1: con18'),statrow('Digital-payment non-users','Phone owners, anydigpayment=0: con18'),
*[statrow('Age '+k.replace('–','-'),'Phone owners, age_group='+k+': con18') for k in ['15–24','25–39','40–59','60+']],
statrow('Lowest income quintile','Phone owners, inc_q=1: con18'),statrow('Highest income quintile','Phone owners, inc_q=5: con18')
],[3.63,1.09,1.08,1.24],10)
note('Source: authors’ calculations from [2]. Each row has its own valid denominator. Four phone owners have uncertain lock responses and are excluded from the relevant rows. Age, gender, payment and income rows overlap and must not be added together.')
fig('figure2.png','Figure 2. Income differences in payment use and device protection. Payment use: lowest quintile n = 515, highest n = 712 (all adults). Lock use: lowest n = 298, highest n = 623 (valid phone owners). Survey-weighted shares; source: authors’ calculations from [2].')
p('A lock limits access to a device; it is not a measure of whether a person recognizes deceptive requests. Appendix A retains the exploratory comparison of sending money by lock status, including its small cell counts. It cannot establish a protective or harmful effect of locking.')

# 8 Model
new('5.3 Adjusted association with request exposure')
p(f"The adjusted model includes {A['model_n']:,} phone owners and {A['model_positive']} positive outcomes. Digital-payment use is associated with higher odds of a reported request (Table 3). Figure 3 shows the corresponding unadjusted weighted comparison. These are complementary summaries of association, with the interpretation limits stated in Section 3.")
caption('Table 3. Exploratory weighted logistic model for unsolicited requests')
model_labels=[('Digital payment','Payment user versus non-user'),('Female','Woman versus man'),('Age per 10 years','Age per 10-year increase'),('Secondary education','Secondary versus primary or less'),('Tertiary education','Tertiary versus primary or less'),('Income quintile','Income quintile per one-step increase'),('In workforce','In workforce versus out'),('Urban','Urban versus rural')]
table(['Predictor and comparison','Adjusted\nodds ratio','Approximate\n95% interval'],[[label,*model(key)] for key,label in model_labels],[3.9,1.35,1.79],10.3)
note('Outcome: con21 = 1. Robust intervals assume independent respondents and do not account for the full clustered/stratified design. Age and income effects assume linearity on log odds. The intercept is reported in Appendix A; all coefficients and approximate p-values remain in the reproducibility files. No design-based significance claim is made.')
fig('figure3.png','Figure 3. Unsolicited money requests by digital-payment use among phone owners. Positive reports: users 173; non-users 46. Survey-weighted percentages; source: authors’ calculations from [2]. These are exposure reports, not verified fraud rates.')
p(f"The unadjusted difference is {gap('Phone owners, anydigpayment=1: con21','Phone owners, anydigpayment=0: con21')} percentage points. After adjustment, the payment-use odds ratio is {model('Digital payment')[0]} (approximate interval {model('Digital payment')[1]}). The women-versus-men odds ratio is {model('Female')[0]} (interval {model('Female')[1]}). Adjustment cannot remove omitted differences in phone activity or establish the direction of influence.")
p('The commercial implication is to test support where digital activity is already present, while also addressing barriers among less active users. The model is not a customer risk score and does not justify charging particular demographic groups different prices.')

# 9 Business canvas
new('6 Business model canvas')
p('We propose a multilingual payment-safety companion distributed through institutions. The paying customer would be a bank, payment provider or merchant network; end users would receive guidance without an additional fee. The service would provide short audio and visual explanations, a pre-payment checklist and verified routes to the institution’s support and official reporting channels.')
caption('Table 4. Proposed business model canvas summary')
table(['Canvas element','Proposed design and validation need'],[
['Customer segments','Institutional buyers serving first-time digital users and small merchants. End-user priorities include women, older users and people needing assisted access. These are pilot recruitment priorities, not proven market segments.'],
['Value proposition','Understandable safety guidance and easier navigation to trusted support. Buyers receive aggregated learning and support-use measures. Fraud reduction and cost savings must be demonstrated.'],
['Channels','Partner app or web links, branch and business-correspondent onboarding, and merchant-network training. Test low-bandwidth audio and assisted use.'],
['Customer relationships','Named institutional account contact, staff training, quarterly reviews and agreed service scope. End users access support through existing partner channels.'],
['Revenue streams','Recurring institutional subscription. The model assumes no end-user charge, advertising, data sale, transaction commission or onboarding revenue.'],
['Key activities','Content localization, usability testing, secure integration, link verification, partner onboarding and measurement of comprehension and support use.'],
['Key resources','Small product team, reusable content library, language reviewers, secure hosting and a partner-approved directory of support channels.'],
['Key partners','Pilot bank or merchant network; language and accessibility specialists; independent security reviewers. Official channels are referral destinations, not assumed commercial partners.'],
['Cost structure','Fixed product and quality team; variable institution-level delivery cost; incremental customer acquisition cost; prelaunch development and pilot evaluation.'],
],[1.45,5.59],10.1)
h('Scope of the service',2)
p('The companion would not hold money, authorize payments, guarantee recovery or request credentials. It would not need an OTP, PIN, password or remote access. These design choices follow the credential-awareness rationale in RBI guidance [6]. Provider fraud controls remain essential. Commercial differentiation rests on accessible delivery and measurable service quality, rather than an unsupported promise of unique fraud detection.')

# 10 Alternatives and GTM
new('7 Alternatives and go to market plan')
p('Existing alternatives already address parts of the problem. Table 5 identifies where the proposed service would need to add measurable value. The comparison is a functional review of documented alternatives, not a scored market survey or proof that competitors lack similar capabilities.')
caption('Table 5. Alternatives and proposed differentiation')
table(['Alternative','Established role','Proposed additional value to test'],[
['Bank and RBI awareness campaigns [6]','Broad education through multiple communication channels.','Partner-specific local-language journeys, comprehension checks and repeat follow-up.'],
['In-app warnings such as Google Pay [7]','Warnings within payment flows. Google’s documentation describes alerts for suspicious requests.','Practice outside the transaction flow and assisted onboarding. Warning effectiveness must be tested rather than assumed.'],
['Bank support and official reporting channels [8]','Existing complaint handling and financial cyber-fraud reporting through the portal and helpline 1930.','Help users find verified routes quickly; never duplicate official investigation or imply guaranteed recovery.'],
['Institution builds the service itself','An internal product or training team is a practical make-or-buy alternative.','Reusable localized content and implementation support would need to beat the buyer’s internal cost and quality.'],
],[1.6,2.55,2.89],10)
h('7.1 Pilot before expansion',2)
p('Discovery and design, months 1-2. Seek one bank or merchant-network sponsor and agree on scope, access and a named budget owner. Conduct consent-based interviews and usability sessions with intended users; none have yet been conducted. Test current reporting journeys before designing additional steps. Use simulated payment scenarios without collecting account credentials.',boldlead='Discovery and design, months 1-2.')
p('Controlled pilot, months 3-5. Compare the companion with existing guidance where feasible. Prespecify outcomes: comprehension on unseen scenarios, successful identification of official support, completion and legitimate-task delay. Track staff time, accessibility failures and cost per supported institution. A separate power calculation is required before treating fraud loss as an evaluable outcome.',boldlead='Controlled pilot, months 3-5.')
p('Commercial gate and scale, month 6 onward. Ask the sponsor to assess paid renewal against the results and implementation burden. Scale to additional institutions only after a paid commitment, a manageable support load and acceptable security review. Use partner referrals and reusable integration modules; expand languages after demonstrating use. The projection’s customer counts are assumptions, not signed contracts.',boldlead='Commercial gate and scale, month 6 onward.')
note('The timing above is a proposed schedule. Effect sizes, sample size, go/no-go thresholds and partner commitments must be agreed before the pilot; no pilot outcome is claimed.')

# 11 unit economics
new('8 Illustrative financial model')
p('ILLUSTRATIVE ASSUMPTIONS TO BE VALIDATED. All prices, costs, customer counts and funding amounts in Sections 8-9 are planning assumptions. They are not measured in Findex, market quotations or forecasts. Figures use INR lakh (1 lakh = INR 100,000). The base subscription is INR 50,000 per institution per month for an agreed pilot-scale service scope; usage limits and extra support pricing require negotiation.',boldlead='ILLUSTRATIVE ASSUMPTIONS TO BE VALIDATED.')
caption('Table 6. Base unit economics and monthly cost assumptions')
table(['Input','Assumption','Treatment in the model'],[
['Monthly subscription per institution','INR 50,000','Recurring revenue; no setup fee'],
['Monthly variable delivery cost per institution','INR 10,000','Hosting, messaging and incremental delivery support'],
['Customer acquisition cost per new institution','INR 2 lakh','Incremental sales effort, travel, demonstrations and onboarding; expensed on acquisition'],
['Product and engineering team','INR 1.70 lakh / month','Fixed operating cost'],
['Content and localization maintenance','INR 0.40 lakh / month','Fixed operating cost'],
['Quality and security oversight','INR 0.35 lakh / month','Fixed operating cost'],
['Administration and core tools','INR 0.55 lakh / month','Fixed operating cost'],
['Total fixed operating cost in Year 1','INR 3.00 lakh / month','INR 36 lakh annually; grows 20% per year'],
],[2.62,1.65,2.77],10)
note('Acquisition spending excludes costs already classified as fixed; variable support excludes core quality oversight. Prelaunch development and evaluation appear only in the seed budget, not again in annual operating expenses. These boundaries prevent double counting.')
h('8.1 Contribution and break even',2)
p('Base monthly contribution per institution = INR 50,000 minus INR 10,000 = INR 40,000, an 80% contribution margin. Simple acquisition payback = INR 2 lakh / INR 0.40 lakh = 5 months, assuming full payment and no churn. This excludes fixed overhead and is not a claim about realized customer profitability.')
p('Steady-state break-even = INR 3 lakh / INR 0.40 lakh = 7.5, rounded up to 8 paying institutions. If one new institution is acquired each month, acquisition expense adds INR 2 lakh monthly: break-even becomes 12.5, rounded up to 13 institutions. Thus reaching eight customers does not guarantee annual cash break-even during growth.')
p('Validate price with budget-owning institutions, record acquisition effort and unsuccessful sales costs, and measure support intensity. No lifetime-value multiple is asserted because retention and contract renewal have not been observed. The model currently assumes no churn, which is particularly demanding over three years.')

# 12 scenarios
new('8.2 Three year scenario projections')
p('Each scenario starts with zero paying institutions and assumes linear growth within each year, no churn and constant scenario pricing. Average institutions = (opening + closing institutions) / 2. Conservative, base and optimistic monthly prices are INR 40,000, INR 50,000 and INR 60,000, respectively. Variable cost and acquisition cost remain as in Table 6.')
caption('Table 7. Illustrative revenue and operating cost projection in INR lakh')
rows=[]
for r in F['projection']:
    rows.append([r['scenario'] if r['year']==1 else '',str(r['year']),f"{r['average_institutions']:g} / {r['end_institutions']}",f"{r['revenue_lakh']:.2f}",f"{r['total_cost_lakh']:.2f}",f"{r['surplus_lakh']:.2f}"])
table(['Scenario','Year','Institutions\navg / closing','Revenue','Total\ncost','Surplus /\n(deficit)'],rows,[1.35,.48,1.47,1.15,1.25,1.34],9.9)
note('All values are assumptions or calculations from them. Negative surplus denotes a deficit. Annual total cost = fixed cost + 12 × average institutions × INR 0.10 lakh + new institutions × INR 2 lakh. Revenue = 12 × average institutions × monthly fee. Fixed annual cost is INR 36.00, 43.20 and 51.84 lakh in Years 1-3. Details are in Appendix A.')
fig('figure4.png','Figure 4. Illustrative annual operating surplus or deficit by scenario. Calculated from the assumptions in Tables 6-7; not an empirical result or probability-weighted forecast. INR lakh.')
p('The base case loses INR 32.80 lakh in Year 1, reaches annual operating break-even in Year 2 and generates INR 52.16 lakh in Year 3. The conservative case remains loss-making throughout. The optimistic case depends on faster institutional sales and a higher realized price; neither is evidenced by the survey.')
note('These are operating planning figures before tax, interest, depreciation, financing flows and prelaunch expenditure. They exclude pass-through taxes and assume collections keep pace with recognized revenue. Receivable delays and liquidity are addressed separately in the seed reserve. They are not audited accounts, valuation estimates or returns to investors.')

# 13 sensitivity
new('8.3 Sensitivity and financing implications')
p('Table 8 varies two inputs at a time while holding Year 1 fixed cost at INR 3 lakh per month. It reports the minimum whole number of institutions required for recurring operating break-even, excluding new-customer acquisition expense. The base assumption is the middle price and middle cost cell.')
caption('Table 8. Sensitivity of steady-state break-even institution count')
table(['Monthly variable cost\nper institution','Fee INR 40,000','Fee INR 50,000','Fee INR 60,000'],[
[f"INR {int(v*100000):,}"]+[str(next(r['breakeven_institutions'] for r in F['sensitivity'] if r['variable_cost_lakh']==v and r['price_lakh']==price)) for price in [.4,.5,.6]] for v in [.08,.1,.15]
],[2.36,1.56,1.56,1.56],10.5)
note('Formula: round up [INR 300,000 / (monthly fee minus monthly variable cost)]. All cells use unvalidated assumptions. Acquisition-related break-even is higher, as shown in Section 8.1.')
h('What changes the decision',2)
p('Pricing power. With a monthly variable cost of INR 10,000, reducing the fee from INR 50,000 to INR 40,000 increases the break-even count from 8 to 10. At ten institutions, the base fee yields INR 1 lakh monthly recurring operating surplus; the lower fee yields zero. Discounting therefore consumes the margin available to fund acquisition.',boldlead='Pricing power.')
p('Support intensity. If variable cost rises to INR 15,000 at the base fee, nine institutions are needed. Support requirements could increase with usage even if the number of institutional customers is unchanged. Contracts therefore need a measured service scope rather than unlimited support priced from an untested average.',boldlead='Support intensity.')
p('Growth expense. Acquiring institutions is not free. At the base fee and variable cost, a 50% higher acquisition cost of INR 3 lakh extends simple payback from 5 to 7.5 months. At one new institution per month, it raises break-even including acquisition expense to 15 active institutions.',boldlead='Growth expense.')
p('Renewal risk. The scenario table assumes no churn. Losing one base-priced institution reduces monthly contribution by INR 40,000 before any cost of replacing it. In Year 2, the base case has zero annual operating surplus, leaving no cushion for underperforming sales or renewal losses.',boldlead='Renewal risk.')
h('Revenue is not the same as available cash',2)
p('Institutional procurement and collection delays may create a funding gap even when operating results improve. At the base Year 1 closing run rate of eight institutions, two months of subscription revenue equal INR 8 lakh. A proposed INR 12 lakh working-capital reserve exceeds that simple receivables illustration, but it is not a month-by-month liquidity forecast. Actual payment terms, advance billing and tax timing must be added before fundraising.')
p('The financing decision should follow observed pilot cost and a credible sales pipeline. The sensitivity analysis prioritizes price, support load, acquisition cost and renewal validation; it does not establish the probabilities of any scenario.')

# 14 seed and risks
new('9 Funding needs and venture risks')
p('The illustrative seed request is INR 75 lakh. The proposed structure is staged equity or grant support for development and validation; no funding offer, valuation or ownership dilution is assumed. Fixed debt repayments would require a more reliable collection and renewal base than is currently evidenced.')
caption('Table 9. Illustrative seed budget and use of funds')
table(['Use of funds','INR lakh','Purpose'],[
['Year 1 base operating deficit','32.80','Net operating funding gap from Table 7'],
['Prelaunch product and integration','10.00','One-time build before commercial Year 1'],
['Prelaunch pilot and evaluation','5.00','User research, testing and independent review'],
['Working-capital reserve','12.00','Allowance for delayed collections and delivery timing'],
['Contingency and runway reserve','15.20','Buffer for slower sales and underestimated costs'],
['Total seed requirement','75.00','Illustrative planning envelope'],
],[2.65,1.05,3.34],10)
p('Release the INR 15 lakh prelaunch allocation against prototype and pilot milestones; the remaining INR 60 lakh would support launch, the base operating gap and reserves. The base model covers its Year 1 deficit within this envelope. In the conservative case, cumulative operating deficits plus prelaunch costs reach INR 81.80 lakh by the end of Year 2, exceeding the seed amount even before preserving working capital. Slower growth therefore requires a revised plan or additional funding.')
caption('Table 10. Key venture risks and responses')
table(['Risk','Practical response and evidence required'],[
['Weak willingness to pay or long procurement','Obtain a paid pilot or renewal commitment from a budget owner; stage hiring and track sales-cycle length.'],
['Support costs exceed subscription margin','Measure delivery hours and usage by institution; negotiate service limits and review variable cost.'],
['Incorrect advice or compromised links','Use partner-approved content, regular link checks, security review and an incident-response process.'],
['Exclusion or payment friction','Test local-language audio and assisted access; measure accessibility failures and legitimate-task delay.'],
['Dependence on one partner or easy imitation','Use reusable integrations and diversify paid relationships after the pilot. Demonstrate quality before claiming a defensible advantage.'],
],[2.05,4.99],10)
note('All spending allocations are proposed. No bank, merchant network, investor or public reporting body has been represented as an agreed partner. The research does not measure a total addressable market.')

# 15 conclusion and supplementary analysis
new('10 Discussion and conclusion')
p('India’s 2024 Findex evidence shows that broad account ownership coexists with lower digital payment use and uneven device protection. Higher reported request exposure among phone-owning payment users persists in an exploratory adjusted model. These findings identify questions for product testing rather than establish that digital finance causes fraud.')
p('The entrepreneurial case is strongest as a narrowly scoped institutional pilot: accessible safety guidance, verified support navigation and explicit measurement of usefulness and cost. The illustrative model shows why institutional willingness to pay and acquisition efficiency matter as much as the technical concept. A viable product must demonstrate additional value over existing campaigns, warnings and reporting channels.')
p('The next research step is consent-based work with merchants, users and institutional budget owners, followed by an evaluated pilot. Design-based uncertainty estimation would require additional survey-design information. A claim that the service reduces losses would require an adequately powered study of verified outcomes, beyond the present evidence.')
h('Appendix A Supplementary analysis')
caption('Table A1. Sending money among respondents who reported a request')
table(['Lock status among request recipients','Sent money\ncount','Valid n','Weighted\nshare'],[
statrow('Phone has a lock','Unsolicited request, phone lock=1: sent money'),
statrow('Phone has no lock','Unsolicited request, phone lock=2: sent money'),
statrow('All request recipients','Reported unsolicited request: con22'),
],[3.63,1.09,1.08,1.24],10)
note('Source: authors’ calculations from [2]. The two lock-status groups partition the 219 request recipients. Only 45 reported sending money, including six without a lock. Selection, unknown timing and confounding preclude a causal protection claim; this is not a population loss rate.')
caption('Table A2. Base-case cost bridge in INR lakh')
base=[r for r in F['projection'] if r['scenario']=='Base']
table(['Cost component','Year 1','Year 2','Year 3'],[
['New institutions acquired',*[str(r['new_institutions']) for r in base]],
['Fixed operating cost',*[f"{r['fixed_cost_lakh']:.2f}" for r in base]],
['Variable delivery cost',*[f"{r['variable_cost_lakh']:.2f}" for r in base]],
['Acquisition cost',*[f"{r['acquisition_cost_lakh']:.2f}" for r in base]],
['Total operating cost',*[f"{r['total_cost_lakh']:.2f}" for r in base]],
],[3.14,1.30,1.30,1.30],10)
note('Illustrative assumptions. Customer counts in the first row are counts, not monetary values. For completeness, the logistic model intercept odds ratio is '+model('Intercept')[0]+' (approximate 95% interval '+model('Intercept')[1]+'); it is a baseline model parameter, not a substantive population estimate.')

# 16 references and audit
new('References')
note('Numbered citation style is used throughout. Online sources were checked on 7 November 2026. The links below retain their complete destinations without forcing long URLs into narrow lines.')
refs=[
('[1] World Bank. (2025). The Global Findex Database 2025: Connectivity and Financial Inclusion in the Digital Economy.','Global Findex report','https://www.worldbank.org/en/publication/globalfindex/report'),
('[2] Development Research Group, Finance and Private Sector Development Unit, World Bank. (2025). India - The Global Findex Database 2025, 2024 survey. Ref. IND_2024_FINDEX_v02_M. Data downloaded 4 November 2026.','Dataset and documentation · DOI 10.48529/c9vy-pq51','https://doi.org/10.48529/c9vy-pq51'),
('[3] World Bank. (n.d.). India: Global snapshot of indicators and enabling regulations. Digital payment definition and published gender aggregates.','India digital finance dashboard','https://digitalfinance.worldbank.org/country/india'),
('[4] World Bank. (n.d.). Trust. Inclusive Digital Financial Services: A Reference Guide for Policymakers and Regulators.','Trust and digital financial literacy','https://digitalfinance.worldbank.org/topics/digital-financial-literacy/trust'),
('[5] World Bank. (n.d.). Financial Inclusion and Consumer Protection. Responsible Financial Access.','Responsible financial access overview','https://responsiblefinance.worldbank.org/en/responsible-finance'),
('[6] Reserve Bank of India. (2020, June 22). Increasing Instances of Payment Frauds - Enhancing Public Awareness Campaigns Through Multiple Channels. RBI/2019-20/256.','Official RBI circular PDF','https://www.rbi.org.in/commonman/Upload/English/Notification/PDFs/256CIRCULARE6521761166042728106B78DFA3D78A1.PDF'),
('[7] Kenghe, A. (2019, July 31). What’s under the hood: Security on Google Pay. Official Google India Blog. Used as a documented example of in-app warnings, not an independent effectiveness evaluation.','Google Pay security explanation','https://india.googleblog.com/2019/07/whats-under-hood-security-on-google-pay.html'),
('[8] Ministry of Home Affairs. (2022, April 6). Cyber Frauds Helpline. Press Information Bureau, Government of India. Release ID 1814120.','Official description of helpline 1930 and the reporting portal','https://www.pib.gov.in/PressReleasePage.aspx?PRID=1814120'),
]
for txt,label,url in refs:
    x=p(txt);x.paragraph_format.space_after=Pt(2);x.paragraph_format.keep_with_next=True
    for r in x.runs:r.font.size=Pt(10)
    x=p();link(x,label,url);x.paragraph_format.space_after=Pt(9)
    for r in x.runs:r.font.size=Pt(10)
h('Reproducibility record',2)
note('The analysis was rerun on 7 November 2026 using the original India file and analysis_group31.py. Both the weighted-results CSV and exploratory-model CSV match the previous outputs exactly. A full-precision audit file records weighted denominators, model sample size and data/script fingerprints. Report percentages and figures use these audited values. Financial projections and sensitivity calculations are separately reproducible and labelled as assumptions.')
note('The source dataset remains subject to its access conditions. The World Bank, Gallup and funders are not responsible for the authors’ interpretations. The financial concept, assumptions and recommendations are the authors’ proposals; no primary qualitative fieldwork or commercial validation is claimed.')

# Remove inherited title paragraph rules; keep the cover typographic and black.
for root in [doc.element,doc.styles.element]:
    for border in root.xpath('.//w:pBdr'):
        border.getparent().remove(border)
dest=OUT/'Group_31_Term_Paper_Revised.docx';doc.save(dest)
for filename in ['analysis_group31.py','Group_31_weighted_results.csv','Group_31_exploratory_model.csv','Group_31_analysis_audit.json','revision_finance.py']:
    shutil.copy2(filename,OUT/filename)
manifest={'abstract_words':len(abstract.split()),'expected_pages':16,'tables':10,'supplementary_tables':2,'figures':4,'author_names':['Rushal Verma','Vichanshu Raj','Sudhanshu'],'analysis_matches_previous':Path('baseline_weighted_results.csv').read_bytes()==Path('Group_31_weighted_results.csv').read_bytes() and Path('baseline_exploratory_model.csv').read_bytes()==Path('Group_31_exploratory_model.csv').read_bytes()}
(OUT/'verification.json').write_text(json.dumps(manifest,indent=2))
print(dest);print(manifest)

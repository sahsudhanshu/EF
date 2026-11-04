from docx import Document
from docx.shared import Inches,Pt
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from reportlab.platypus import SimpleDocTemplate, BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from xml.sax.saxutils import escape
import os,json
os.makedirs('Group_31/report',exist_ok=True)
sections=[
('Abstract','Using the 2024 India Global Findex survey (n = 3,000), we examine financial inclusion, digital payments and reported unsolicited money requests. Weighted account ownership was 89.0% and 48.5% made or received a digital payment. Among phone owners, 13.1% of digital-payment users and 4.3% of non-users reported an unsolicited request. An exploratory weighted logistic model gives an adjusted odds ratio of 3.45 (approximate 95% interval 2.24–5.30). These results are associational, and the interval does not account for full survey design. We propose a safety support service as a hypothesis to test.'),
('I. Introduction','Financial accounts can make it easier to receive payments, save and transact. Digital access can extend those benefits, but phone-based fraud and confusing payment instructions may undermine confidence. We ask how use differs from access, whether digital-payment users report more unsolicited requests, and which groups have less device protection. The survey concerns adults, not specifically entrepreneurs or businesses.'),
('II. Related work','The World Bank Global Findex describes access, use and digital connectivity [1]. Its survey asks phone owners whether their device has a PIN, password or fingerprint lock and whether an unknown person called or messaged asking for money [2]. A lock is one safety measure and cannot prevent all social engineering. The Reserve Bank of India advises customers not to share payment credentials [3].'),
('III. Data and methodology','The 2025 database contains the 2024 India survey, with 3,000 adult respondents and 199 variables [2]. We calculate weighted percentages using wgt. Derived account and anydigpayment indicators code 0 as no, don’t know or refusal. For raw safety variables, we exclude nonresponse and retain yes/no responses. Device lock and request exposure are measured among phone owners. The follow-up on sending money is restricted to respondents reporting an unsolicited request. Sample counts are unweighted.'),
('IV. Results','Among all adults, 89.0% had an account, 48.5% made or received a digital payment and 66.5% owned a phone. Among phone owners, 57.7% reported a device lock (n = 2,141) and 9.4% reported an unsolicited request (n = 2,145). Payment users had a request rate of 13.1% (n = 1,283) versus 4.3% for non-users (n = 862). Women and men had nearly equal account ownership, but payment use was 42.7% and 54.1%, respectively. The device-lock rate among phone owners was 50.3% for women and 62.7% for men.'),
('A. Differences by income and age','Digital payment use was 34.8% in the lowest household-income quintile and 67.4% in the highest. Among eligible phone owners, device lock use was 40.6% and 75.2%, respectively. Lock use among phone owners aged 60 or older was 22.9% (n = 154), compared with 75.7% among those aged 15–24 (n = 497). These estimates use different denominators and should not be interpreted as a causal effect of income or age. The weighted gaps identify areas for further investigation and product testing.'),
('B. Response to a request','Among 219 respondents reporting a request, 45 said that they sent money. The weighted proportion was 21.0% among those reporting a request. This follow-up is not a population-wide loss rate, does not verify whether a request was fraudulent, and has a relatively small number of positive responses. Comparing its subgroups may reflect selection or confounding and cannot establish that a phone lock prevents or increases losses.'),
('V. Adjusted analysis','A weighted logistic regression among phone owners (n = 2,145) controls for gender, age, education, income quintile, workforce participation and urban/rural residence. Digital-payment users had 3.45 times the odds of reporting a request (approximate 95% interval 2.24–5.30). Robust standard errors assume independent respondents because the public file lacks strata and primary sampling unit identifiers. Thus the interval and test are exploratory, not design-based. Odds are not risks; omitted factors, selection and reverse causation prevent causal interpretation.'),
('Qualitative interpretation','A focused review of World Bank guidance on trust and financial consumer protection, together with RBI fraud-awareness guidance [3–5], suggests that practical support, provider safeguards and timely redress may help users use financial services with confidence. These are interpretations of published sources, not interviews or survey comments. The survey cannot establish that distrust caused the adoption gap or that a device lock prevents deceptive requests.'),
('VI. Entrepreneurial implications','The observed gaps motivate testing a multilingual digital safety companion distributed through banks or payment providers. It could offer short explanations, a pre-payment checklist and verified links to assistance. It must never request a PIN or OTP. Demand, willingness to pay, the impact on actual losses and the cost of support remain untested. A pilot should measure comprehension, access to reporting and unintended friction before commercialization.'),
('VII. Limitations and conclusion','The survey is cross-sectional and self-reported. Digital payment includes receiving money, and an unsolicited request is not necessarily a banking scam or a verified loss. Only 45 of 219 exposed respondents reported sending money, limiting subgroup analysis. Broader device protection and survey-design information are needed. India shows high account ownership but lower digital use and uneven device protection; the relationship between payments and reported requests warrants further study.'),
('References','[1] World Bank, The Global Findex Database 2025, https://www.worldbank.org/en/publication/globalfindex/report.\n[2] World Bank, India Global Findex 2025 microdata, IND_2024_FINDEX_v02_M, https://doi.org/10.48529/c9vy-pq51.\n[3] Reserve Bank of India, Safeguards for Digital Banking, https://rbikehtahai.rbi.org.in/safeguards-for-digital-banking.html.\n[4] World Bank, Trust, https://digitalfinance.worldbank.org/topics/digital-financial-literacy/trust.\n[5] World Bank, Financial Consumer Protection, https://digitalfinance.worldbank.org/topics/financial-consumer-protection.')]
doc=Document(); sec=doc.sections[0]; sec.top_margin=sec.bottom_margin=Inches(.7); sec.left_margin=sec.right_margin=Inches(.75)
style=doc.styles['Normal']; style.font.name='Times New Roman'; style.font.size=Pt(10)
p=doc.add_paragraph(); p.alignment=1; r=p.add_run('Mobile Banking Financial Inclusion and Cybersecurity Risk in India'); r.bold=True;r.font.size=Pt(16)
p=doc.add_paragraph('Rushal Verma, Vichanshu Raj, Sudhanshu\nGroup 31, Entrepreneurial Finance');p.alignment=1
cols=sec._sectPr.xpath('./w:cols')[0]; cols.set(qn('w:num'),'2'); cols.set(qn('w:space'),'360')
for title,body in sections:
    doc.add_heading(title,level=2); doc.add_paragraph(body)
    if title=='IV. Results': doc.add_picture('Group_31/figures/fig2_exposure.png',width=Inches(3.2)); doc.add_paragraph('Fig. 1. Unsolicited requests among phone owners; weighted shares.')
doc.save('Group_31/report/IEEE_Report.docx')

# Export a typeset PDF of the longer paper from its editable document content.
pdfmetrics.registerFont(TTFont('PaperTimes','C:/Windows/Fonts/times.ttf')); pdfmetrics.registerFont(TTFont('PaperTimesBold','C:/Windows/Fonts/timesbd.ttf'))
S=getSampleStyleSheet(); S.add(ParagraphStyle(name='PaperTitle',parent=S['Title'],fontName='PaperTimesBold',fontSize=17,leading=21,alignment=TA_CENTER,spaceAfter=12)); S.add(ParagraphStyle(name='PaperBody',parent=S['BodyText'],fontName='PaperTimes',fontSize=10,leading=13,spaceAfter=6)); S.add(ParagraphStyle(name='PaperHeading',parent=S['Heading2'],fontName='PaperTimesBold',fontSize=12,leading=15,spaceBefore=9,spaceAfter=4)); S.add(ParagraphStyle(name='CompactBody',parent=S['PaperBody'],fontSize=9.2,leading=11.2,spaceAfter=3)); S.add(ParagraphStyle(name='CompactHeading',parent=S['PaperHeading'],fontSize=10.5,leading=12,spaceBefore=5,spaceAfter=2))
S['CompactHeading'].keepWithNext=True
def safe(s): return escape(s).replace('\n','<br/>')
def footer(c,d): c.setFont('Times-Roman',8); c.drawCentredString(306,32,'Group 31  |  Entrepreneurial Finance  |  '+str(d.page))
source=Document('Group_31_Term_Paper_Completed.docx'); story=[]
from docx.table import Table as DocTable
from docx.text.paragraph import Paragraph as DocPara
from docx.oxml.ns import qn as Q
for child in source.element.body.iterchildren():
    if child.tag==Q('w:p'):
        p=DocPara(child,source); txt=p.text.strip()
        if not txt: continue
        sty='PaperTitle' if p.style.name=='Title' else ('PaperHeading' if p.style.name.startswith('Heading') else 'PaperBody')
        story.append(Paragraph(safe(txt),S[sty]))
    elif child.tag==Q('w:tbl'):
        t=DocTable(child,source); rows=[[Paragraph(safe(c.text),S['PaperBody']) for c in row.cells] for row in t.rows]
        tab=Table(rows,repeatRows=1,colWidths=[150,85,85,110]); tab.setStyle(TableStyle([('GRID',(0,0),(-1,-1),.5,colors.grey),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e7edf3')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5)]));story.append(tab);story.append(Spacer(1,8))
story.append(PageBreak()); story.append(Paragraph('Appendix: Survey figures',S['PaperHeading']))
figure_files=['fig1_access_and_use.png','fig2_exposure.png','fig3_gender.png','fig4_income.png']
for filename in figure_files:
    story.append(Image('Group_31/figures/'+filename,width=6*inch,height=3.525*inch)); story.append(Spacer(1,10))
SimpleDocTemplate('Group_31/Research_Report.pdf',pagesize=(612,792),leftMargin=66,rightMargin=66,topMargin=60,bottomMargin=60).build(story,onFirstPage=footer,onLaterPages=footer)
source.add_page_break(); source.add_heading('Appendix Survey figures',level=1)
for filename in figure_files:
    source.add_picture('Group_31/figures/'+filename,width=Inches(6.1))
source.save('Group_31/Research_Report.docx')
# IEEE-style compact PDF, reading the same source sections as the editable report.
story=[]
for title,body in sections:
    story += [Paragraph(safe(title),S['CompactHeading']),Paragraph(safe(body),S['CompactBody'])]
    if title=='IV. Results': story += [Image('Group_31/figures/fig2_exposure.png',width=2.8*inch,height=1.645*inch),Paragraph('Fig. 1. Weighted unsolicited-request rate among phone owners.',S['CompactBody'])]
def ieee_page(c,doc):
    footer(c,doc)
    if doc.page==1:
        c.setFont('PaperTimesBold',15); c.drawCentredString(306,747,'Mobile Banking Financial Inclusion and')
        c.drawCentredString(306,729,'Cybersecurity Risk in India')
        c.setFont('PaperTimes',10); c.drawCentredString(306,709,'Rushal Verma, Vichanshu Raj, Sudhanshu')
        c.drawCentredString(306,695,'Group 31, Entrepreneurial Finance')
first=[Frame(48,52,247,625,id='left1',leftPadding=0,rightPadding=0),Frame(317,52,247,625,id='right1',leftPadding=0,rightPadding=0)]
later=[Frame(48,52,247,688,id='left',leftPadding=0,rightPadding=0),Frame(317,52,247,688,id='right',leftPadding=0,rightPadding=0)]
from reportlab.platypus import NextPageTemplate
story.insert(0,NextPageTemplate('later'))
pdf=BaseDocTemplate('Group_31/report/IEEE_Report.pdf',pagesize=(612,792));pdf.addPageTemplates([PageTemplate(id='first',frames=first,onPage=ieee_page),PageTemplate(id='later',frames=later,onPage=ieee_page)]);pdf.build(story)

# The notebook contains executable source, not copied outputs or bundled microdata.
code=open('analysis_group31.py',encoding='utf-8').read()
nb={'cells':[{'cell_type':'markdown','metadata':{},'source':['# Group 31: Financial inclusion and digital safety in India\n','Run from the project root with the licensed India data file at `data/Findex_Microdata_2025_updateIndia.dta`. The estimates are weighted. Model intervals assume independent respondents and are not design-based.']},{'cell_type':'code','execution_count':None,'metadata':{},'outputs':[],'source':code.splitlines(keepends=True)}], 'metadata':{'kernelspec':{'display_name':'Python 3','language':'python','name':'python3'},'language_info':{'name':'python','version':'3.11'}},'nbformat':4,'nbformat_minor':5}
with open('Group_31/analysis.ipynb','w',encoding='utf-8') as f: json.dump(nb,f,ensure_ascii=False,indent=1)

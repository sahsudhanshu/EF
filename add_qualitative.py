from docx import Document
from docx.oxml import OxmlElement
from docx.text.paragraph import Paragraph
path='Group_31_Term_Paper_Completed.docx'
d=Document(path)
anchor=next(p for p in d.paragraphs if p.text=='6 Entrepreneurial opportunity')
def insert(text,style=None):
    e=OxmlElement('w:p'); anchor._p.addprevious(e); p=Paragraph(e,anchor._parent)
    if style:p.style=style
    p.add_run(text)
insert('5.4 Qualitative interpretation of published sources','Heading 2')
insert('Method and scope. This is a focused interpretive review of three public institutional sources, selected for their relevance to trust, consumer protection and fraud prevention: the World Bank discussion of trust [8], its financial consumer protection guidance [9], and the Reserve Bank of India’s awareness circular [10]. The sources were read for recurring mechanisms and design implications. This is not a systematic review or an analysis of interviews, survey comments or focus groups; no primary qualitative fieldwork was conducted. The themes below are interpretations, not claims that the survey respondents expressed these views.')
insert('Theme 1 Access must become confident use. The World Bank describes trust, awareness and dispute resolution as factors that support adoption [8]. The survey shows high account ownership but lower digital payment use. Together these observations make it reasonable to investigate how trust and usability influence the transition from account access to active use. They do not establish that distrust caused the measured gap: phone access, affordability, preferences and other factors could also matter.')
insert('Theme 2 Safety depends on the provider as well as the user. The World Bank emphasizes disclosure, fair treatment and complaint mechanisms as parts of consumer protection [9]. RBI’s awareness circular describes recurring fraud methods, including requests for payment credentials and malicious links [10]. In the present data, a device lock is a limited safeguard: it cannot establish whether a user will recognize a deceptive instruction. A useful service should therefore combine understandable guidance with verified support channels and provider-side controls rather than assume a lesson alone will prevent fraud.')
insert('Theme 3 Inclusion requires accessible support. The descriptive differences by gender, income and age suggest that a single smartphone-first interface may not fit all users. This is a design hypothesis rather than a finding about individual preferences. Interviews in local languages, testing on inexpensive devices, and observation of how people find help could identify barriers before a product is launched. Participants should not be asked to share credentials or disclose actual account details.')
insert('Interpretive synthesis. The quantitative pattern identifies where further investigation is warranted; the literature suggests plausible mechanisms and service features. Neither establishes a market size, a causal effect of a safety tool, or proof that the proposed venture is commercially viable. A pilot should test both adoption and unintended effects, including whether warnings delay legitimate transactions.')
refs=next(p for p in d.paragraphs if p.text.startswith('[7] World Bank. Global Findex'))
for text in [
'[8] World Bank. Trust, Digital Finance Inclusion. https://digitalfinance.worldbank.org/topics/digital-financial-literacy/trust',
'[9] World Bank. Financial Consumer Protection, Digital Finance Inclusion. https://digitalfinance.worldbank.org/topics/financial-consumer-protection',
'[10] Reserve Bank of India. Increasing Instances of Payment Frauds: Enhancing Public Awareness Campaigns Through Multiple Channels, 22 June 2020. https://www.rbi.org.in/commonman/Upload/English/Notification/PDFs/256CIRCULARE6521761166042728106B78DFA3D78A1.PDF']:
    p=d.add_paragraph(text)
d.save(path)

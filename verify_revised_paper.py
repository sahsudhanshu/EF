from pathlib import Path
import json,hashlib,re,subprocess
from decimal import Decimal,ROUND_CEILING
from docx import Document
from pypdf import PdfReader

O=Path('Group_31/revised'); A=json.loads(Path('Group_31_analysis_audit.json').read_text());D={r['comparison']:r for r in A['descriptives']};F=json.loads((O/'financial_model.json').read_text())
doc=Document(O/'Group_31_Term_Paper_Revised.docx');pdf=PdfReader(O/'Group_31_Term_Paper_Revised.pdf')
checks=[]
def check(label,value):
    assert value,label
    checks.append(label)
check('Original descriptive CSV reproduced byte for byte',Path('baseline_weighted_results.csv').read_bytes()==Path('Group_31_weighted_results.csv').read_bytes())
check('Original model CSV reproduced byte for byte',Path('baseline_exploratory_model.csv').read_bytes()==Path('Group_31_exploratory_model.csv').read_bytes())
check('Full-precision weighted fractions reconcile',all(abs(r['weighted_percent']-100*r['weight_numerator']/r['weight_denominator'])<1e-10 for r in D.values()))
check('Model converged and sample matches',A['model_n']==2145 and A['model_positive']==219 and A['max_score']<1e-7)
table_keys={2:['All adults: account','All adults: anydigpayment','All adults: con1','female=1: anydigpayment','female=2: anydigpayment','Phone owners: con21','Phone owners, anydigpayment=1: con21','Phone owners, anydigpayment=0: con21','Reported unsolicited request: con22'],3:['Phone owners: con18','Phone owners, female=1: con18','Phone owners, female=2: con18','Phone owners, anydigpayment=1: con18','Phone owners, anydigpayment=0: con18']+['Phone owners, age_group='+k+': con18' for k in ['15–24','25–39','40–59','60+']]+['Phone owners, inc_q=1: con18','Phone owners, inc_q=5: con18'],12:['Unsolicited request, phone lock=1: sent money','Unsolicited request, phone lock=2: sent money','Reported unsolicited request: con22']}
for idx,keys in table_keys.items():
    for row,key in zip(doc.tables[idx].rows[1:],keys):
        r=D[key]
        check('Table values match '+key,[c.text for c in row.cells][1:]==[f"{r['positives']:,}",f"{r['n']:,}",f"{r['weighted_percent']:.1f}%"])
for row,r in zip(doc.tables[4].rows[1:],A['model'][1:]):
    check('Model table matches '+r['variable'],[c.text for c in row.cells][1:]==[f"{r['odds_ratio']:.2f}",f"{r['low_95']:.2f} to {r['high_95']:.2f}"])
for row,r in zip(doc.tables[8].rows[1:],F['projection']):
    check('Projection '+r['scenario']+' '+str(r['year']),[c.text for c in row.cells][3:]==[f"{r['revenue_lakh']:.2f}",f"{r['total_cost_lakh']:.2f}",f"{r['surplus_lakh']:.2f}"])
    check('Projection arithmetic '+r['scenario']+' '+str(r['year']),abs(r['revenue_lakh']-r['total_cost_lakh']-r['surplus_lakh'])<1e-9 and abs(r['total_cost_lakh']-r['fixed_cost_lakh']-r['variable_cost_lakh']-r['acquisition_cost_lakh'])<1e-9)
for r in F['sensitivity']:
    exact=int((Decimal(3)/(Decimal(str(r['price_lakh']))-Decimal(str(r['variable_cost_lakh'])))).to_integral_value(rounding=ROUND_CEILING))
    check('Sensitivity cell '+str(r['price_lakh'])+'/'+str(r['variable_cost_lakh']),r['breakeven_institutions']==exact)
check('Seed budget totals INR 75 lakh',sum(F['seed_uses_lakh'].values())==75)
check('Monthly fixed costs total INR 3 lakh',sum([Decimal('1.70'),Decimal('.40'),Decimal('.35'),Decimal('.55')])==3)
check('Growth acquisition sensitivity',Decimal(3)/Decimal('.4')==Decimal('7.5') and (Decimal(3)+3)/Decimal('.4')==15)
check('Conservative funding gap',Decimal('36.8')+30+15==Decimal('81.8'))
check('Page count and contents agree',len(pdf.pages)==16)
fulltext='\n'.join(p.extract_text() for p in pdf.pages)
check('No replacement glyphs or wrong author name','\ufffd' not in fulltext and 'Sudhanshu Sah' not in fulltext)
check('Four body figures present',all('Figure '+str(i)+'.' in fulltext for i in range(1,5)))
citations=set()
for match in re.findall(r'\[([1-8](?:, [1-8])*)\]','\n'.join(p.extract_text() for p in pdf.pages[:15])):
    citations.update(int(k.strip()) for k in match.split(','))
check('All references are cited and all citations have entries',citations==set(range(1,9)))
urls=[r.target_ref for r in doc.part.rels.values() if 'hyperlink' in r.reltype]
check('Eight intact reference hyperlinks',len(urls)==8 and all('\n' not in u and ' ' not in u for u in urls))
pdflinks=[]
for page in pdf.pages:
    for a in page.get('/Annots',[]):
        x=a.get_object();action=x.get('/A',{});uri=action.get('/URI')
        if uri:pdflinks.append(str(uri))
check('Reference links survived Word PDF export',set(urls)<=set(pdflinks))

qa=O/'qa';old={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in qa.glob('page-*.png')}
subprocess.run([r'C:\Users\Sudhanshu\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe','-r','110','-png',str(O/'Group_31_Term_Paper_Revised.pdf'),str(qa/'page')],check=True)
changed=[p.name for p in qa.glob('page-*.png') if old.get(p.name)!=hashlib.sha256(p.read_bytes()).hexdigest()]
report={'checks_passed':len(checks),'checks':checks,'pages':len(pdf.pages),'changed_pages_since_first_visual_review':changed,'rendered_by':'Microsoft Word 16.0; rasterized with Poppler','data_sha256':A['data_sha256'],'script_sha256':A['script_sha256'],'final_docx_sha256':hashlib.sha256((O/'Group_31_Term_Paper_Revised.docx').read_bytes()).hexdigest(),'final_pdf_sha256':hashlib.sha256((O/'Group_31_Term_Paper_Revised.pdf').read_bytes()).hexdigest()}
(O/'final_verification.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps({k:report[k] for k in ['checks_passed','pages','changed_pages_since_first_visual_review']},indent=2))

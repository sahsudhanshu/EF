from docx import Document
for name in ['Group_31_Term_Paper_Completed.docx','Group_31_Term_Paper.docx']:
    doc=Document(name)
    for p in doc.paragraphs:
        for run in p.runs:
            run.text=run.text.replace('Sudhanshu Sah','Sudhanshu')
    doc.save(name)

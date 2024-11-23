import docx 
doc = docx.Document('lion.docx')
lenpar = len(doc.paragraphs)
print(lenpar)
par1t = doc.paragraphs[0].runs[0].text
data =(par1t)


import PyPDF2
pdfFileObj = open('constituicao_ingles_3ed.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

allpages = (pdfReader.numPages)

alltext = ""
#colocar isso em parametro
x = open('constituicao_ingles_3ed.pdf.txt',"w")

for page in range(allpages):
	pageObj = pdfReader.getPage(page)
	thispage = pageObj.extractText()
	print(thispage)
	try:
		x.write(thispage)
	except:
		x.write("EEERRROOORRR")	
	alltext += thispage


x.close()




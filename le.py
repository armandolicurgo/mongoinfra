#*-* coding: utf-8 *-*

def uread(filename, encoding='utf-8', errors='strict'):
	with open(filename, 'rb') as f:
		return f.read().decode(encoding, errors=errors)

def uwrite(content, filename, encoding='utf-8', errors='strict'):
	with open(filename, 'wb') as f:
		f.write(str(content).encode(encoding, errors=errors))
	return True


from bs4 import BeautifulSoup

html_doc = uread("x.htm")

soup = BeautifulSoup(html_doc, "html.parser")
print(soup.get_text())


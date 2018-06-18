import string
from pymongo import MongoClient
from selenium import webdriver
import json
from datetime import datetime


from bson.objectid import ObjectId


def logar(pp):
	now = datetime.now()
	fl = open("get.log","a")
	fl.write(""+pp+"\n")
	fl.close()


def palavras(pp):
	palavras = {}
	r = json.dumps(palavras)
	return (r)


def mongar(urll,tit,ini, fim):
	fff= open(  "saida.txt","r")
	tx = fff.read()
	tx = tx.replace("\n\n"," ")
	tx = tx.replace("  "," ")
	fff.close()
	cliente = MongoClient('localhost', 27017)
	#print(dir(cliente))
	banco = cliente.test
	#print(dir(banco))
	pal = palavras(tx)
	coletado = {"coletado": tx, "palavras": pal, "url":  urll, "titulo": tit , "inicio": ini ,"fim": fim,  "ver": 9}
	alb = banco.coletar
	m_id = alb.insert_one(coletado).inserted_id
	#print( m_id )
	return(m_id)




def getjob(pp):
	cliente = MongoClient('localhost', 27017)
	banco = cliente.test
	coletado = {"job1": 2 , "ativo": 1, "repetir": 1}
	alb = banco.coletado
	m_id = alb.find_one(coletado)
	#print( m_id )
	return(m_id['urls'])

def getjobb(pp):
        d = open("sites.txt","r")
        rr = d.read()
        d.close()
        return(rr)


options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument("window-size=1920x1080")

driver = webdriver.Chrome(chrome_options=options)


urls = getjobb(1)

sites = urls

"""
print("=" * 70)
print(sites)
print("=" * 70)

"""


conta = 0
ff= open(  "get.txt","w")
for site in sites.split("\n"):
	inicio = datetime.now()
	logar(site)
	driver.get(site)
	print(driver.title)
	titulo = "" + driver.title
	conta += 1
	#driver.save_screenshot("img" + str(conta) + ".png")
	tx = driver.find_elements_by_xpath("//a")
	for txt in tx:
		try :
			ff.write(str(txt.text)+"\n")
		except:
			ff.write("eerrrroo"+"\n")	
	ff.close()
	fim = datetime.now()
	oid = mongar(site, titulo, (inicio.hour*24*60+inicio.minute*60+inicio.second), (fim.hour*24*60+fim.minute*60+fim.second)-(inicio.hour*24*60+inicio.minute*60+inicio.second))
	driver.save_screenshot("d:/img/" + ObjectId(oid).__str__() + ".png")	
	ff= open(  "get.txt","w")
ff.close()
driver.close()


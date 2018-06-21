#crud.py
# implementa crud database
# crud.py -init database
# crud.py -init database colection1 colection2 colection3
# crud.py 
#import pymongo
import json
import string
from pymongo import MongoClient



class Crud():
	um crud para cada collection
	cliente = `` # nao inicializado
	
	def init(url=``,collect=``):
		cliente = MongoClient(url)
		return cliente
	def c(jso):
		pass # return _id
	def r(id):
		pass # return jso
	def u(id):
		pass # return jso
	def d(id):
		pass # return js
	def open(url):
		cliente = MongoClient(url)
		return cliente
	def sync(dic,jso):
  	pass
	def dodefault():
		crd = Crud('mongodb://localhost:27017/','test')
  	
        def Consulta1(self):
                #import string
                #from pymongo import MongoClient

                ff= open(  "consulta1.txt","w")

                client = MongoClient('localhost', 27017)
                query = {"ver": {"$gt" : 6}}
                campos = {"coletado": 1,"url": 1,"inicio": 1, "fim": 1}
                ff.close()
                database = client["test"]
                collection = database["coletados"]

                # Created with Studio 3T, the IDE for MongoDB - https://studio3t.com/

                maxi = 10000
                i=0
                cursor = collection.find(query, campos)
                try:
                        for doc in cursor:
                                i+=1
                                if (i < maxi):
                                        print( doc )
                finally:
                    client.close()

		
        def Consulta2Grafico(self):
                #import string
                #from pymongo import MongoClient
                #import matplotlib.pyplot as plt
                ff= open(  "consulta1.txt","w")
                cliente = MongoClient('localhost', 27017)
                banco = cliente.test

                coletado = {"ver" :  8 }
                campos = {"url": 1,"inicio": 1, "fim": 1}
                sr = {"url": 1,"inicio": 1}

                alb = banco.coletados
                m_id = alb.find(coletado, campos)
                print( m_id )
                x,y = [],[]
                for kk in m_id:
                        i =int(kk['inicio'])
                        f =int(kk['fim'])
                        print( i , f)
                        if (0 < f < 1000):
                                x.append(i)
                                y.append(f)

                ff.close()

                plt.style.use('seaborn-whitegrid')
                fig,ax = plt.subplots()
                ax.plot(x, y,"bo")
                plt.show()

"""        import string
        from pymongo import MongoClient
        from selenium import webdriver
        import json
        from datetime import datetime
"""

        from bson.objectid import ObjectId

        def mongar(st):
                cliente = MongoClient('localhost', 27017)
                banco = cliente.test
                job = {"job1": 1,  "urls":  st, "ativo": 1, "repetir": 1}
                alb = banco.coletados
                m_id = alb.insert_one(job).inserted_id
                #print( m_id )
                return(m_id)

        def fazer():
                sites = """http://bigdata-madesimple.com/top-50-open-source-web-crawlers-for-data-mining/"""
                ossites = {"job" : sites.split("\n")}
                oid = mongar(sites)
                            
        def mongar2(st):
                cliente = MongoClient('localhost', 27017)
                banco = cliente.test
                job = {"job1": 2,  "urls":  st, "ativo": 1, "repetir": 1}
                alb = banco.coletados
                m_id = alb.insert_one(job).inserted_id
                #print( m_id )
                return(m_id)


        def fazer2():
                sites = """

                txt = """analise multi variada
                tensorflow pca"""

                txt = txt.replace(" ","+")
                goog = """https://www.google.com/search?q="""
                sites = ""
                for um in txt.split("\n"):
                        sites = sites + (goog+um+"\n")

                ossites = {"job" : sites.split("\n")}
                oid = mongar2(sites)

#crud.py
import json
import string
from pymongo import MongoClient

interf = """/test/coletados/_id/ 
/test/coletados/
/test/jobs/_id/
/test/jobs/"""
interf = interf.split("\n")



class Crud():
	cliente = ''
	def trata(self,suported,solicited):
		print(suported)
		print(solicited)
		return('{"ret","implementar as consultas json"}')

	def __init__(self,u='mongodb://localhost:27017/',c='test'):
		cliente = MongoClient(u)
	def dodefault(self):
		crd = Crud('mongodb://localhost:27017/','test')	
	def Consulta1(self):
		ff= open(  "consulta1.txt","w")
		client = MongoClient('localhost', 27017)
		query = {"ver": {"$gt" : 6}}
		campos = {"coletado": 1,"url": 1,"inicio": 1, "fim": 1}
		ff.close()
		database = client["test"]
		collection = database["coletados"]
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

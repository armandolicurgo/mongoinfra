#crud.py
# implementa crud database
# crud.py -init database
# crud.py -init database colection1 colection2 colection3
# crud.py 
import pymongo
import json


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
  	

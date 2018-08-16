# Requires pymongo 3.6.0+
from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId
from flask import render_template, jsonify


def connectionString():
    return "mongodb://localhost:27017/"


def connectionDatabase():
    return "test"


def connectionCollection():
    return "csh_clientes"


def insertDocument(query):
    client = MongoClient(connectionString())
    database = client[connectionDatabase()]
    collection = database[connectionCollection()]
    oid = collection.insert_one(query).inserted_id
    client.close()
    return oid


def updateDocument(idpart,query):
    client = MongoClient(connectionString())
    database = client[connectionDatabase()]
    collection = database[connectionCollection()]
    cursor = collection.update(idpart,query )
    client.close()

def deleteDocument(idpart):
    client = MongoClient(connectionString())
    database = client[connectionDatabase()]
    collection = database[connectionCollection()]
    cursor = collection.delete_one(idpart )
    client.close()


def getAllDocumentsHTML(sort):
    client = MongoClient(connectionString())
    database = client[connectionDatabase()]
    collection = database[connectionCollection()]
    if sort == "":
        query = {}
        sortthis = [(u"customer", 1)]
        cursor = collection.find(query)
    else:
        query = {}
        sortthis = [(u"city", 1)]
        cursor = collection.find(query, sort=sortthis)
    allDocuments = ""
    try:
        for doc in cursor:
            objectid = ObjectId(doc['_id']).__str__()
            customer = (doc['customer'])
            customerid = (doc['customerid'])
            address = (doc['address'])
            address2 = (doc['address2'])
            city = (doc['city'])
            document_ = (doc['document_'])
            state_ = (doc['state_'])
            phone = (doc['phone'])
            contact = (doc['contact'])
            credit = (doc['credit'])
            allDocuments += render_template("eachdoc.html",
                                            id_=objectid,
                                            document_=document_,
                                            state_=state_,
                                            customer=customer,
                                            customerid=customerid,
                                            address=address,
                                            address2=address2,
                                            city=city,
                                            phone=phone,
                                            contact=contact,
                                            credit=credit)
    finally:
        client.close()
    return '<!DOCTYPE html><table style="width:80%">"' + allDocuments + "</table>"

def getAllDocumentsJSON(sort):
    client = MongoClient(connectionString())
    database = client[connectionDatabase()]
    collection = database[connectionCollection()]
    if sort == "X":
        query = {}
        sortthis = [(u"customer", 1)]
        cursor = collection.find(query)
    else:
        query = {}
        sortthis = [(u"city", 1)]
        cursor = collection.find(query, sort=sortthis)
    allDocuments = []
    try:
        for doc in cursor:
            it = {"_id" : ObjectId(doc['_id']).__str__(),
                "customer" : (doc['customer']),
                "customerid" : (doc['customerid']),
                "address" : (doc['address']),
                "address2" : (doc['address2']),
                "city" : (doc['city']),
                "document_" : (doc['document_']),
                "state_" : (doc['state_']),
                "phone" : (doc['phone']),
                "contact" : (doc['contact']),
                "credit" : (doc['credit'])}
            allDocuments.append(it)
    finally:
        client.close()
    return jsonify(allDocuments)


def getDocumentHTML(objectid):
    client = MongoClient(connectionString())
    database = client[connectionDatabase()]
    collection = database[connectionCollection()]
    query = {}
    cursor = collection.find({"_id": ObjectId(objectid)})
    allDocuments = ""
    try:
        for doc in cursor:
            objectid = ObjectId(doc['_id']).__str__()
            customer = (doc['customer'])
            customerid = (doc['customerid'])
            address = (doc['address'])
            address2 = (doc['address2'])
            city = (doc['city'])
            document_ = (doc['document_'])
            state_ = (doc['state_'])
            phone = (doc['phone'])
            contact = (doc['contact'])
            credit = (doc['credit'])
            allDocuments += render_template("customer2.html",
                                            id_=objectid,
                                            document_=document_,
                                            state_=state_,
                                            customer=customer,
                                            customerid=customerid,
                                            address=address,
                                            address2=address2,
                                            city=city,
                                            phone=phone,
                                            contact=contact,
                                            credit=credit)
    finally:
        client.close()
    return allDocuments


def dropDocuments():
    client = MongoClient(connectionString())
    database = client[connectionDatabase()]
    collection = database[connectionCollection()]
    query = {}
    cursor = collection.remove(query)
    """try:
		for doc in cursor:
			print(doc)
	finally:
		client.close()
	"""
    client.close()

    
    


def connection2String():
    return "mongodb://localhost:27017/"


def connection2Database():
    return "test"


def connection2Collection():
    return "csh_stock"


def insert2Document(query):
    client = MongoClient(connection2String())
    database = client[connection2Database()]
    collection = database[connection2Collection()]
    oid = collection.insert_one(query).inserted_id
    client.close()
    return oid


def update2Document(idpart,query):
    client = MongoClient(connection2String())
    database = client[connection2Database()]
    collection = database[connection2Collection()]
    cursor = collection.update(idpart,query )
    client.close()

def delete2Document(idpart):
    client = MongoClient(connection2String())
    database = client[connection2Database()]
    collection = database[connection2Collection()]
    cursor = collection.delete_one(idpart )
    client.close()


def getAllDocuments2HTML(sort):
    client = MongoClient(connection2String())
    database = client[connection2Database()]
    collection = database[connection2Collection()]
    if sort == "":
        query = {}
        sortthis = [(u"product", 1)]
        cursor = collection.find(query)
    else:
        query = {}
        sortthis = [(u"city", 1)]
        cursor = collection.find(query, sort=sortthis)
    allDocuments = ""
    try:
        for doc in cursor:
            objectid = ObjectId(doc['_id']).__str__()
            product = (doc['Product'])
            productid = (doc['ProductId'])
            group = (doc['Group'])
            price = (doc['Price'])
            packing = (doc['Packing'])
            unitperpack = (doc['UnitPerPack'])
            credit = (doc['Credit'])
            available = (doc['Available'])
            allDocuments += render_template("eachproduct.html",
                                            id_=objectid,
                                            product=product,
                                            productid=productid,
                                            group=group,price=price,packing=packing,
                                            unitperpack=unitperpack,available=available,
                                            credit=credit)
    finally:
        client.close()
    return '<!DOCTYPE html><table style="width:80%">"' + allDocuments + "</table>"

def getAllDocuments2JSON(sort):
    client = MongoClient(connection2String())
    database = client[connection2Database()]
    collection = database[connection2Collection()]
    if sort == "X":
        query = {}
        sortthis = [(u"product", 1)]
        cursor = collection.find(query)
    else:
        query = {}
        sortthis = [(u"city", 1)]
        cursor = collection.find(query, sort=sortthis)
    allDocuments = []
    try:
        for doc in cursor:
            it = {"_id" : ObjectId(doc['_id']).__str__(),
                "product" : (doc['Product']),
                "productid" : (doc['ProductId']),
                "address" : (doc['Address']),
                "address2" : (doc['Address2']),
                "city" : (doc['City']),
                "document_" : (doc['Document_']),
                "state_" : (doc['State_']),
                "phone" : (doc['Phone']),
                "contact" : (doc['Contact']),
                "credit" : (doc['credit'])}
            allDocuments.append(it)
    finally:
        client.close()
    return jsonify(allDocuments)


def getDocument2HTML(objectid):
    client = MongoClient(connection2String())
    database = client[connection2Database()]
    collection = database[connection2Collection()]
    query = {}
    cursor = collection.find({"_id": ObjectId(objectid)})
    allDocuments = ""
    try:
        for doc in cursor:
            objectid = ObjectId(doc['_id']).__str__()
            product = (doc['Product'])
            productid = (doc['ProductId'])
            group = (doc['Group'])
            price = (doc['Price'])
            packing = (doc['Packing'])
            unitperpack = (doc['UnitPerPack'])
            available = (doc['Available'])
            credit = (doc['Credit'])
            allDocuments += render_template("product2.html",
                                            id_=objectid,
                                            product=product,
                                            productid=productid,
                                            group=group,
                                            price=price,
                                            packing=packing,
                                            unitperpack=unitperpack,
                                            available=available,
                                            credit=credit)
    finally:
        client.close()
    return allDocuments


def drop2Documents():
    client = MongoClient(connection2String())
    database = client[connection2Database()]
    collection = database[connection2Collection()]
    query = {}
    cursor = collection.remove(query)
    """try:
		for doc in cursor:
			print(doc)
	finally:
		client.close()
	"""
    client.close()

    
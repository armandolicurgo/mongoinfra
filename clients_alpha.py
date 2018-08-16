# Requires pymongo 3.6.0+
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
#client = MongoClient("mongodb://host:port/")

database = client["test"]
collection = database["csh_clients"]

# Created with Studio 3T, the IDE for MongoDB - https://studio3t.com/

query = {}
sort = [ (u"Client", 1) ]

cursor = collection.find(query, sort = sort)
try:
    for doc in cursor:
        print(doc)
finally:
    client.close()


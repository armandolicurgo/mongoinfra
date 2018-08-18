# Requires pymongo 3.6.0+
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
database = client["test"]
collection = database["csh_clients"]

#select City, count(*)
#from csh_clients group by City;

# Created with Studio 3T, the IDE for MongoDB - https://studio3t.com/

pipeline = [
    {
        u"$group": {
            u"_id": {
                u"City": u"$City"
            },
            u"COUNT(*)": {
                u"$sum": 1
            }
        }
    }, 
    {
        u"$project": {
            u"_id": 0,
            u"City": u"$_id.City",
            u"COUNT(*)": u"$COUNT(*)"
        }
    }, 
    {
        u"$project": {
            u"_id": 0,
            u"City": u"$City",
            u"COUNT(*)": u"$COUNT(*)"
        }
    }
]

cursor = collection.aggregate(
    pipeline
)
try:
    for doc in cursor:
        print(doc)
finally:
    client.close()


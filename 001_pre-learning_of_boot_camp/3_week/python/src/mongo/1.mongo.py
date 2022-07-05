from pymongo import MongoClient

client = MongoClient('Mongo URL')
db = client.dbsparta

doc = {
    'name': 'unchaptered',
    'age': 27
}

db.users.insert_one(doc)
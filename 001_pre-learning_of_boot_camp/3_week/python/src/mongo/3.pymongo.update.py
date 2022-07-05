from pymongo import MongoClient

client = MongoClient('Mongo URL')
db = client.dbsparta 

resultMovie = db.movies.update_one({ 'title': '가버나움' }, { '$set': { 'point': '0.00' } })

print(resultMovie)
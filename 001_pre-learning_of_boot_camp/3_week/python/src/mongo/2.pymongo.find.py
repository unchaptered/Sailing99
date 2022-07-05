from pymongo import MongoClient

client = MongoClient('Mongo URL')
db = client.dbsparta 

targetMovie = db.movies.find_one({ 'title': '가버나움' })
resultMovie = db.movies.find_one({ 'point': targetMovie['point'] })

print(targetMovie)
print(resultMovie)
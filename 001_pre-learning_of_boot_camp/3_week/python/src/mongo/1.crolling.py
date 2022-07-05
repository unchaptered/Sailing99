import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

# Crolling
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}
data = requests.get(
    'https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',
    headers = headers
)

soup = BeautifulSoup(data.text, 'html.parser')
movies = soup.select('#old_content > table > tbody > tr')

# Database
client = MongoClient('Mongo URL')
db = client.dbsparta

for movie in movies:
    target = movie.select_one('td.title > div > a')
    if target is not None:
        title = target.text
        point = movie.select_one('td.point').text
        ranking = movie.select_one('td:nth-child(1) > img')['alt']
        doc = {
            'title': title,
            'point': point,
            'ranking': ranking
        }
        db.movies.insert_one(doc)
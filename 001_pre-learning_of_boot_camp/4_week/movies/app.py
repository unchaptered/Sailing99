import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
client = MongoClient('Mongo URL')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/movie', methods=['POST'])
def movie_post():
    data = requests.get(
        request.form['url'],
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    )

    soup = BeautifulSoup(data.text, 'html.parser')

    db.movies.insert_one({
        'title': soup.select_one('meta[property="og:title"]')['content'],
        'image': soup.select_one('meta[property="og:image"]')['content'],
        'description': soup.select_one('meta[property="og:description"]')['content'],
        'star': request.form['star'],
        'comment': request.form['comment']
    })

    return jsonify({'msg': 'POST 연결 완료!'})

@app.route('/movie', methods=['GET'])
def movie_get():
    return jsonify({
        'movies': list(db.movies.find({}, {"_id": False}))
    })

if __name__ == '__main__':
    app.run(
        '0.0.0.0',
        port=5000,
        debug=True
    )
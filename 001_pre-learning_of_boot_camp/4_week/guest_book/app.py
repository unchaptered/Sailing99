from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('Mongo URL')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/post', methods=['POST'])
def homework_post():
    db.post.insert_one({
        'name': request.form['name'],
        'comment': request.form['comment']
    })

    return jsonify({'msg':'댓글 작성 완료!'})

@app.route('/post', methods=['GET'])
def homework_get():
    return jsonify({
        'posts': list(
            db.post.find({}, {"_id": False})
        )
    })

if __name__ == '__main__':
    app.run(
        '0.0.0.0',
        port=5000,
        debug=True
    )
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('Mongo URL')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/bucket', methods=['GET'])
def bucket_get():
   return jsonify({
      'msg': 'GET 연결 완료!',
      'buckets': list(db.bucket.find({}, {'_id': False}))
   })

@app.route('/bucket', methods=['POST'])
def bucket_post():
   num = len(
      list(db.bucket.find({}, {'_id': False}))
   ) + 1

   db.bucket.insert_one({
      'num': num,
      'bucket': request.form['bucket'],
      'done': 0
   })

   return jsonify({'msg': '등록 완료!'})

@app.route('/bucket/done', methods=['POST'])
def bucket_done():
   
   db.bucket.update_one({'num': int(request.form['num'])} , { '$set': { 'done': 1 } })

   return jsonify({'msg': 'POST(완료) 연결 완료!'})

if __name__ == '__main__':
    app.run(
        '0.0.0.0',
        port=5000,
        debug=True
    )

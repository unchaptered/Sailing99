from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('Mongo URL')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/mars', methods=['POST'])
def web_mars_post():
    db.mars.insert_one({
        'name': request.form['name'],
        'address': request.form['address'],
        'size': request.form['size']
    })

    return jsonify({'msg': '주문 완료!'})

@app.route("/mars", methods=["GET"])
def web_mars_get():
    return jsonify({
        'orders': list(
            db.mars.find({}, {"_id": False})
        )
    })

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
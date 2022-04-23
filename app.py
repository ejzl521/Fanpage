from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb+srv://duck:1234@cluster0.f9x0w.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.duck


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/comment', methods=['GET'])
def test_get():
    comments = list(db.comments.find({}, {'_id': False}))
    return jsonify({"comments": comments})


@app.route('/comment', methods=['POST'])
def test_post():
    post_body = request.form
    name = post_body['name']
    comment = post_body['comment']
    doc = {'name': name, 'comment': comment}
    db.comments.insert_one(doc)
    return jsonify({"msg": "success!"})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

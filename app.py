from flask import Flask, request, jsonify
from words import *

app = Flask(__name__)
@app.route("/")
def home():
    return "Hello, Flask!"

@app.route('/get_round', methods = ['GET'])
def getRound():
    round = request.args.get('round')
    result = getResultForWord()
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
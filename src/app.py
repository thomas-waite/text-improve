from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/predict', methods=['POST'])
def predict(x: int):
    y = x ** 2 + 3
    return jsonify({'class_id': 'hello', 'class_name': y})

import json
from flask import Flask, request
from model import 
app = Flask(__name__)


@app.route('/')
def hello():
    return json.dumps({'status': 200, 'body': 'Hello world'})


@app.route('/predict', methods=['POST'])
def predict():
    x = float(request.form['x'])
    y = x ** 2 + 3
    return json.dumps({'class_id': 'hello', 'class_name': y})


if __name__ == '__main__':
    app.run()

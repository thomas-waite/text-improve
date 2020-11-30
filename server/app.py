import json
from flask import Flask, request
from model.Transformer import Model

# Initialise
app = Flask(__name__)
model = Model()


@app.route('/')
def hello():
    return json.dumps({'status': 200, 'body': 'Hello world'})


@app.route('/predict', methods=['POST'])
def predict():
    input_text = request.form['text']
    generated_text = model.text_generation(input_text)
    message = json.dumps(generated_text)

    return json.dumps({'status': 200, 'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
    },
        'body': message})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80')

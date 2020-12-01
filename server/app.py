import json
from flask import Flask, request, jsonify
from model.Transformer import Model
from flask_cors import CORS

# Initialise
app = Flask(__name__)
CORS(app)
model = Model()


@app.route('/')
def hello():
    return json.dumps({'statusCode': 200, 'body': 'Hello world'})


@app.route('/predict', methods=['POST'])
def predict():
    # TODO: Flask is not depending 'Content-Type': 'application/json' correctly
    # so having to force it to retrieve json
    data = request.get_json(force=True)
    {"text": "the football stadium is"}
    input_text = data['text']
    generated_text = model.text_generation(input_text)
    message = json.dumps(generated_text)

    return jsonify(
        {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                # 'Access-Control-Allow-Origin': '*'
            },
            'body': message})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80')

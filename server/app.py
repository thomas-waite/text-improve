import json
from flask import Flask, request
# from model.module import Model

# Initialise
app = Flask(__name__)
# model = Model()


@app.route('/')
def hello():
    return json.dumps({'status': 200, 'body': 'Hello world'})


# @app.route('/predict', methods=['POST'])
# def predict():
#     input_text = request.form['text']
#     generated_text = model.text_generation(input_text)
#     return json.dumps({'status': 200, 'input_text': input_text, 'generated': generated_text[0]['generated_text']})


if __name__ == '__main__':
    app.run()

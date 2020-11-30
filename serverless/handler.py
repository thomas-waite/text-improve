try:
    import unzip_requirements
except ImportError:
    pass

import json
from Transformer import Model


def load_model():
    initialise_all = False
    return Model(initialise_all)


model = load_model()


def lambda_generate_text(event, context):
    """Lambda function to handle execution of the ML inference"""

    print(event)
    data = json.loads(event["body"])
    print('data keys: ', data.keys())
    text = data["text"]
    task_id = data["task_id"]
    print({text})
    print({task_id})

    result = ''
    if task_id == 'question-answering':
        question = data["question"]
        result = model.question_answer(text, question)
    elif task_id == 'text-generation':
        result = model.text_generation(text)
    elif task_id == 'summarisation':
        result = model.summarise(text)
    else:
        return {
            'statusCode': 400
        }

    return {
        "statusCode": 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        "body": json.dumps(result)
    }

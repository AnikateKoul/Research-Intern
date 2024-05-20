from flask import Flask, request, jsonify
from services import plain_prompt, guardrail_wrapper
import json
import guardrails as gr


app = Flask(__name__)
app.debug = True


def load_api_key():
    with open('config.json') as config_file:
        config = json.load(config_file)
        return config['apiKey']


api_key = load_api_key()


@app.route('/plainPrompt', methods=['POST'])
def get_plain_answer():  # put application's code here
    data = request.get_json()
    user_input = data.get('user_input')
    if not user_input:
        return 'No data given, so cannot generate output!'

    try:
        result = guardrail_wrapper.ai_model_with_guardrails(input_text=user_input)
        print("Validated Output:", result)
    except Exception as e:
        print("Validation Error:", e)


@app.route('/guardrailPrompt', methods=['POST'])
def get_guardrail_answer():
    data = request.get_json()
    user_input = data.get('user_input')
    if not user_input:
        return 'No data given, so cannot generate output!'

    return jsonify(guardrail_wrapper.ai_model_with_guardrails(input_text=user_input))


if __name__ == '__main__':
    app.run(debug=True)

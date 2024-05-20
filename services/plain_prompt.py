import google.generativeai as genai
import json


def get_response(user_input):
    def load_api_key():
        with open('config.json') as config_file:
            config = json.load(config_file)
            return config['apiKey']

    genai.configure(api_key=load_api_key())
    gen_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash-latest",
        generation_config=gen_config,
    )
    chat_session = model.start_chat(
        history=[
        ]
    )

    response = chat_session.send_message(user_input)

    return response.text





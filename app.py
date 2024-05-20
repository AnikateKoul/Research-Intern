from flask import Flask

import json

app = Flask(__name__)


def load_api_key():
    with open('config.json') as config_file:
        config = json.load(config_file)
        return config['api_key']


api_key = load_api_key()


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

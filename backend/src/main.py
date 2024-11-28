from flask import Flask
from flask_cors import CORS
from src.controllers.words import WORDS_CONTROLLER


def main():
    APP = Flask(__name__)
    CORS(APP)

    APP.register_blueprint(WORDS_CONTROLLER)

    APP.debug = True
    # ensure that the JSON response is utf-8 encoded
    APP.config['JSON_AS_ASCII'] = False
    APP.json.ensure_ascii=False
    APP.run(host="0.0.0.0", port=3000)

if __name__ == "__main__":
    # start Flask server
    main()
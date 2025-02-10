from flask import Flask
from flask_cors import CORS
from src.controllers.games import GAMES_CONTROLLER
from src.controllers.words import WORDS_CONTROLLER
# from src.controllers.users import USERS_CONTROLLER


def main():
    APP = Flask(__name__)
    CORS(APP, resources={r"/*": {"origins": "http://localhost:8080"}})

    APP.register_blueprint(WORDS_CONTROLLER)
    APP.register_blueprint(GAMES_CONTROLLER)

    APP.debug = True
    # ensure that the JSON response is utf-8 encoded
    APP.config['JSON_AS_ASCII'] = False
    APP.json.ensure_ascii=False
    APP.run(host="0.0.0.0", port=3000)

if __name__ == "__main__":
    # start Flask server
    main()
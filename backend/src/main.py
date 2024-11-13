from flask import Flask
from flask_cors import CORS


def main():
    APP = Flask(__name__)
    CORS(APP)

    APP.debug = True
    APP.run(host="0.0.0.0", port=3000)

if __name__ == "__main__":
    # start Flask server
    main()

from flask import Blueprint
from zufallsworte import zufallswoerter
from werkzeug.exceptions import InternalServerError

WORDS_CONTROLLER = Blueprint("words", __name__)

@WORDS_CONTROLLER.errorhandler(InternalServerError)
def get_random_word() -> str:
    return zufallswoerter(1), 200

WORDS_CONTROLLER.add_url_rule("/words/random", view_func=get_random_word, methods=["GET"])

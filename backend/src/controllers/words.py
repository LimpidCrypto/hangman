
import random
from flask import Blueprint, request
from zufallsworte import zufallswoerter, anzahl_buchstaben
from werkzeug.exceptions import InternalServerError

WORDS_CONTROLLER = Blueprint("words", __name__)

@WORDS_CONTROLLER.errorhandler(InternalServerError)
def get_random_word() -> str:
    return zufallswoerter(1), 200

def get_word_with_difficulty() -> str:
    difficulty = request.args.get('difficulty')
    if difficulty == 1:
        lengthRange = (1, 5)
    elif difficulty == 2:
        lengthRange = (6, 10)
    else:
        lengthRange = (11, 15)

    selectedLength = random.randint(lengthRange[0], lengthRange[1])

    return anzahl_buchstaben(selectedLength, 1), 200

WORDS_CONTROLLER.add_url_rule("/words/random", view_func=get_random_word, methods=["GET"])
WORDS_CONTROLLER.add_url_rule("/words", view_func=get_word_with_difficulty, methods=["GET"])

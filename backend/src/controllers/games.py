
import random
from flask import Blueprint, request
from werkzeug.exceptions import InternalServerError
from serde import from_dict, to_dict

from src.models.games import NewGame, create_game

GAMES_CONTROLLER = Blueprint("games", __name__)

@GAMES_CONTROLLER.errorhandler(InternalServerError)
def add_game() -> str:
    data = request.get_json()
    new_game = from_dict(NewGame, data)
    return to_dict(create_game(new_game))


GAMES_CONTROLLER.add_url_rule("/games", view_func=add_game, methods=["POST"])

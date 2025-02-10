
from flask import Blueprint, request
from werkzeug.exceptions import InternalServerError
from serde import from_dict, to_dict

from src.models.games import NewGame, create_game, get_game as get_game_model

GAMES_CONTROLLER = Blueprint("games", __name__)

@GAMES_CONTROLLER.errorhandler(InternalServerError)
def add_game() -> str:
    data = request.get_json()
    new_game = from_dict(NewGame, data)
    return to_dict(create_game(new_game))

@GAMES_CONTROLLER.errorhandler(InternalServerError)
def get_game(game_id: str) -> str:
    game = get_game_model(game_id)
    print(game)
    return to_dict(game)


GAMES_CONTROLLER.add_url_rule("/games", view_func=add_game, methods=["POST"])
GAMES_CONTROLLER.add_url_rule("/game/<game_id>", view_func=get_game, methods=["GET"])

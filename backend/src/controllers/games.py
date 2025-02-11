
from flask import Blueprint, request
from werkzeug.exceptions import InternalServerError
from serde import from_dict, to_dict
from typing import Tuple

from src.models.games import NewGame, NewWord, add_new_word, create_game, get_game as get_game_model, get_user_to_pick as get_user_to_pick_model

GAMES_CONTROLLER = Blueprint("games", __name__)

@GAMES_CONTROLLER.errorhandler(InternalServerError)
def add_game() -> str:
    data = request.get_json()
    new_game = from_dict(NewGame, data)

    return to_dict(create_game(new_game))

@GAMES_CONTROLLER.errorhandler(InternalServerError)
def get_game(game_id: str) -> str:
    game = get_game_model(game_id)

    return to_dict(game)

@GAMES_CONTROLLER.errorhandler(InternalServerError)
def get_user_to_pick(game_id: str) -> str:
    user_to_pick = get_user_to_pick_model(game_id)

    return user_to_pick

@GAMES_CONTROLLER.errorhandler(InternalServerError)
def add_picked_word(game_id: str) -> None:
    data = request.get_json()
    new_word = from_dict(NewWord, data)

    return to_dict(add_new_word(game_id, new_word))


GAMES_CONTROLLER.add_url_rule("/games", view_func=add_game, methods=["POST"])
GAMES_CONTROLLER.add_url_rule("/game/<game_id>", view_func=get_game, methods=["GET"])
GAMES_CONTROLLER.add_url_rule("/game/<game_id>/user-to-pick", view_func=get_user_to_pick, methods=["GET"])
GAMES_CONTROLLER.add_url_rule("/game/<game_id>/pick-word", view_func=add_picked_word, methods=["POST"])


from flask import Blueprint, request
from src.responses import GameResponse
from werkzeug.exceptions import InternalServerError
from serde import from_dict, to_dict
from typing import Tuple

from src.models.games import NewGame, NewWord, NewLetter, add_new_letter, add_new_word, create_game, get_game as get_game_model, get_user_to_pick as get_user_to_pick_model, get_user_to_guess as get_user_to_guess_model

GAMES_CONTROLLER = Blueprint("games", __name__)

@GAMES_CONTROLLER.errorhandler(InternalServerError)
def add_game() -> str:
    data = request.get_json()
    new_game = from_dict(NewGame, data)

    return to_dict(create_game(new_game))

@GAMES_CONTROLLER.errorhandler(InternalServerError)
def get_game(game_id: str) -> str:
    try:
        game = get_game_model(game_id)
        user_to_pick = get_user_to_pick_model(game_id)
        user_to_guess = get_user_to_guess_model(game_id)
    except ValueError as error:
        if str(error) == "All users have picked a word":
            return to_dict(GameResponse(**to_dict(game), user_to_pick=None, user_to_guess=None))

    return to_dict(GameResponse(**to_dict(game), user_to_pick=user_to_pick, user_to_guess=user_to_guess))

@GAMES_CONTROLLER.errorhandler(InternalServerError)
def add_picked_word(game_id: str) -> None:
    data = request.get_json()
    new_word = from_dict(NewWord, data)
    game = add_new_word(game_id, new_word)
    user_to_pick = get_user_to_pick_model(game_id)
    user_to_guess = get_user_to_guess_model(game_id)

    return to_dict(GameResponse(**to_dict(game), user_to_pick=user_to_pick, user_to_guess=user_to_guess))

@GAMES_CONTROLLER.errorhandler(InternalServerError)
def add_guessed_letter(game_id: str) -> None:
    data = request.get_json()
    new_letter = from_dict(NewLetter, data)
    game = add_new_letter(game_id, new_letter)
    user_to_pick = get_user_to_pick_model(game_id)
    user_to_guess = get_user_to_guess_model(game_id)

    return to_dict(GameResponse(**to_dict(game), user_to_pick=user_to_pick, user_to_guess=user_to_guess))


GAMES_CONTROLLER.add_url_rule("/games", view_func=add_game, methods=["POST"])
GAMES_CONTROLLER.add_url_rule("/game/<game_id>", view_func=get_game, methods=["GET"])
GAMES_CONTROLLER.add_url_rule("/game/<game_id>/pick-word", view_func=add_picked_word, methods=["POST"])
GAMES_CONTROLLER.add_url_rule("/game/<game_id>/guess-letter", view_func=add_guessed_letter, methods=["POST"])

from json import JSONDecodeError
from typing import List, Optional, Dict, Union
from uuid import uuid4

from serde import SerdeError, serde, to_dict
from src.models._entities.games import UserWords
from src.models.data_store_manager import DataList, DataStoreManager
from src.models import GamesEntity, GamesModel, GamesColumn
from src.models.user_words import is_ongoing

@serde
class NewGame():
    usernames: List[str]
    game_type: str
    difficulty: Optional[int] = None

    def __init__(self, usernames: List[str], game_type: str, difficulty: Optional[int] = None):
        self.usernames = usernames
        self.game_type = game_type
        self.difficulty = difficulty

@serde
class NewWord():
    word: str
    picked_by: str

    def __init__(self, word: str, picked_by: str):
        self.word = word
        self.picked_by = picked_by

@serde
class NewLetter():
    letter: str
    guessed_by: str

    def __init__(self, letter: str, guessed_by: str):
        self.letter = letter
        self.guessed_by = guessed_by

def create_game(new_game: NewGame) -> str:
    try:
        game_uuid = str(uuid4())
        return GamesEntity().create(
            DataStoreManager,
            DataList.GAMES,
            GamesModel(
                id=game_uuid,
                type=new_game.game_type,
                users=new_game.usernames,
                user_scores={ username: 0 for username in new_game.usernames },
                difficulty=new_game.difficulty,
            )
        )
    except (FileNotFoundError, JSONDecodeError, SerdeError) as error:
        raise error



def get_game(game_id: str) -> GamesModel:
    game = GamesEntity().find(DataList.GAMES).where(GamesColumn.ID, game_id).one(DataStoreManager)
    return _calculate_scores(game)

def _calculate_scores(game: GamesModel) -> GamesModel:
    user_scores = { username: 0 for username in game.users }
    for user_word in game.user_words:
        for username, letters_guessed in user_word["letters_guessed_by"].items():
            word_list = user_word["word"].split()
            for wl_letter in word_list:
                if wl_letter in letters_guessed:
                    user_scores[username] += 1
            for letter in letters_guessed:
                if letter not in word_list:
                    user_scores[user_word["picked_by"]] -= 1
    game.user_scores = user_scores

    return game

def get_user_words(game_id: str) -> List[UserWords]:
    return get_game(game_id).user_words

def get_ongoing_word(game_id: str) -> Optional[UserWords]:
    user_words = get_user_words(game_id)
    for user_word in user_words:
        if is_ongoing(user_word):
            return user_word

    return None

def get_user_to_pick(game_id: str) -> Optional[str]:
    ongoing_word = get_ongoing_word(game_id)
    if ongoing_word is None:
        # determine the next user to pick
        game = get_game(game_id)
        users = game.users
        users_already_picked = [user_word["picked_by"] for user_word in game.user_words]
        users_not_picked = [user for user in users if user not in users_already_picked]
        if len(users_not_picked) == 0:
            raise ValueError("All users have picked a word")
        return users_not_picked[0]

    return None

def get_user_to_guess(game_id: str) -> Optional[str]:
    game = get_game(game_id)
    ongoing_word = get_ongoing_word(game_id)
    if ongoing_word is None:
        return None
    users_to_guess = [user for user in game.users if user != ongoing_word["picked_by"]]
    # determine the next user to guess by finding the user that guessed the least number of times
    guess_counts = {user: 0 for user in users_to_guess}
    for user in users_to_guess:
        if user not in ongoing_word["letters_guessed_by"]:
            return user
    for user, letters_guessed in ongoing_word["letters_guessed_by"].items():
        guess_counts[user] = len(letters_guessed)

    next_user_to_guess = min(guess_counts, key=guess_counts.get)
    return next_user_to_guess

def add_new_word(game_id: str, new_word: NewWord) -> GamesModel:
    try:
        game = get_game(game_id)
        game.user_words.append({"picked_by": new_word.picked_by, "word": new_word.word.upper(), "letters_guessed_by": {}})
        return GamesEntity().find(DataList.GAMES).where(GamesColumn.ID, game_id).update(DataStoreManager, game)
    except (FileNotFoundError, JSONDecodeError, SerdeError) as error:
        raise error

def add_new_letter(game_id: str, new_letter: NewLetter) -> GamesModel:
    try:
        game = get_game(game_id)
        ongoing_word = get_ongoing_word(game_id)
        if ongoing_word is None:
            raise ValueError("No ongoing word found")
        ongoing_word_index = game.user_words.index(ongoing_word)
        if new_letter.guessed_by not in ongoing_word["letters_guessed_by"]:
            ongoing_word["letters_guessed_by"][new_letter.guessed_by] = []
        if new_letter.letter not in ongoing_word["letters_guessed_by"][new_letter.guessed_by]:
            ongoing_word["letters_guessed_by"][new_letter.guessed_by].append(new_letter.letter)
            game.user_words[ongoing_word_index] = ongoing_word
        return GamesEntity().find(DataList.GAMES).where(GamesColumn.ID, game_id).update(DataStoreManager, game)
    except (FileNotFoundError, JSONDecodeError, SerdeError) as error:
        raise error

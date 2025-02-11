from json import JSONDecodeError
from typing import List, Optional, Dict
from uuid import uuid4

from serde import SerdeError, serde, to_dict
from src.models.data_store_manager import DataList, DataStoreManager
from src.models import GamesEntity, GamesModel, GamesColumn, UserWordsModel

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
        print(new_game)
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
    return GamesEntity().find(DataList.GAMES).where(GamesColumn.ID, game_id).one(DataStoreManager)

def get_user_words(game_id: str) -> List[UserWordsModel]:
    return get_game(game_id).user_words

def get_ongoing_word(game_id: str) -> Optional[UserWordsModel]:
    user_words = get_user_words(game_id)
    for user_word in user_words:
        if user_word.is_ongoing():
            return user_word

    return None

def get_user_to_pick(game_id: str) -> Optional[str]:
    ongoing_word = get_ongoing_word(game_id)
    if ongoing_word is None:
        # determine the next user to pick
        game = get_game(game_id)
        users = game.users
        users_already_picked = [user_word.picked_by for user_word in game.user_words]
        users_not_picked = [user for user in users if user not in users_already_picked]
        if len(users_not_picked) == 0:
            return None
        return { "user_to_pick": users_not_picked[0] }

    return to_dict(ongoing_word)

def add_new_word(game_id: str, new_word: NewWord) -> GamesModel:
    try:
        game = get_game(game_id)
        game.user_words.append(UserWordsModel(new_word.picked_by, new_word.word))
        return GamesEntity().find(DataList.GAMES).where(GamesColumn.ID, game_id).update(DataStoreManager, game)
    except (FileNotFoundError, JSONDecodeError, SerdeError) as error:
        raise error

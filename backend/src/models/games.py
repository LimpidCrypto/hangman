from json import JSONDecodeError
from typing import List, Optional, Dict
from uuid import uuid4

from serde import SerdeError, serde
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

def get_user_to_pick(game_id: str) -> Optional[str]:
    game = get_game(game_id)
    if len(game.user_words) == len(game.users):
        return None
    user_to_pick = game.users[len(game.user_words) % len(game.users)]

    return user_to_pick

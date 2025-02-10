from json import JSONDecodeError
from typing import List, Optional
from uuid import uuid4

from serde import SerdeError, serde
from src.models.data_store_manager import DataList, DataStoreManager
from src.models._entities import GamesEntity, GamesModel

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
                user_words=[],
                difficulty=new_game.difficulty,
            )
        )
    except (FileNotFoundError, JSONDecodeError, SerdeError) as error:
        raise error


from enum import Enum
from typing import Dict, List, Optional
from serde import serde, from_dict
from src.models._entities.user_words import Model as UserWordsModel
from src.models._entities import BaseEntity

@serde
class Model:
    id: str
    type: str
    users: List[str]
    user_words: List[UserWordsModel]
    difficulty: Optional[int] = None

    def __init__(self, id: str, type: str, users: List[str], user_words: List[UserWordsModel], difficulty: Optional[int] = None):
        self.id = id
        self.type = type
        self.users = users
        self.user_words = user_words
        self.difficulty = difficulty


class Entity(BaseEntity[Model]):
    def _deserialize(self, data: Dict[str, str]) -> Model:
        return from_dict(Model, data)


class Column(Enum):
    ID = "id"
    TYPE = "type"
    USERS = "users"
    USER_WORDS = "user_words"
    DIFFICULTY = "difficulty"
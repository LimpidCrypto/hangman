from enum import Enum
import time
from typing import Dict, List, Optional, Any
from serde import serde, from_dict
from src.models._entities.base_entity import BaseEntity
from src.models._entities.user_words import Model as UserWordsModel

@serde
class Model:
    id: str
    type: str
    users: List[str]
    user_words: List[UserWordsModel]
    user_scores: Dict[str, int]
    timestamp: float
    difficulty: Optional[int] = None

    def __init__(
            self,
            id: str,
            type: str,
            users: List[str],
            user_words: List[UserWordsModel] = [],
            user_scores: Dict[str, int] = {},
            timestamp: float = time.time(),
            difficulty: Optional[int] = None
        ):
        self.id = id
        self.type = type
        self.users = users
        self.user_words = user_words
        self.user_scores = user_scores
        self.timestamp = timestamp
        self.difficulty = difficulty


class Entity(BaseEntity[Model]):
    def _deserialize(self, data: Dict[str, Any]) -> Model:
        print("IUWESDOIUHOWSEW", data)
        return from_dict(Model, data)


class Column(Enum):
    ID = "id"
    TYPE = "type"
    USERS = "users"
    USER_WORDS = "user_words"
    DIFFICULTY = "difficulty"
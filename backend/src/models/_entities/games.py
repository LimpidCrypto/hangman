from enum import Enum
import time
from typing import Dict, List, Optional, Any, TypedDict, Union
from serde import serde, from_dict
from src.models._entities.base_entity import BaseEntity

class UserWords(TypedDict):
    picked_by: str
    word: str
    letters_guessed_by: Dict[str, List[str]]

@serde
class Model:
    id: str
    type: str
    users: List[str]
    user_words: List[Dict[str, Union[str, Dict[str, List[str]]]]]
    user_scores: Dict[str, int]
    timestamp: float
    difficulty: Optional[int] = None

    def __init__(
            self,
            id: str,
            type: str,
            users: List[str],
            user_words: List[Dict[str, Union[str, Dict[str, List[str]]]]] = [],
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
        model = from_dict(Model, data)
        return model


class Column(Enum):
    ID = "id"
    TYPE = "type"
    USERS = "users"
    USER_WORDS = "user_words"
    DIFFICULTY = "difficulty"
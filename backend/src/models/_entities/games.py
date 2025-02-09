from enum import Enum
from typing import Dict, List, Optional
from serde import serde, from_dict
from src.models._entities import BaseEntity

@serde
class UserWords:
    user: str
    word: str
    letters_guessed: List[chr]

@serde
class Model:
    id: str
    type: str
    users: List[str]
    user_words: List[UserWords]
    difficulty: Optional[int] = None

    def __init__(self, id: str) -> None:
        self.id = id


class Entity(BaseEntity[Model]):
    def _deserialize(self, data: Dict[str, str]) -> Model:
        return from_dict(Model, data)


class Column(Enum):
    ID = "id"
    NAME = "name"
    LAST_ACTIVE = "last_active"
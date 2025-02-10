from enum import Enum
from typing import Dict, List
from serde import serde, from_dict
from src.models._entities import BaseEntity

@serde
class Model:
    user: str
    word: str
    letters_guessed: List[str]

    def __init__(self, user: str, word: str, letters_guessed: List[str]):
        self.user = user
        self.word = word
        self.letters_guessed = letters_guessed


class Entity(BaseEntity[Model]):
    def _deserialize(self, data: Dict[str, str]) -> Model:
        return from_dict(Model, data)


class Column(Enum):
    USER = "user"
    WORD = "word"
    LETTERS_GUESSED = "letters_guessed"
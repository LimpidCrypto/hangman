from enum import Enum
from typing import Dict, List
from serde import serde, from_dict
from src.models._entities import BaseEntity

@serde
class Model:
    picked_by: str
    word: str
    letters_guessed_by: Dict[str, List[str]]

    def __init__(self, picked_by: str, word: str, letters_guessed_by: Dict[str, List[str]] = {}):
        self.picked_by = picked_by
        self.word = word
        self.letters_guessed_by = letters_guessed_by


class Entity(BaseEntity[Model]):
    def _deserialize(self, data: Dict[str, str]) -> Model:
        return from_dict(Model, data)


class Column(Enum):
    PICKED_BY = "picked_by"
    WORD = "word"
    LETTERS_GUESSED_BY = "letters_guessed_by"
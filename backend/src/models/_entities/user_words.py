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

    def get_all_word_letters(self) -> List[str]:
        return list(set(self.word))

    def get_all_guessed_letters(self) -> List[str]:
        return list(set([letter for letters in self.letters_guessed_by.values() for letter in letters]))

    def get_false_letters_count(self) -> int:
        return len([letter for letter in self.word if letter not in self.letters_guessed_by])

    def get_correct_letters_count(self) -> int:
        return len([letter for letter in self.word if letter in self.letters_guessed_by])

    def add_letter_guessed(self, letter: str, username: str) -> None:
        if username not in self.letters_guessed_by:
            self.letters_guessed_by[username] = []
        self.letters_guessed_by[username].append(letter)

    def is_guessed(self) -> bool:
        all_word_letters = self.get_all_word_letters()
        all_guessed_letters = self.get_all_guessed_letters()

        return all(letter in all_guessed_letters for letter in all_word_letters)

    def is_guess_failed(self) -> bool:
        return self.get_false_letters_count() >= 10


class Entity(BaseEntity[Model]):
    def _deserialize(self, data: Dict[str, str]) -> Model:
        return from_dict(Model, data)


class Column(Enum):
    PICKED_BY = "picked_by"
    WORD = "word"
    GUESSED = "guessed"
    LETTERS_GUESSED_BY = "letters_guessed_by"
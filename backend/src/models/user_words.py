from typing import List

from src.models._entities import UserWordsModel

def get_all_word_letters(model: UserWordsModel) -> List[str]:
    return list(set(model.word))

def get_all_guessed_letters(model: UserWordsModel) -> List[str]:
    return list(set([letter for letters in model.letters_guessed_by.values() for letter in letters]))

def get_false_letters_count(model: UserWordsModel) -> int:
    return len([letter for letter in model.word if letter not in model.letters_guessed_by])

def get_correct_letters_count(model: UserWordsModel) -> int:
    return len([letter for letter in model.word if letter in model.letters_guessed_by])

def add_letter_guessed(model: UserWordsModel, letter: str, username: str) -> None:
    if username not in model.letters_guessed_by:
        model.letters_guessed_by[username] = []
    model.letters_guessed_by[username].append(letter)

def is_guess_successful(model: UserWordsModel) -> bool:
    all_word_letters = get_all_word_letters(model)
    all_guessed_letters = get_all_guessed_letters(model)

    return all(letter in all_guessed_letters for letter in all_word_letters)

def is_guess_failed(model: UserWordsModel) -> bool:
    return get_false_letters_count(model) >= 10

def is_ongoing(model: UserWordsModel) -> bool:
    return not is_guess_successful(model) and not is_guess_failed(model)
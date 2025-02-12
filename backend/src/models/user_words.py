from typing import List

from src.models._entities import UserWords

def get_all_word_letters(model: UserWords) -> List[str]:
    return list(set(model["word"]))

def get_all_guessed_letters(model: UserWords) -> List[str]:
    return list(set([letter for letters in model["letters_guessed_by"].values() for letter in letters]))

def get_false_letters_count(model: UserWords) -> int:
    return len([letter for letter in model["word"] if letter not in model["letters_guessed_by"]])

def get_correct_letters_count(model: UserWords) -> int:
    return len([letter for letter in model["word"] if letter in model["letters_guessed_by"]])

def add_letter_guessed(model: UserWords, letter: str, username: str) -> None:
    if username not in model["letters_guessed_by"]:
        model["letters_guessed_by"][username] = []
    model["letters_guessed_by"][username].append(letter)

def is_guess_successful(model: UserWords) -> bool:
    all_word_letters = get_all_word_letters(model)
    all_guessed_letters = get_all_guessed_letters(model)

    return all(letter in all_guessed_letters for letter in all_word_letters)

def is_guess_failed(model: UserWords) -> bool:
    return get_false_letters_count(model) >= 10

def is_ongoing(model: UserWords) -> bool:
    print("IJNI", model)
    return not is_guess_successful(model) and not is_guess_failed(model)

from enum import Enum
from serde import serde

class GameType(str, Enum):
    PLAYER_VS_PLAYER = "player_vs_player"
    PLAYER_VS_CPU = "player_vs_cpu"

class WordDifficulty(int, Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3

@serde
class UserTurns:
    pick: str
    guess: str

    def __init__(self, pick: str, guess: str):
        self.pick = pick
        self.guess = guess

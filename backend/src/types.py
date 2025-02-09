
from enum import Enum

class GameType(str, Enum):
    PLAYER_VS_PLAYER = "player_vs_player"
    PLAYER_VS_CPU = "player_vs_cpu"

class WordDifficulty(int, Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3

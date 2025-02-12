from serde import serde
from typing import Optional, List, Dict, Union

from src.models import GamesModel, UserWordsModel, UserWords

@serde
class GameResponse:
    id: str
    type: str
    users: List[str]
    user_words: List[Dict[str, Union[str, Dict[str, List[str]]]]]
    user_scores: Dict[str, int]
    timestamp: float
    difficulty: Optional[int] = None
    user_to_pick: Optional[str] = None
    user_to_guess: Optional[str] = None

    def __init__(
            self,
            id: str,
            type: str,
            users: List[str],
            user_words: List[Dict[str, Union[str, Dict[str, List[str]]]]],
            user_scores: Dict[str, int],
            timestamp: float,
            difficulty: Optional[int] = None,
            user_to_pick: Optional[str] = None,
            user_to_guess: Optional[str] = None
        ):
        self.id = id
        self.type = type
        self.users = users
        self.user_words = user_words
        self.user_scores = user_scores
        self.timestamp = timestamp
        self.difficulty = difficulty
        self.user_to_pick = user_to_pick
        self.user_to_guess = user_to_guess
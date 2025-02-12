from unittest import TestCase, main
from src.models import GamesEntity

class TestGamesSerde(TestCase):
    def test_deserialize(self):
        json = {'id': '8e9b1bf2-f9c0-4942-9d80-23fb4e189618', 'type': 'player_vs_player', 'users': ['test1', 'test2'], 'user_words': [{'picked_by': 'test1', 'word': 'hello', 'letters_guessed_by': {}}], 'user_scores': {'test1': 0, 'test2': 0}, 'timestamp': 1739293684.5476522, 'difficulty': None}
        model = GamesEntity()._deserialize(json)
        self.assertEqual(model.id, '8e9b1bf2-f9c0-4942-9d80-23fb4e189618')

if __name__ == '__main__':
    main()
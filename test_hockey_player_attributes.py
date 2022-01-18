from unittest import TestCase
from game import hockey_player_attributes as hockey_player_attributes


class TestHockeyPlayerAttributes(TestCase):
    def test_hockey_player_attributes_when_character_is_level_one(self):
        player = {'health': 150, 'damage': 10, 'accuracy': 0, 'level': 'waterboy', 'attack': None, 'current '
                                                                                                   'experience': 0}
        expected = {'health': 60, 'damage': 20, 'accuracy': 55, 'level': 'waterboy',
                    'attack': ['trip', 'hook', 'wrist shot'], 'current experience': 0}
        actual = hockey_player_attributes(player)
        self.assertEqual(expected, actual)

    def test_hockey_player_attributes_when_character_is_level_two(self):
        player = {'health': 150, 'damage': 10, 'accuracy': 0, 'level': 'benchwarmer', 'attack': None, 'current '
                                                                                                      'experience': 0}
        expected = {'health': 90, 'damage': 25, 'accuracy': 45, 'level': 'benchwarmer',
                    'attack': ['slash', 'cross check', 'body check'], 'current experience': 0}
        actual = hockey_player_attributes(player)
        self.assertEqual(expected, actual)

    def test_hockey_player_attributes_when_character_is_level_three(self):
        player = {'health': 150, 'damage': 10, 'accuracy': 0, 'level': 'superstar', 'attack': None, 'current '
                                                                                                    'experience': 0}
        expected = {'health': 140, 'damage': 40, 'accuracy': 25, 'level': 'superstar',
                    'attack': ['slew foot', 'hip check', 'slap shot'], 'current experience': 0}
        actual = hockey_player_attributes(player)
        self.assertEqual(expected, actual)

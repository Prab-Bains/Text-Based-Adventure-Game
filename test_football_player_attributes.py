from unittest import TestCase
from game import football_player_attributes as football_player_attributes


class TestFootballPlayerAttributes(TestCase):
    def test_football_player_attributes_when_character_is_level_one(self):
        player = {'health': 100, 'damage': 10, 'accuracy': 10, 'level': 'waterboy', 'attack': None, 'current '
                                                                                                    'experience': 0}
        expected = {'health': 60, 'damage': 30, 'accuracy': 45, 'level': 'waterboy',
                    'attack': ['stiff arm', 'tackle', 'chirp'], 'current experience': 0}
        actual = football_player_attributes(player)
        self.assertEqual(expected, actual)

    def test_football_player_attributes_when_character_is_level_two(self):
        player = {'health': 100, 'damage': 10, 'accuracy': 10, 'level': 'benchwarmer', 'attack': None, 'current '
                                                                                                       'experience': 0}
        expected = {'health': 90, 'damage': 40, 'accuracy': 35, 'level': 'benchwarmer',
                    'attack': ['football', 'gatorade bottle', 'facemask'], 'current experience': 0}
        actual = football_player_attributes(player)
        self.assertEqual(expected, actual)

    def test_football_player_attributes_when_character_is_level_three(self):
        player = {'health': 100, 'damage': 10, 'accuracy': 10, 'level': 'superstar', 'attack': None, 'current '
                                                                                                     'experience': 0}
        expected = {'health': 140, 'damage': 60, 'accuracy': 25, 'level': 'superstar',
                    'attack': ['hit stick', 'helmet', 'punch'], 'current experience': 0}
        actual = football_player_attributes(player)
        self.assertEqual(expected, actual)

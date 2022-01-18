from unittest import TestCase
from game import baseball_player_attributes as baseball_player_attributes


class TestBaseballPlayerAttributes(TestCase):
    def test_baseball_player_attributes_when_character_is_level_one(self):
        player = {'health': 100, 'damage': 1, 'accuracy': 10, 'level': 'waterboy', 'attack': None, 'current '
                                                                                                   'experience': 0}
        expected = {'health': 60, 'damage': 5, 'accuracy': 60, 'level': 'waterboy',
                    'attack': ['baseball', 'gleaming staredown', 'bucket of ice cold water'], 'current experience': 0}
        actual = baseball_player_attributes(player)
        self.assertEqual(expected, actual)

    def test_baseball_player_attributes_when_character_is_level_two(self):
        player = {'health': 100, 'damage': 1, 'accuracy': 10, 'level': 'benchwarmer', 'attack': None, 'current '
                                                                                                      'experience': 0}
        expected = {'health': 90, 'damage': 20, 'accuracy': 55, 'level': 'benchwarmer',
                    'attack': ['sock full of sand', 'running punch', 'helmet'], 'current experience': 0}
        actual = baseball_player_attributes(player)
        self.assertEqual(expected, actual)

    def test_baseball_player_attributes_when_character_is_level_three(self):
        player = {'health': 100, 'damage': 1, 'accuracy': 10, 'level': 'superstar', 'attack': None, 'current '
                                                                                                    'experience': 0}
        expected = {'health': 140, 'damage': 25, 'accuracy': 35, 'level': 'superstar',
                    'attack': ['bat', 'cleat stomp', 'poisonous gatorade'], 'current experience': 0}
        actual = baseball_player_attributes(player)
        self.assertEqual(expected, actual)

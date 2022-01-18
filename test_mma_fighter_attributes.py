from unittest import TestCase
from game import mma_fighter_attributes as mma_fighter_attributes


class TestMmaFighterAttributes(TestCase):
    def test_mma_fighter_attributes_when_character_is_level_one(self):
        player = {'health': 100, 'damage': 10, 'accuracy': 0, 'level': 'waterboy', 'attack': None, 'current '
                                                                                                   'experience': 0}
        expected = {'health': 50, 'damage': 30, 'accuracy': 50, 'level': 'waterboy',
                    'attack': ['jab', 'right hook', 'uppercut'], 'current experience': 0}
        actual = mma_fighter_attributes(player)
        self.assertEqual(expected, actual)

    def test_mma_fighter_attributes_when_character_is_level_two(self):
        player = {'health': 100, 'damage': 10, 'accuracy': 0, 'level': 'benchwarmer', 'attack': None, 'current '
                                                                                                      'experience': 0}
        expected = {'health': 70, 'damage': 40, 'accuracy': 40, 'level': 'benchwarmer',
                    'attack': ['flying knee', 'round kick', 'elbow'], 'current experience': 0}
        actual = mma_fighter_attributes(player)
        self.assertEqual(expected, actual)

    def test_mma_fighter_attributes_when_character_is_level_three(self):
        player = {'health': 100, 'damage': 10, 'accuracy': 0, 'level': 'superstar', 'attack': None, 'current '
                                                                                                    'experience': 0}
        expected = {'health': 100, 'damage': 60, 'accuracy': 30, 'level': 'superstar',
                    'attack': ['superman Punch', 'headlock', 'arm bar'], 'current experience': 0}
        actual = mma_fighter_attributes(player)
        self.assertEqual(expected, actual)

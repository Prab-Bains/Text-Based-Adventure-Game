from unittest import TestCase
from game import level_up as level_up


class TestLevelUp(TestCase):
    def test_level_up_MMA_Fighter(self):
        player = {'class_name': 'MMA Fighter', 'level': 'waterboy', 'current experience': 125, 'experience needed': 100}
        expected = {'class_name': 'MMA Fighter', 'level': 'benchwarmer', 'current experience': 0,
                    'experience needed': 100, 'attack': ['flying knee', 'round kick', 'elbow'], 'damage': 40,
                    'health': 70, 'accuracy': 40}
        actual = level_up(player)
        self.assertEqual(expected, actual)

    def test_level_up_hockey_player(self):
        player = {'class_name': 'Hockey Player', 'level': 'benchwarmer', 'current experience': 125,
                  'experience needed': 100}

        expected = {'class_name': 'Hockey Player', 'level': 'superstar', 'current experience': 0,
                    'experience needed': 100, 'attack': ['slew foot', 'hip check', 'slap shot'], 'damage': 40,
                    'health': 140, 'accuracy': 25}

        actual = level_up(player)
        self.assertEqual(expected, actual)

    def test_level_up_football_player_(self):
        player = {'class_name': 'Football Player', 'level': 'waterboy', 'current experience': 125,
                  'experience needed': 100}

        expected = {'class_name': 'Football Player', 'level': 'benchwarmer', 'current experience': 0,
                    'experience needed': 100, 'attack': ['football', 'gatorade bottle', 'facemask'], 'damage': 40,
                    'health': 90, 'accuracy': 35}

        actual = level_up(player)
        self.assertEqual(expected, actual)

    def test_level_up_baseball_player_(self):
        player = {'class_name': 'Baseball Player', 'level': 'waterboy', 'current experience': 125,
                  'experience needed': 100}

        expected = {'class_name': 'Baseball Player', 'level': 'benchwarmer', 'current experience': 0,
                    'experience needed': 100, 'attack': ['sock full of sand', 'running punch', 'helmet'], 'damage': 20,
                    'health': 90, 'accuracy': 55}

        actual = level_up(player)
        self.assertEqual(expected, actual)

    def test_level_up_when_MMA_Fighter_does_not_have_enough_experience(self):
        player = {'class_name': 'MMA Fighter', 'level': 'benchwarmer', 'current experience': 125,
                  'experience needed': 100}
        expected = player
        actual = level_up(player)
        self.assertEqual(expected, actual)

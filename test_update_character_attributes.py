from unittest import TestCase
from game import update_character_attributes as update_character_attributes


class TestUpdateCharacterAttributes(TestCase):
    def test_update_character_attributes_when_character_is_mma_fighter(self):
        player = {'class_name': 'MMA Fighter', 'health': 10, 'damage': 10, 'accuracy': 20, 'level': 'waterboy',
                  'attack': None, 'current experience': 0}

        expected = {'class_name': 'MMA Fighter', 'health': 50, 'damage': 30, 'accuracy': 50, 'level': 'waterboy',
                    'attack': ['jab', 'right hook', 'uppercut'], 'current experience': 0}

        actual = update_character_attributes(player)
        self.assertEqual(actual, expected)

    def test_update_character_attributes_when_character_is_hockey_player(self):
        player = {'class_name': 'Hockey Player', 'health': 10, 'damage': 10, 'accuracy': 20, 'level': 'benchwarmer',
                  'attack': None, 'current experience': 0}

        expected = {'class_name': 'Hockey Player', 'health': 90, 'damage': 25, 'accuracy': 45, 'level': 'benchwarmer',
                    'attack': ['slash', 'cross check', 'body check'], 'current experience': 0}

        actual = update_character_attributes(player)
        self.assertEqual(actual, expected)

    def test_update_character_attributes_when_character_is_football_player(self):
        player = {'class_name': 'Football Player', 'health': 10, 'damage': 10, 'accuracy': 20, 'level': 'waterboy',
                  'attack': None, 'current experience': 0}

        expected = {'class_name': 'Football Player', 'health': 60, 'damage': 30, 'accuracy': 45, 'level': 'waterboy',
                    'attack': ['stiff arm', 'tackle', 'chirp'], 'current experience': 0}

        actual = update_character_attributes(player)
        self.assertEqual(actual, expected)

    def test_update_character_attributes_when_character_is_baseball_player(self):
        player = {'class_name': 'Baseball Player', 'health': 10, 'damage': 10, 'accuracy': 20, 'level': 'superstar',
                  'attack': None, 'current experience': 0}

        expected = {'class_name': 'Baseball Player', 'health': 140, 'damage': 25, 'accuracy': 35, 'level': 'superstar',
                    'attack': ['bat', 'cleat stomp', 'poisonous gatorade'], 'current experience': 0}

        actual = update_character_attributes(player)
        self.assertEqual(actual, expected)

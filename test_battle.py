from unittest import TestCase
from unittest.mock import patch
from game import battle as battle


class TestBattle(TestCase):
    @patch('random.randint', side_effect=[2])
    @patch('builtins.input', side_effect=[2])
    def test_battle_when_user_flees_and_does_not_take_damage_when_running_away(self, _, __):
        character = {'name': 'Prab', 'class_name': 'Hockey Player', 'health': 60, 'damage': 20,
                     'accuracy': 55, 'level': 'waterboy', 'attack': ['trip', 'hook', 'wrist shot'], "X-coordinate": 0,
                     "Y-coordinate": 0, 'current experience': 0, 'experience needed': 100}
        character_copy = {'name': 'Prab', 'class_name': 'Hockey Player', 'health': 60, 'damage': 20,
                          'accuracy': 55, 'level': 'waterboy', 'attack': ['trip', 'hook', 'wrist shot'],
                          "X-coordinate": 0, "Y-coordinate": 0, 'current experience': 0, 'experience needed': 100}

        enemy = {'name': 'Trainer', 'damage': 10, 'health': 50}
        expected = False
        actual = battle(character, enemy)

        self.assertEqual(actual, expected)
        self.assertEqual(character, character_copy)

    @patch('random.randint', side_effect=[1])
    @patch('builtins.input', side_effect=[2])
    def test_battle_when_user_flees_and_takes_damage_when_running_away(self, _, __):
        character = {'name': 'Prab', 'class_name': 'Hockey Player', 'health': 60, 'damage': 20,
                     'accuracy': 55, 'level': 'benchwarmer', 'attack': ['trip', 'hook', 'wrist shot'],
                     "X-coordinate": 0, "Y-coordinate": 0, 'current experience': 0, 'experience needed': 100}
        character_copy = {'name': 'Prab', 'class_name': 'Hockey Player', 'health': 60, 'damage': 20,
                          'accuracy': 55, 'level': 'benchwarmer', 'attack': ['trip', 'hook', 'wrist shot'],
                          "X-coordinate": 0, "Y-coordinate": 0, 'current experience': 0, 'experience needed': 100}

        enemy = {'name': 'Trainer', 'damage': 10, 'health': 50}
        expected = False
        actual = battle(character, enemy)

        self.assertEqual(actual, expected)
        self.assertEqual(character['current experience'], character_copy['current experience'])
        # shows that the character's health went down by 10
        self.assertEqual(character['health'] + 10, character_copy['health'])

    @patch('random.randint', side_effect=[10, 0, 5, 12, 1])
    @patch('builtins.input', side_effect=[1, 1])
    def test_battle_when_user_wins_battle(self, _, __):
        character = {'name': 'Prabhjeet', 'class_name': 'Hockey Player', 'health': 60, 'damage': 25,
                     'accuracy': 55, 'level': 'waterboy', 'attack': ['trip', 'hook', 'wrist shot'], "X-coordinate": 0,
                     "Y-coordinate": 0, 'current experience': 0, 'experience needed': 100}
        character_copy = {'name': 'Prabhjeet', 'class_name': 'Hockey Player', 'health': 60, 'damage': 25,
                          'accuracy': 55, 'level': 'waterboy', 'attack': ['trip', 'hook', 'wrist shot'],
                          "X-coordinate": 0, "Y-coordinate": 0, 'current experience': 0, 'experience needed': 100}

        enemy = {'name': 'Trainer', 'damage': 10, 'health': 50}
        expected = True
        actual = battle(character, enemy)
        self.assertEqual(actual, expected)
        # shows that the character's experience went up by 25
        self.assertEqual(character['current experience'] - 25, character_copy['current experience'])
        # shows that the enemy has died
        self.assertEqual(enemy['health'], 0)

    @patch('random.randint', side_effect=[99, 0, 5, 99, 1])
    @patch('builtins.input', side_effect=[1, 1])
    def test_battle_when_user_loses_battle(self, _, __):
        character = {'name': 'BCIT', 'class_name': 'Hockey Player', 'health': 60, 'damage': 25,
                     'accuracy': 55, 'level': 'waterboy', 'attack': ['trip', 'hook', 'wrist shot'], "X-coordinate": 0,
                     "Y-coordinate": 0, 'current experience': 0, 'experience needed': 100}
        character_copy = {'name': 'BCIT', 'class_name': 'Hockey Player', 'health': 60, 'damage': 25,
                          'accuracy': 55, 'level': 'waterboy', 'attack': ['trip', 'hook', 'wrist shot'],
                          "X-coordinate": 0, "Y-coordinate": 0, 'current experience': 0, 'experience needed': 100}

        enemy = {'name': 'Trainer', 'damage': 30, 'health': 50}
        expected = False
        actual = battle(character, enemy)
        self.assertEqual(actual, expected)
        self.assertEqual(character['current experience'], character_copy['current experience'])
        # shows that the character has died
        self.assertEqual(character['health'], 0)

    @patch('random.randint', side_effect=[10, 0, 1])
    @patch('builtins.input', side_effect=[1])
    def test_battle_when_foe_runs_away(self, _, __):
        character = {'name': 'CST', 'class_name': 'Hockey Player', 'health': 60, 'damage': 25,
                     'accuracy': 55, 'level': 'waterboy', 'attack': ['trip', 'hook', 'wrist shot'], "X-coordinate": 0,
                     "Y-coordinate": 0, 'current experience': 0, 'experience needed': 100}
        character_copy = {'name': 'CST', 'class_name': 'Hockey Player', 'health': 60, 'damage': 25,
                          'accuracy': 55, 'level': 'waterboy', 'attack': ['trip', 'hook', 'wrist shot'],
                          "X-coordinate": 0, "Y-coordinate": 0, 'current experience': 0, 'experience needed': 100}

        enemy = {'name': 'Trainer', 'damage': 30, 'health': 50}
        expected = False
        actual = battle(character, enemy)
        self.assertEqual(actual, expected)
        # shows that the character's experience went up by 20
        self.assertEqual(character['current experience'] - 20, character_copy['current experience'])

    @patch('random.randint', side_effect=[10, 0, 15, 1])
    @patch('builtins.input', side_effect=[1, 1])
    def test_battle_when_user_wins_battle_and_is_on_boss_level(self, _, __):
        character = {'name': 'Bains', 'class_name': 'Hockey Player', 'health': 60, 'damage': 25,
                     'accuracy': 55, 'level': 'superstar', 'attack': ['trip', 'hook', 'wrist shot'], "X-coordinate": 0,
                     "Y-coordinate": 0, 'current experience': 0, 'experience needed': 100}
        character_copy = {'name': 'Bains', 'class_name': 'Hockey Player', 'health': 60, 'damage': 25,
                          'accuracy': 55, 'level': 'waterboy', 'attack': ['trip', 'hook', 'wrist shot'],
                          "X-coordinate": 0, "Y-coordinate": 0, 'current experience': 0, 'experience needed': 100}

        enemy = {'name': 'Trainer', 'damage': 10, 'health': 50}
        expected = True
        actual = battle(character, enemy)
        self.assertEqual(actual, expected)
        # shows that the character's experience went up by 100
        self.assertEqual(character['current experience'] - 100, character_copy['current experience'])
        # shows that the enemy has died
        self.assertEqual(enemy['health'], 0)

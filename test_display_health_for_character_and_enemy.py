import io
from unittest import TestCase
from unittest.mock import patch
from game import display_health_for_character_and_enemy as display_health_for_character_and_enemy


class TestDisplayHealthForCharacterAndEnemy(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_health_for_character_and_enemy_when_character_and_enemy_are_both_alive(self, display_of_health):
        character = {'health': 10}
        enemy = {'health': 100}
        enemy_name = 'coach'
        expected = "Your health is 10\nYour coach's health is 100\n"
        display_health_for_character_and_enemy(character, enemy, enemy_name)
        actual = display_of_health.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_health_for_character_and_enemy_when_character_alive_enemy_is_dead(self, display_of_health):
        character = {'health': 10}
        enemy = {'health': 0}
        enemy_name = 'coach'
        expected = "Your health is 10\n"
        display_health_for_character_and_enemy(character, enemy, enemy_name)
        actual = display_of_health.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_health_for_character_and_enemy_when_character_dies(self, display_of_health):
        character = {'health': 0}
        enemy = {'health': 100}
        enemy_name = 'coach'
        expected = "You are losing a lot of blood!\n"
        display_health_for_character_and_enemy(character, enemy, enemy_name)
        actual = display_of_health.getvalue()
        self.assertEqual(expected, actual)

    def test_display_health_for_character_and_enemy_and_dictionaries_are_unchanged(self):
        character = {'health': 100}
        character_copy = {'health': 100}
        enemy = {'health': 100}
        enemy_copy = {'health': 100}
        enemy_name = 'coach'
        display_health_for_character_and_enemy(character, enemy, enemy_name)
        self.assertEqual(character, character_copy)
        self.assertEqual(enemy, enemy_copy)

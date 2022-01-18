from unittest import TestCase
from game import is_alive as is_alive


class TestIsAlive(TestCase):
    def test_is_alive_when_character_health_is_greater_than_zero(self):
        character = {"health": 5}
        expected_output = True
        actual_output = is_alive(character)
        self.assertEqual(expected_output, actual_output)

    def test_is_alive_when_character_health_is_zero(self):
        character = {"health": 0}
        expected_output = False
        actual_output = is_alive(character)
        self.assertEqual(expected_output, actual_output)

    def test_is_alive_when_character_health_is_less_than_zero(self):
        character = {"health": -10}
        expected_output = False
        actual_output = is_alive(character)
        self.assertEqual(expected_output, actual_output)

    def test_is_alive_and_character_dictionary_is_not_changed(self):
        character = {"health": 0}
        character_copy = {"health": 0}
        is_alive(character)
        self.assertEqual(character, character_copy)

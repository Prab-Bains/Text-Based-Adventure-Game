from unittest import TestCase
from game import move_character as move_character


class TestMoveCharacter(TestCase):
    def test_move_character_north(self):
        characters = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 5}
        direction = 'North'
        expected_output = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        actual_output = move_character(characters, direction)
        self.assertEqual(expected_output, actual_output)

    def test_move_character_south(self):
        characters = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        direction = 'South'
        expected_output = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 5}
        actual_output = move_character(characters, direction)
        self.assertEqual(expected_output, actual_output)

    def test_move_character_east(self):
        characters = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 5}
        direction = 'East'
        expected_output = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}
        actual_output = move_character(characters, direction)
        self.assertEqual(expected_output, actual_output)

    def test_move_character_west(self):
        characters = {"X-coordinate": 1, "Y-coordinate": 0, "Current HP": 5}
        direction = 'West'
        expected_output = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        actual_output = move_character(characters, direction)
        self.assertEqual(expected_output, actual_output)

from unittest import TestCase
from game import validate_move as validate_move


class TestValidateMove(TestCase):
    def test_validate_move_if_move_is_valid(self):
        board = {(0, 0): "Room 1", (0, 1): "Room 2", (1, 0): "Room 3", (1, 1): "Room 4"}
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        direction = 'South'
        expected_output = True
        actual_output = validate_move(board, character, direction)
        self.assertEqual(expected_output, actual_output)

    def test_validate_move_if_move_is_not_valid_along_left_border(self):
        board = {(0, 0): "Room one", (0, 1): "Room two", (1, 0): "Room three", (1, 1): "Room four"}
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        direction = 'West'
        expected_output = False
        actual_output = validate_move(board, character, direction)
        self.assertEqual(expected_output, actual_output)

    def test_validate_move_if_move_is_not_valid_along_top_border(self):
        board = {(0, 0): "Room one", (0, 1): "Room two", (1, 0): "Room three", (1, 1): "Room four"}
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        direction = 'North'
        expected_output = False
        actual_output = validate_move(board, character, direction)
        self.assertEqual(expected_output, actual_output)

    def test_validate_move_if_move_is_not_valid_along_right_border(self):
        board = {(0, 0): "Room one", (0, 1): "Room two", (1, 0): "Room three", (1, 1): "Room four"}
        character = {"X-coordinate": 1, "Y-coordinate": 0, "Current HP": 5}
        direction = 'East'
        expected_output = False
        actual_output = validate_move(board, character, direction)
        self.assertEqual(expected_output, actual_output)

    def test_validate_move_if_move_is_not_valid_along_bottom_border(self):
        board = {(0, 0): "Room one", (0, 1): "Room two", (1, 0): "Room three", (1, 1): "Room four"}
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}
        direction = 'East'
        expected_output = False
        actual_output = validate_move(board, character, direction)
        self.assertEqual(expected_output, actual_output)

    def test_validate_move_if_board_is_different_size(self):
        board = {(0, 0): "Room one", (0, 1): "Room two", (1, 0): "Room three", (1, 1): "Room four", (2, 0): "Room five",
                 (2, 1): "Room six"}
        character = {"X-coordinate": 2, "Y-coordinate": 1, "Current HP": 5}
        direction = 'East'
        expected_output = False
        actual_output = validate_move(board, character, direction)
        self.assertEqual(expected_output, actual_output)

    def test_validate_move_character_dictionary_not_changed(self):
        board = {(0, 0): "1", (0, 1): "2", (1, 0): "3", (1, 1): "4"}
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 3}
        direction = 'West'
        expected_output = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 3}
        validate_move(board, character, direction)
        self.assertEqual(expected_output, character)

    def test_validate_move_board_dictionary_not_changed(self):
        board = {(0, 0): "one", (0, 1): "two", (1, 0): "three", (1, 1): "four"}
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 2}
        direction = 'West'
        expected_output = {(0, 0): "one", (0, 1): "two", (1, 0): "three", (1, 1): "four"}
        validate_move(board, character, direction)
        self.assertEqual(expected_output, board)

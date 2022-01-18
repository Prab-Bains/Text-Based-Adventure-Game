from unittest import TestCase
from game import describe_current_location as describe_current_location


class TestDescribeCurrentLocation(TestCase):
    def test_describe_current_location_at_start_of_game(self):
        board = {(0, 0): 'You have entered the room of silent screams. There is nobody within '
                         'miles of you, nobody to hear you scream.',
                 (0, 1): "You have entered Annebelle's bedroom, you better hope you don't make "
                         'her mad!',
                 (1, 0): 'You have entered the sewers of IT, keep a lookout for Pennywise!',
                 (1, 1): 'You have entered a pitch black room with a spot light on Chucky. The '
                         'door slams shut! What will you do?'}

        character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}

        expected_output = 'You have entered the room of silent screams. There is nobody within miles of you, ' \
                          'nobody to hear you scream.'

        actual_output = describe_current_location(board, character)
        self.assertEqual(expected_output, actual_output)

    def test_describe_current_location_after_character_has_moved(self):
        board = {(0, 0): 'Room 1',
                 (0, 1): 'Room 2',
                 (1, 0): 'Room 3',
                 (1, 1): 'Room 4'}

        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}

        expected_output = 'Room 4'

        actual_output = describe_current_location(board, character)
        self.assertEqual(expected_output, actual_output)

    def test_describe_current_location_dictionary_is_unchanged(self):
        board = {(0, 0): 'Empty Room',
                 (0, 1): 'Empty Room',
                 (1, 0): 'Empty Room',
                 (1, 1): 'Empty Room'}

        board_copy = {(0, 0): 'Empty Room',
                      (0, 1): 'Empty Room',
                      (1, 0): 'Empty Room',
                      (1, 1): 'Empty Room'}

        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}
        character_copy = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}

        describe_current_location(board, character)

        self.assertEqual(board, board_copy)
        self.assertEqual(character, character_copy)

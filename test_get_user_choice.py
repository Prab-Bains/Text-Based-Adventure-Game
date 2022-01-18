from unittest import TestCase
from game import get_user_choice as get_user_choice
from unittest.mock import patch
import io


class TestGetUserChoice(TestCase):
    @patch('builtins.input', side_effect=[1])
    def test_get_user_choice_if_user_inputs_north(self, _):
        expected_output = 'North'
        actual_output = get_user_choice()
        self.assertEqual(expected_output, actual_output)

    @patch('builtins.input', side_effect=[3])
    def test_get_user_choice_if_user_inputs_south(self, _):
        expected_output = 'South'
        actual_output = get_user_choice()
        self.assertEqual(expected_output, actual_output)

    @patch('builtins.input', side_effect=[2])
    def test_get_user_choice_if_user_inputs_east(self, _):
        expected_output = 'East'
        actual_output = get_user_choice()
        self.assertEqual(expected_output, actual_output)

    @patch('builtins.input', side_effect=[4])
    def test_get_user_choice_if_user_inputs_west(self, _):
        expected_output = 'West'
        actual_output = get_user_choice()
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['North', 1])
    def test_get_user_choice_if_user_inputs_is_incorrect_first_time(self, _, error_message):
        expected_output = 'North'
        actual_output = get_user_choice()
        expected_error_message = """
1.) North
2.) East
3.) South
4.) West
That is not a valid input\n"""
        self.assertEqual(expected_output, actual_output)
        self.assertEqual(expected_error_message, error_message.getvalue())

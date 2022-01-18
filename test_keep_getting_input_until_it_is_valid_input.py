from unittest import TestCase
from unittest.mock import patch
from game import keep_getting_input_until_it_is_valid_input as keep_getting_input_until_it_is_valid_input


class TestKeepGettingUserInputUntilItIsValid(TestCase):
    @patch('builtins.input', side_effect=[3])
    def test_keep_getting_input_until_it_is_valid_input_when_first_input_is_valid(self, _):
        options = ['Hello', 'Hola', 'Hi', 'Salut']
        responses = ['1', '2', '3', '4']
        expected = 'Hi'
        actual = keep_getting_input_until_it_is_valid_input(options, responses)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['wsediifgawe', 3])
    def test_keep_getting_input_until_it_is_valid_input_when_first_input_is_not_valid(self, _):
        options = ['Hello', 'Hola', 'Hi', 'Salut']
        responses = ['1', '2', '3', '4']
        expected = 'Hi'
        actual = keep_getting_input_until_it_is_valid_input(options, responses)
        self.assertEqual(expected, actual)

from unittest import TestCase
from unittest.mock import patch
from game import get_user_name as get_user_name


class TestGetUserName(TestCase):
    @patch('builtins.input', side_effect=['Prab'])
    def test_get_user_name_when_name_is_letters(self, _):
        expected = 'Prab'
        actual = get_user_name()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=[1234])
    def test_get_user_name_when_name_is_numbers(self, _):
        expected = 1234
        actual = get_user_name()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['Prab123'])
    def test_get_user_name_when_name_is_numbers_and_letters(self, _):
        expected = 'Prab123'
        actual = get_user_name()
        self.assertEqual(expected, actual)
from unittest import TestCase
from unittest.mock import patch
from game import get_class_name as get_class_name


class TestGetClassName(TestCase):
    @patch('builtins.input', side_effect=[1])
    def test_get_class_name_when_user_selects_first_class(self, _):
        expected = 'MMA Fighter'
        actual = get_class_name()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=[2])
    def test_get_class_name_when_user_selects_second_class(self, _):
        expected = 'Hockey Player'
        actual = get_class_name()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=[3])
    def test_get_class_name_when_user_selects_third_class(self, _):
        expected = 'Football Player'
        actual = get_class_name()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=[4])
    def test_get_class_name_when_user_selects_fourth_class(self, _):
        expected = 'Baseball Player'
        actual = get_class_name()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['class one', 4])
    def test_get_class_name_when_user_inputs_something_besides_number_between_one_and_four(self, _):
        expected = 'Baseball Player'
        actual = get_class_name()
        self.assertEqual(expected, actual)

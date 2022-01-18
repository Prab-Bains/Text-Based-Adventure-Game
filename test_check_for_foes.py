from unittest import TestCase
from unittest.mock import patch
from game import check_for_foes


class TestCheckForFoes(TestCase):
    @patch('random.randint', side_effect=[4])
    def test_check_for_foes_when_return_is_false(self, _):
        character = {'level': 'waterboy'}
        expected = False
        actual = check_for_foes(character)
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1])
    def test_check_for_foes_when_return_is_true(self, _):
        character = {'level': 'waterboy'}
        expected = True
        actual = check_for_foes(character)
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[4])
    def test_check_for_foes_when_return_is_supposed_to_be_false_but_character_is_level_three(self, _):
        character = {'level': 'superstar'}
        expected = True
        actual = check_for_foes(character)
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1])
    def test_check_for_foes_character_dictionary_is_unchanged(self, _):
        character = {'level': 'waterboy'}
        character_copy = {'level': 'waterboy'}
        check_for_foes(character)
        self.assertEqual(character, character_copy)

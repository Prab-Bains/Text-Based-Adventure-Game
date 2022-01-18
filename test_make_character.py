from unittest import TestCase
from unittest.mock import patch
from game import make_character as make_character


class TestMakeCharacter(TestCase):
    # the input 1 refers to the 'MMA Fighter' class
    @patch('builtins.input', side_effect=['Prab', 1])
    def test_make_character(self, _):

        expected = {'name': 'Prab', 'class_name': 'MMA Fighter', 'health': 50, 'damage': 30, 'accuracy': 50,
                    'level': 'waterboy', 'attack': ['jab', 'right hook', 'uppercut'], "X-coordinate": 0,
                    "Y-coordinate": 0, 'current experience': 0, 'experience needed': 100}

        actual = make_character()
        self.assertEqual(actual, expected)


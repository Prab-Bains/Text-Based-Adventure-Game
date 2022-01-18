from unittest import TestCase
from unittest.mock import patch
from game import take_damage_when_running_away as take_damage_when_running_away


class TestTakeDamageWhenRunningAway(TestCase):
    @patch('random.randint', side_effect=[4])
    def test_take_damage_when_running_away_when_return_value_is_false(self, _):
        expected = False
        actual = take_damage_when_running_away()
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1])
    def test_take_damage_when_running_away_when_return_value_is_true(self, _):
        expected = True
        actual = take_damage_when_running_away()
        self.assertEqual(expected, actual)

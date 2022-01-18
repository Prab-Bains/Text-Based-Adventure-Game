from unittest import TestCase
from unittest.mock import patch
from game import foe_runs_away as foe_runs_away


class TestFoeRunsAway(TestCase):
    @patch('random.randint', side_effect=[4])
    def test_foe_runs_away_when_return_is_false(self, _):
        expected = False
        actual = foe_runs_away()
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1])
    def test_foe_runs_away_when_return_is_true(self, _):
        expected = True
        actual = foe_runs_away()
        self.assertEqual(expected, actual)

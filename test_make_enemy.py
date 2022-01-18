from unittest import TestCase
from unittest.mock import patch
from game import make_enemy as make_enemy


class TestMakeEnemy(TestCase):
    @patch('random.randint', side_effect=[0])
    def test_make_enemy(self, _):
        expected = {'name': 'trainer', 'damage': 10, 'health': 50}
        actual = make_enemy()
        self.assertEqual(expected, actual)

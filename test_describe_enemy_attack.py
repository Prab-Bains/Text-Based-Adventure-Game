from unittest import TestCase
from unittest.mock import patch
from game import describe_enemy_attack as describe_enemy_attack


class TestDescribeEnemyAttack(TestCase):
    @patch('random.randint', side_effect=[0])
    def test_describe_enemy_attack_with_first_attack_in_enemy_attack_list(self, _):
        opponent = 'coach'
        expected = 'Your ' + opponent + ' counters your attack and hits you with a spartan kick'
        actual = describe_enemy_attack(opponent)
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1])
    def test_describe_enemy_attack_with_second_attack_in_enemy_attack_list(self, _):
        opponent = 'coach'
        expected = 'Your ' + opponent + ' counters your attack and hits you with a RKO'
        actual = describe_enemy_attack(opponent)
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[2])
    def test_describe_enemy_attack_with_third_attack_in_enemy_attack_list(self, _):
        opponent = 'coach'
        expected = 'Your ' + opponent + ' counters your attack and hits you with a choke slam'
        actual = describe_enemy_attack(opponent)
        self.assertEqual(expected, actual)

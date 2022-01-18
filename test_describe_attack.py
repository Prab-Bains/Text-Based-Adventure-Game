from unittest import TestCase
from unittest.mock import patch
from game import describe_attack as describe_attack


class TestDescribeAttack(TestCase):
    @patch('random.randint', side_effect=[0])
    def test_describe_attack_first_attack_in_character_attack_list(self, _):
        character = {'attack': ['jab', 'right hook', 'uppercut']}
        opponent = 'enemy'
        expected = 'You attack your ' + opponent + ' with a jab'
        actual = describe_attack(character, opponent)
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1])
    def test_describe_attack_second_attack_in_character_attack_list(self, _):
        character = {'attack': ['jab', 'right hook', 'uppercut']}
        opponent = 'enemy'
        expected = 'You attack your ' + opponent + ' with a right hook'
        actual = describe_attack(character, opponent)
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[2])
    def test_describe_attack_third_attack_in_character_attack_list(self, _):
        character = {'attack': ['jab', 'right hook', 'uppercut']}
        opponent = 'enemy'
        expected = 'You attack your ' + opponent + ' with a uppercut'
        actual = describe_attack(character, opponent)
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[2])
    def test_describe_attack_character_dictionary_is_not_changed(self, _):
        character = {'attack': ['jab', 'right hook', 'uppercut']}
        character_copy = {'attack': ['jab', 'right hook', 'uppercut']}
        opponent = 'enemy'
        describe_attack(character, opponent)
        self.assertEqual(character, character_copy)

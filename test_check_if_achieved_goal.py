from unittest import TestCase
from game import check_if_achieved_goal as check_if_achieved_goal


class TestCheckIfAchievedGoal(TestCase):
    def test_check_if_achieved_goal_when_character_has_not_achieved_the_goal(self):
        character = {'level': 'waterboy', 'current experience': 0, 'experience needed': 100}
        expected = False
        actual = check_if_achieved_goal(character)
        self.assertEqual(expected, actual)

    def test_check_if_achieved_goal_when_character_has_achieved_the_goal(self):
        character = {'level': 'superstar', 'current experience': 100, 'experience needed': 100}
        expected = True
        actual = check_if_achieved_goal(character)
        self.assertEqual(expected, actual)

    def test_check_if_achieved_goal_when_character_has_reached_level_three_but_not_beat_boss(self):
        character = {'level': 'superstar', 'current experience': 0, 'experience needed': 100}
        expected = False
        actual = check_if_achieved_goal(character)
        self.assertEqual(expected, actual)

    def test_check_if_achieved_goal_dictionary_is_not_changed(self):
        character = {'level': 'superstar', 'current experience': 100, 'experience needed': 100}
        character_copy = {'level': 'superstar', 'current experience': 100, 'experience needed': 100}
        check_if_achieved_goal(character)
        self.assertEqual(character, character_copy)

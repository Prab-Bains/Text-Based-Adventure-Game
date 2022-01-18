from unittest import TestCase
from game import update_enemy_attributes as update_enemy_attributes


class TestEnemyAttributes(TestCase):
    def test_update_enemy_attributes_when_character_is_level_one(self):
        character = {'level': 'waterboy'}
        enemy = {'name': 'trainer', 'damage': 10, 'health': 0}
        expected = {'name': 'trainer', 'damage': 10, 'health': 50}
        actual = update_enemy_attributes(character, enemy)
        self.assertEqual(expected, actual)

    def test_update_enemy_attributes_when_character_is_level_two(self):
        character = {'level': 'benchwarmer'}
        enemy = {'name': 'trainer', 'damage': 10, 'health': 50}
        expected = {'name': 'trainer', 'damage': 10, 'health': 120}
        actual = update_enemy_attributes(character, enemy)
        self.assertEqual(expected, actual)

    def test_update_enemy_attributes_when_character_is_level_three(self):
        character = {'level': 'superstar'}
        enemy = {'name': 'trainer', 'damage': 10, 'health': 120}
        expected = {'name': 'trainer', 'damage': 10, 'health': 500}
        actual = update_enemy_attributes(character, enemy)
        self.assertEqual(expected, actual)

    def test_update_enemy_attributes_and_character_dictionary_is_not_changed(self):
        character = {'level': 'superstar'}
        character_copy = {'level': 'superstar'}
        enemy = {'name': 'trainer', 'damage': 10, 'health': 120}
        update_enemy_attributes(character, enemy)
        self.assertEqual(character, character_copy)

from unittest import TestCase
from game import enemy_is_alive as enemy_is_alive


class TestEnemyIsAlive(TestCase):
    def test_enemy_is_alive_when_enemy_health_is_greater_than_zero(self):
        enemy = {"health": 5}
        expected_output = True
        actual_output = enemy_is_alive(enemy)
        self.assertEqual(expected_output, actual_output)

    def test_enemy_is_alive_when_enemy_health_is_zero(self):
        enemy = {"health": 0}
        expected_output = False
        actual_output = enemy_is_alive(enemy)
        self.assertEqual(expected_output, actual_output)

    def test_enemy_is_alive_when_enemy_health_is_less_than_zero(self):
        enemy = {"health": -5}
        expected_output = False
        actual_output = enemy_is_alive(enemy)
        self.assertEqual(expected_output, actual_output)

    def test_enemy_is_alive_and_enemy_dictionary_is_unchanged(self):
        enemy = {"health": 0}
        enemy_copy = {"health": 0}
        enemy_is_alive(enemy)
        self.assertEqual(enemy, enemy_copy)

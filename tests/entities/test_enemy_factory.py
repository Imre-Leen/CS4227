import unittest

from src.entities import enemy_factory
from src.entities import enemy_tile


class TestEnemyFactory(unittest.TestCase):

    def test_create_enemy_normal(self):
        enemy_fact = enemy_factory.EnemyFactory()
        enemy_actual = enemy_fact.create_enemy("normal")
        enemy_expected = enemy_tile.EnemyTile(1.0, 0.0, 0.5, 380, 350, 10, 10)
        self.assertEqual(enemy_actual.x_pos, enemy_expected.x_pos)
        self.assertEqual(enemy_actual.y_pos, enemy_expected.y_pos)
        self.assertEqual(enemy_actual.width, enemy_expected.width)
        self.assertEqual(enemy_actual.height, enemy_expected.height)
        self.assertEqual(enemy_actual.red_val, enemy_expected.red_val)
        self.assertEqual(enemy_actual.green_val, enemy_expected.green_val)
        self.assertEqual(enemy_actual.blue_val, enemy_expected.blue_val)

    def test_create_enemy_boss(self):
        enemy_fact = enemy_factory.EnemyFactory()
        enemy_actual = enemy_fact.create_enemy("boss")
        enemy_expected = enemy_tile.EnemyTile(1.0, 0.0, 3.0, 380, 350, 10, 10)
        self.assertEqual(enemy_actual.x_pos, enemy_expected.x_pos)
        self.assertEqual(enemy_actual.y_pos, enemy_expected.y_pos)
        self.assertEqual(enemy_actual.width, enemy_expected.width)
        self.assertEqual(enemy_actual.height, enemy_expected.height)
        self.assertEqual(enemy_actual.red_val, enemy_expected.red_val)
        self.assertEqual(enemy_actual.green_val, enemy_expected.green_val)
        self.assertEqual(enemy_actual.blue_val, enemy_expected.blue_val)
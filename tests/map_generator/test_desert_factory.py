import unittest

from src.map_generator.desert_factory import DesertFactory


class TestDesertFactory(unittest.TestCase):

    def test_desert_factory_floor(self):
        factory = DesertFactory()
        actual_floor_data = factory.get_floor_tile_data()
        expected_floor_data = (1, 0.8, 0.0)
        self.assertEqual(actual_floor_data, expected_floor_data)
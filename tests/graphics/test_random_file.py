"""
This test class is here to demonstrate how testing is done on an individual method
"""
import unittest

from src.graphics import random_file


class TestRandomFile(unittest.TestCase):

    def test_random_method(self):
        actual_result = random_file.random_method()
        expected_result = 11
        self.assertEqual(actual_result, expected_result)

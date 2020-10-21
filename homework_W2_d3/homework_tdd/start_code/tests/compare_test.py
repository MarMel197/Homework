import unittest

from src.compare import compare

class TestCompare(unittest.TestCase):

    def test_compare_3_1_returns_3_is_greater_than_1(self):
        self.assertEqual("3 is greater than 1", compare(3, 1))

    def test_compare_5_5_returns_5_is_equal_to_5(self):
        self.assertEqual("5 is equal to 5", compare(5, 5))

    def test_compare_2_8_returns_2_is_less_than_8(self):
        self.assertEqual("2 is less than 8", compare(2, 8))

    def test_compare_1000000_1000000_returns_is_equal_to(self):
        self.assertEqual("1000000 is equal to 1000000", compare(1000000, 1000000))
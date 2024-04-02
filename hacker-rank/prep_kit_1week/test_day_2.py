from unittest import TestCase

from day_2 import *


class Test(TestCase):
    def test_lonelyinteger(self):
        result = lonelyinteger([1, 2, 2, 1, 3, 6, 6, 7, 7])
        self.assertEqual(3, result)

    def test_diagonaldifference_case0(self):
        arr = [
            [1, 2, 3],
            [4, 5, 6],
            [9, 8, 9]
        ]
        result = diagonalDifference(arr)
        self.assertEqual(2, result)

    def test_diagonaldifference_case1(self):
        arr = [
            [11, 2, 4],
            [4, 5, 6],
            [10, 8, -12]
        ]
        result = diagonalDifference(arr)
        self.assertEqual(15, result)

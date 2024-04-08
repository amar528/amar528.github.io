from unittest import TestCase

from binary_tree import *
from mini_abs_diff_bfs_530 import Solution


class TestSolution(TestCase):
    def test_get_minimum_difference_example1(self):
        root = build_tree([4, 2, 6, 1, 3])

        sol = Solution()
        result = sol.getMinimumDifference(root)

        self.assertEquals(1, result)

    def test_get_minimum_difference_example2(self):
        root = build_tree([1, 0, 48, None, None, 12, 49])

        sol = Solution()
        result = sol.getMinimumDifference(root)

        self.assertEquals(1, result)

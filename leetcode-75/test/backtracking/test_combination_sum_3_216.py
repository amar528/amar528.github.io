from unittest import TestCase

from leetcode75.backtracking.combination_sum_3_216 import Solution


class TestSolution(TestCase):
    def test_combination_sum3_example1(self):
        k = 3
        n = 7

        sol = Solution()

        result = sol.combinationSum3(k, n)
        self.assertListEqual([[1, 2, 4]], result)
        # only 1 way to sum 7 = 1 + 2 + 4

    def test_combination_sum3_example2(self):
        k = 3
        n = 9

        sol = Solution()

        result = sol.combinationSum3(k, n)
        self.assertListEqual([
            [1, 2, 6],
            [1, 3, 5],
            [2, 3, 4]], result)
        # 1 + 2 + 6 = 9
        # 1 + 3 + 5 = 9
        # 2 + 3 + 4 = 9

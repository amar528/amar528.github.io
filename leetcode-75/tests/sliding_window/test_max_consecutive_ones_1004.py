from unittest import TestCase

from leetcode75.sliding_window.max_consecutive_ones_1004 import Solution


class TestSolution(TestCase):
    def test_longest_ones_example1(self):
        nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
        k = 2

        sol = Solution()
        result = sol.longestOnes(nums, k)

        self.assertEqual(6, result)

    def test_longest_ones_example2(self):
        nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
        k = 3

        sol = Solution()
        result = sol.longestOnes(nums, k)

        self.assertEqual(10, result)

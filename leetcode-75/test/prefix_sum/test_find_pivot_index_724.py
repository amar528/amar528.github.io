from unittest import TestCase

from leetcode75.prefix_sum.find_pivot_index_724 import Solution


class TestSolution(TestCase):
    def test_pivot_index_example1(self):
        nums = [1, 7, 3, 6, 5, 6]
        #       1, 8, 11, , 5, 11,
        # n = 6          ^
        # [0, 1, 8, 11, 17, 22, 28, 0]

        sol = Solution()
        result = sol.pivotIndex(nums)

        self.assertEqual(3, result)

    def test_pivot_index_example2(self):
        nums = [1, 2, 3]

        sol = Solution()
        result = sol.pivotIndex(nums)

        self.assertEqual(-1, result)

    def test_pivot_index_example3(self):
        nums = [2, 1, -1]

        sol = Solution()
        result = sol.pivotIndex(nums)

        self.assertEqual(0, result)

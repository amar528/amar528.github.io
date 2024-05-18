from unittest import TestCase

from leetcode75.two_pointers.max_num_k_sum_pairs_1679 import Solution


class TestSolution(TestCase):
    def test_max_operations_example1(self):
        nums = [1, 2, 3, 4]
        k = 5

        sol = Solution()
        result = sol.maxOperations(nums, k)

        self.assertEqual(2, result)

    def test_max_operations_example2(self):
        nums = [3, 1, 3, 4, 3]
        k = 6

        sol = Solution()
        result = sol.maxOperations(nums, k)

        self.assertEqual(1, result)

    def test_max_operations_example3(self):
        nums = [4, 4, 1, 3, 1, 3, 2, 2, 5, 5, 1, 5, 2, 1, 2, 3, 5, 4]
        k = 2

        sol = Solution()
        result = sol.maxOperations(nums, k)

        self.assertEqual(2, result)

    def test_max_operations_example4(self):
        nums = [2, 2, 2, 3, 1, 1, 4, 1]
        k = 4

        sol = Solution()
        result = sol.maxOperations(nums, k)

        self.assertEqual(2, result)

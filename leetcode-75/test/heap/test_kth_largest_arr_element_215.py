from unittest import TestCase

from leetcode75.heap.kth_largest_arr_element_215 import Solution


class TestSolution(TestCase):
    def test_find_kth_largest_example1(self):
        nums = [3, 2, 1, 5, 6, 4]
        k = 2

        expected = 5

        sol = Solution()
        result = sol.findKthLargest(nums, k)

        self.assertEqual(expected, result)

    def test_find_kth_largest_example2(self):
        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        k = 4

        expected = 4

        sol = Solution()
        result = sol.findKthLargest(nums, k)

        self.assertEqual(expected, result)

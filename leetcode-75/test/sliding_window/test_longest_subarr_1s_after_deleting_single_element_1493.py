from unittest import TestCase

from leetcode75.sliding_window.longest_subarr_1s_after_deleting_single_element_1493 import Solution


class TestSolution(TestCase):
    def test_longest_subarray_example1(self):
        nums = [1, 1, 0, 1]

        sol = Solution()
        result = sol.longestSubarray(nums)

        self.assertEqual(3, result)

    def test_longest_subarray_example2(self):
        nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]

        sol = Solution()
        result = sol.longestSubarray(nums)

        self.assertEqual(5, result)

    def test_longest_subarray_example3(self):
        nums = [1, 1, 1]

        sol = Solution()
        result = sol.longestSubarray(nums)

        self.assertEqual(2, result)

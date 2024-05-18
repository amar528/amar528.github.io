from unittest import TestCase

from leetcode75.hashmap_set.find_diff_2_arrays_2215 import Solution


class TestSolution(TestCase):
    def test_find_difference_example1(self):
        nums1 = [1, 2, 3]
        nums2 = [2, 4, 6]

        sol = Solution()
        result = sol.findDifference(nums1, nums2)

        self.assertListEqual([[1, 3], [4, 6]], result)

    def test_find_difference_example2(self):
        nums1 = [1, 2, 3, 3]
        nums2 = [1, 1, 2, 2]

        sol = Solution()
        result = sol.findDifference(nums1, nums2)

        self.assertListEqual([[3], []], result)

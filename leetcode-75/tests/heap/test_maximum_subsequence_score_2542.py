from unittest import TestCase

from leetcode75.heap.maximum_subsequence_score_2542 import Solution


class TestSolution(TestCase):
    def test_max_score_example1(self):
        nums1 = [1, 3, 3, 2]
        nums2 = [2, 1, 3, 4]
        k = 3

        sol = Solution()
        result = sol.maxScore(nums1, nums2, k)

        self.assertEqual(12, result)

    def test_max_score_example2(self):
        nums1 = [4, 2, 3, 1, 1]
        nums2 = [7, 5, 10, 9, 6]
        k = 1

        sol = Solution()
        result = sol.maxScore(nums1, nums2, k)

        self.assertEqual(30, result)

    def test_max_score_example14(self):
        nums1 = [2, 1, 14, 12]
        nums2 = [11, 7, 13, 6]
        k = 3

        sol = Solution()
        result = sol.maxScore(nums1, nums2, k)

        self.assertEqual(168, result)

    def test_max_score_example15(self):
        nums1 = [23, 16, 20, 7, 3]
        nums2 = [19, 21, 22, 22, 12]
        k = 3

        sol = Solution()
        result = sol.maxScore(nums1, nums2, k)

        self.assertEqual(1121, result)

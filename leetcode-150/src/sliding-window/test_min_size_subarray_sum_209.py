from unittest import TestCase
from min_size_subarray_sum_209 import Solution


class TestSolution(TestCase):
    def test_min_sub_array_len_case0(self):
        sol = Solution()
        target = 7
        nums = [2, 3, 1, 2, 4, 3]

        result = sol.minSubArrayLen(target, nums)
        # [4, 3]
        self.assertEqual(2, result)

    def test_min_sub_array_len_case1(self):
        sol = Solution()
        target = 4
        nums = [1, 4, 4]

        result = sol.minSubArrayLen(target, nums)
        self.assertEqual(1, result)

    def test_min_sub_array_len_case2(self):
        sol = Solution()
        target = 11
        nums = [1, 1, 1, 1, 1, 1, 1, 1]

        result = sol.minSubArrayLen(target, nums)
        self.assertEqual(0, result)

    def test_min_sub_array_len_case10(self):
        sol = Solution()
        target = 11
        nums = [1, 2, 3, 4, 5]

        result = sol.minSubArrayLen(target, nums)
        self.assertEqual(3, result)

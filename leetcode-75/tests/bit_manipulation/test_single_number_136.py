from unittest import TestCase

from leetcode75.bit_manipulation.single_number_136 import Solution


class TestSolution(TestCase):
    def test_single_number_example1(self):
        nums = [2, 2, 1]

        sol = Solution()
        result = sol.singleNumber(nums)

        self.assertEqual(1, result)

    def test_single_number_example2(self):
        nums = [4, 1, 2, 1, 2]

        sol = Solution()
        result = sol.singleNumber(nums)

        self.assertEqual(4, result)

    def test_single_number_example3(self):
        nums = [1]

        sol = Solution()
        result = sol.singleNumber(nums)

        self.assertEqual(1, result)

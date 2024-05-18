from unittest import TestCase

from leetcode75.array_string.product_of_array_except_self_238 import Solution


class TestSolution(TestCase):
    def test_product_except_self_example1(self):
        nums = [1, 2, 3, 4]
        #       1  1  2  6 : prefix product
        #

        sol = Solution()
        result = sol.productExceptSelf(nums)

        self.assertListEqual([24, 12, 8, 6], result)

    def test_product_except_self_example2(self):
        nums = [-1, 1, 0, -3, 3]

        sol = Solution()
        result = sol.productExceptSelf(nums)

        self.assertListEqual([0, 0, 9, 0, 0], result)

from unittest import TestCase

from leetcode75.two_pointers.move_zeros_2p_283 import Solution


class TestSolution(TestCase):
    def test_move_zeroes_example1(self):
        nums = [0, 1, 0, 3, 12]

        sol = Solution()
        sol.moveZeroes(nums)

        self.assertListEqual([1, 3, 12, 0, 0], nums)

    def test_move_zeroes_example2(self):
        nums = [0]

        sol = Solution()
        sol.moveZeroes(nums)

        self.assertListEqual([0], nums)

    def test_move_zeroes_example29(self):
        nums = [0, 0, 1]

        sol = Solution()
        sol.moveZeroes(nums)

        self.assertListEqual([1, 0, 0], nums)

    def test_move_zeroes_example6(self):
        nums = [1, 0]

        sol = Solution()
        sol.moveZeroes(nums)

        self.assertListEqual([1, 0], nums)

from unittest import TestCase
from leetcode75.bit_manipulation.counting_bits_338 import Solution


class TestSolution(TestCase):
    def test_count_bits(self):
        sol = Solution()
        result = sol.countBits(5)

        self.assertListEqual([0, 1, 1, 2, 1, 2], result)

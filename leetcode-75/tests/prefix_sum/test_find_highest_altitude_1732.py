from unittest import TestCase

from leetcode75.prefix_sum.find_highest_altitude_1732 import Solution


class TestSolution(TestCase):
    def test_largest_altitude_example1(self):
        gain = [-5, 1, 5, 0, -7]

        sol = Solution()
        result = sol.largestAltitude(gain)

        self.assertEqual(1, result)

    def test_largest_altitude_example2(self):
        gain = [-4, -3, -2, -1, 4, 3, 2]

        sol = Solution()
        result = sol.largestAltitude(gain)

        self.assertEqual(0, result)

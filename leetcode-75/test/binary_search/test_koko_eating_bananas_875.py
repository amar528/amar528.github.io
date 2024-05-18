from unittest import TestCase

from leetcode75.binary_search.koko_eating_bananas_875 import Solution


class TestSolution(TestCase):
    def test_min_eating_speed_example1(self):
        piles = [3, 6, 7, 11]
        h = 8

        sol = Solution()
        result = sol.minEatingSpeed(piles, h)

        self.assertEqual(4, result)

    def test_min_eating_speed_example2(self):
        piles = [30, 11, 23, 4, 20]
        h = 5

        sol = Solution()
        result = sol.minEatingSpeed(piles, h)

        self.assertEqual(30, result)

    def test_min_eating_speed_example3(self):
        piles = [30, 11, 23, 4, 20]
        h = 6

        sol = Solution()
        result = sol.minEatingSpeed(piles, h)

        self.assertEqual(23, result)

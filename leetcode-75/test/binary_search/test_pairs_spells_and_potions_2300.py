from unittest import TestCase
from leetcode75.binary_search.pairs_spells_and_potions_2300 import Solution


class TestSolution(TestCase):
    def test_successful_pairs_example1(self):
        spells = [5, 1, 3]
        potions = [1, 2, 3, 4, 5]
        success = 7

        sol = Solution()
        result = sol.successfulPairs(spells, potions, success)

        self.assertListEqual([4, 0, 3], result)

    def test_successful_pairs_example2(self):
        spells = [3, 1, 2]
        potions = [8, 5, 8]
        success = 16

        sol = Solution()
        result = sol.successfulPairs(spells, potions, success)

        self.assertListEqual([2, 0, 2], result)

    def test_successful_pairs_example3(self):
        spells = [1, 2, 3, 4, 5, 6, 7]
        potions = [1, 2, 3, 4, 5, 6, 7]
        success = 25

        sol = Solution()
        result = sol.successfulPairs(spells, potions, success)

        self.assertListEqual([0, 0, 0, 1, 3, 3, 4], result)

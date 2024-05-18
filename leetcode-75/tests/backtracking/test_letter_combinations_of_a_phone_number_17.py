from unittest import TestCase

from leetcode75.backtracking.letter_combinations_of_a_phone_number_17 import Solution


class TestSolution(TestCase):
    def test_letter_combinations_example1(self):
        digits = "23"

        sol = Solution()
        result = sol.letterCombinations(digits)

        self.assertListEqual(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], result)

    def test_letter_combinations_example2(self):
        digits = ""

        sol = Solution()
        result = sol.letterCombinations(digits)

        self.assertListEqual([], result)

    def test_letter_combinations_example3(self):
        digits = "2"

        sol = Solution()
        result = sol.letterCombinations(digits)

        self.assertListEqual(["a", "b", "c"], result)

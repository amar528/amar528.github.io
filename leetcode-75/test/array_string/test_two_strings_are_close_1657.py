from unittest import TestCase

from leetcode75.array_string.two_strings_are_close_1657 import Solution


class TestSolution(TestCase):
    def test_close_strings_example1(self):
        word1 = "abc"
        word2 = "bca"

        sol = Solution()
        result = sol.closeStrings(word1, word2)

        self.assertTrue(result)

    def test_close_strings_example2(self):
        word1 = "a"
        word2 = "aa"

        sol = Solution()
        result = sol.closeStrings(word1, word2)

        self.assertFalse(result)

    def test_close_strings_example3(self):
        word1 = "cabbba"
        word2 = "abbccc"

        sol = Solution()
        result = sol.closeStrings(word1, word2)

        self.assertTrue(result)

    def test_close_strings_example4(self):
        word1 = "abbzzca"
        word2 = "babzzcz"

        sol = Solution()
        result = sol.closeStrings(word1, word2)

        self.assertFalse(result)

    def test_close_strings_example5(self):
        word1 = "aaabbbbccddeeeeefffff"
        word2 = "aaaaabbcccdddeeeeffff"

        sol = Solution()
        result = sol.closeStrings(word1, word2)

        self.assertFalse(result)

    def test_close_strings_example6(self):
        word1 = "abbzccca"
        word2 = "babzzczc"

        sol = Solution()
        result = sol.closeStrings(word1, word2)

        self.assertTrue(result)

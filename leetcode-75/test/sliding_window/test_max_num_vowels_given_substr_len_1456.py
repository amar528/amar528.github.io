from unittest import TestCase

from leetcode75.sliding_window.max_num_vowels_given_substr_len_1456 import Solution


class TestSolution(TestCase):
    def test_max_vowels_example1(self):
        s = "abciiidef"
        k = 3

        sol = Solution()
        result = sol.maxVowels(s, k)

        self.assertEqual(3, result)

    def test_max_vowels_example2(self):
        s = "aeiou"
        k = 2

        sol = Solution()
        result = sol.maxVowels(s, k)

        self.assertEqual(2, result)

    def test_max_vowels_example3(self):
        s = "leetcode"
        k = 3

        sol = Solution()
        result = sol.maxVowels(s, k)

        self.assertEqual(2, result)

    def test_max_vowels_example4(self):
        s = "weallloveyou"
        k = 7

        sol = Solution()
        result = sol.maxVowels(s, k)

        self.assertEqual(4, result)

    def test_max_vowels_example45(self):
        s = "tryhard"
        k = 4

        sol = Solution()
        result = sol.maxVowels(s, k)

        self.assertEqual(1, result)

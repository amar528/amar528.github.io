from unittest import TestCase

from leetcode75.array_string.reverse_vowels_of_a_string_345 import Solution


class TestSolution(TestCase):
    def test_reverse_vowels_example1(self):
        s = 'hello'
        sol = Solution()
        result = sol.reverseVowels(s)

        self.assertEqual('holle', result)

    def test_reverse_vowels_example2(self):
        s = 'leetcode'
        sol = Solution()
        result = sol.reverseVowels(s)

        self.assertEqual('leotcede', result)

    def test_reverse_vowels_example3(self):
        s = ',.'
        sol = Solution()
        result = sol.reverseVowels(s)

        self.assertEqual(',.', result)

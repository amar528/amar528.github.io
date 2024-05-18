from unittest import TestCase

from leetcode75.array_string.reverse_words_in_a_string_151 import Solution


class TestSolution(TestCase):
    def test_reverse_words_example1(self):
        s = "the sky is blue"

        sol = Solution()
        result = sol.reverseWords(s)

        self.assertEqual('blue is sky the', result)

    def test_reverse_words_example2(self):
        s = "  hello world  "

        sol = Solution()
        result = sol.reverseWords(s)

        self.assertEqual('world hello', result)

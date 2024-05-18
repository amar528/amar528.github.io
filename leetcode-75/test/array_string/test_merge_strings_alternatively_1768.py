from unittest import TestCase

from leetcode75.array_string.merge_strings_alternatively_1768 import Solution


class TestSolution(TestCase):
    def test_merge_alternately_example1(self):
        word1 = "abc"
        word2 = "pqr"

        sol = Solution()
        result = sol.mergeAlternately(word1, word2)

        self.assertEqual('apbqcr', result)

    def test_merge_alternately_example2(self):
        word1 = "ab"
        word2 = "pqrs"

        sol = Solution()
        result = sol.mergeAlternately(word1, word2)

        self.assertEqual('apbqrs', result)

    def test_merge_alternately_example3(self):
        word1 = "abcd"
        word2 = "pq"

        sol = Solution()
        result = sol.mergeAlternately(word1, word2)

        self.assertEqual('apbqcd', result)

from unittest import TestCase

from leetcode75.two_pointers.is_subsequence_392 import Solution


class TestSolution(TestCase):
    def test_is_subsequence_example1(self):
        s = "abc"
        t = "ahbgdc"

        sol = Solution()
        result = sol.isSubsequence(s, t)

        self.assertTrue(result)

    def test_is_subsequence_example2(self):
        s = "axc"
        t = "ahbgdc"

        sol = Solution()
        result = sol.isSubsequence(s, t)

        self.assertFalse(result)

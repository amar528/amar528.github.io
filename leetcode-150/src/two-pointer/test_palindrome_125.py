from unittest import TestCase
from palindrome_125 import Solution


class TestSolution(TestCase):
    def test_is_palindrome_case0(self):
        sol = Solution()
        result = sol.isPalindrome('A man, a plan, a canal: Panama')
        self.assertTrue(result)

    def test_is_palindrome_case1(self):
        sol = Solution()
        result = sol.isPalindrome('race a car')
        self.assertFalse(result)

from unittest import TestCase

from stack.valid_parenthesis_20 import Solution


class TestSolution(TestCase):
    def test_is_valid_example1(self):
        s = '()'

        sol = Solution()
        result = sol.isValid(s)

        self.assertTrue(result)

    def test_is_valid_example2(self):
        s = '(){}[]()[]'

        sol = Solution()
        result = sol.isValid(s)

        self.assertTrue(result)

    def test_is_valid_example3(self):
        s = '(}'

        sol = Solution()
        result = sol.isValid(s)

        self.assertFalse(result)

    def test_is_valid_example4(self):
        s = '([])'

        sol = Solution()
        result = sol.isValid(s)

        self.assertTrue(result)

    def test_is_valid_example5(self):
        s = '(([{}]))'

        sol = Solution()
        result = sol.isValid(s)

        self.assertTrue(result)

    def test_is_valid_example6(self):
        s = '([]){}'

        sol = Solution()
        result = sol.isValid(s)

        self.assertTrue(result)

    def test_is_valid_example7(self):
        s = '(('

        sol = Solution()
        result = sol.isValid(s)

        self.assertFalse(result)

from unittest import TestCase

from leetcode75.array_string.gcd_of_strings_1071 import Solution


class TestSolution(TestCase):
    def test_gcd_of_strings_example1(self):
        str1 = "ABCABC"
        str2 = "ABC"

        sol = Solution()
        result = sol.gcdOfStrings(str1, str2)

        self.assertEqual("ABC", result)

    def test_gcd_of_strings_example2(self):
        str1 = "ABABAB"
        str2 = "ABAB"

        sol = Solution()
        result = sol.gcdOfStrings(str1, str2)

        self.assertEqual("AB", result)

    def test_gcd_of_strings_example3(self):
        str1 = "LEET"
        str2 = "CODE"

        sol = Solution()
        result = sol.gcdOfStrings(str1, str2)

        self.assertEqual("", result)

    def test_gcd_of_strings_example4(self):
        str1 = "ABCDEF"
        str2 = "ABC"

        sol = Solution()
        result = sol.gcdOfStrings(str1, str2)

        self.assertEqual("", result)

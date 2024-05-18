from unittest import TestCase

from leetcode75.stack.decode_string_394 import Solution


class TestSolution(TestCase):
    def test_decode_string_example1(self):
        s = "3[a]2[bc]"

        sol = Solution()
        result = sol.decodeString(s)

        self.assertEqual('aaabcbc', result)

    def test_decode_string_example2(self):
        s = '3[a2[c]]'

        sol = Solution()
        result = sol.decodeString(s)

        self.assertEqual('accaccacc', result)

    def test_decode_string_example3(self):
        s = "2[abc]3[cd]ef"

        sol = Solution()
        result = sol.decodeString(s)

        self.assertEqual('abcabccdcdcdef', result)

    def test_decode_string_example25(self):
        s = "100[leetcode]"

        sol = Solution()
        result = sol.decodeString(s)

        self.assertEqual('leetcode' * 100, result)

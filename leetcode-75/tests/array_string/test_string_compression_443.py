from unittest import TestCase

from leetcode75.array_string.string_compression_443 import Solution


class TestSolution(TestCase):
    def test_compress_example1(self):
        chars = ["a", "a", "b", "b", "c", "c", "c"]

        sol = Solution()
        result = sol.compress(chars)

        self.assertEqual(6, result)
        self.assertEqual(list("a2b2c3"), chars)

    def test_compress_example2(self):
        chars = ["a"]

        sol = Solution()
        result = sol.compress(chars)

        self.assertEqual(1, result)
        self.assertEqual(list("a"), chars)

    def test_compress_example3(self):
        chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]

        sol = Solution()
        result = sol.compress(chars)

        self.assertEqual(4, result)
        self.assertEqual(list("ab12"), chars)

    def test_compress_example4(self):
        chars = ["a", "a", "a", "b", "b", "a", "a"]

        sol = Solution()
        result = sol.compress(chars)

        self.assertEqual(6, result)
        self.assertEqual(list("a3b2a2"), chars)

    def test_compress_example5(self):
        chars = ["a", "a", "a", "a", "a", "a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b",
                 "b", "b", "b", "b", "b", "b", "b", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c",
                 "c"]

        sol = Solution()
        result = sol.compress(chars)

        self.assertEqual(8, result)
        self.assertEqual(["a", "6", "b", "2", "1", "c", "1", "4"], chars)

    def test_compress_example6(self):
        chars = ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"]

        sol = Solution()
        result = sol.compress(chars)

        self.assertEqual(3, result)
        self.assertEqual(list("o10"), chars)

    def test_compress_example7(self):
        chars = ["a"] * 100

        sol = Solution()
        result = sol.compress(chars)

        self.assertEqual(4, result)
        self.assertEqual(list("a100"), chars)

    def test_compress_example8(self):
        chars = ["b", "l", "l", "l", "l", "l", "l", "4", "4", "W", "W", "&", "d", "d", "d", "@", "D", "D", ".", ".",
                 ".", "8", "8", "8", "U", "V", ">", "J", "J", "k", "H", "H", "=", "l", "[", "[", "[", "[", "[", "[",
                 "[", "a", "a", "'", "<", "[", "[", "y", "V", "l", "l", "'", "$", "E", "`", "v", "k", "E", "E", "t",
                 "t", "t", "t", "t", "=", "=", "0", "C", "a", "l", "l", "l", "r", "R", "M", "M", "c", "c", "c", "A",
                 "A", "S", "9", "9", "9", "9", ")", ")", "\\", "s", "\\", "\\", "y", "W", "W", "W", "J", "J", "J", "J",
                 "6", "6", "<", "<", "E", "u", "e", "e", "e", "e", "e", "e", "e", "e", "e", "9", "9", "9", "9", "R",
                 "8", "?", "F", "3", "&", "&", "&", "&", "f", "%", "%", "2", "2", "2", ")", ")", ")", "J", "p", "|",
                 "D", "D", "D", "s", "t", "V", "V", "?", "^", "^", "S", "3", "3", "3", "3", "h", "*", "|", "|", "b",
                 "b", "a", "a", "a", "r", "r", "r", "r", "J", ".", "^", "^", "~", "g", ":", ":", ":", "(", "4", "4",
                 "4", "4", "w", "w", "w", "w", "w", "w", "w", "C", "?", "=", "d", "L", ":", "0", "0", "c", "w", "w",
                 "w", "w", "w", "w", "{", "{", "t", "k", "k", "k", "&", "&", "&", "h", "j", "j", "j", "0", "3", "l",
                 ";", ";", ";", ";", ";", ".", ".", ".", "%", "1", "1", "1", "l", "9", "?", "?", "?", "t", ">", "E",
                 "N", "N", "@", ">", ".", ".", "I", "a", "a", "a", "a", "B", "7", "7", "{", "o", "o", "-", "+", "+",
                 "+", "+", "o", "o", "}", "B", "B", "r", "r", "r", "q", "4", "4", "4", "9", "W", "W", "W", "W", "W",
                 "'", "'", "'", "g", "J", "(", "(", "(", "(", "t", "t", "?", ";", "g", "g", "g", "0", "]", "]", "]"]

        sol = Solution()
        sol.compress(chars)

        self.assertEqual(
            ["b", "l", "6", "4", "2", "W", "2", "&", "d", "3", "@", "D", "2", ".", "3", "8", "3", "U", "V", ">", "J",
             "2", "k", "H", "2", "=", "l", "[", "7", "a", "2", "'", "<", "[", "2", "y", "V", "l", "2", "'", "$", "E",
             "`", "v", "k", "E", "2", "t", "5", "=", "2", "0", "C", "a", "l", "3", "r", "R", "M", "2", "c", "3", "A",
             "2", "S", "9", "4", ")", "2", "\\", "s", "\\", "2", "y", "W", "3", "J", "4", "6", "2", "<", "2", "E", "u",
             "e", "9", "9", "4", "R", "8", "?", "F", "3", "&", "4", "f", "%", "2", "2", "3", ")", "3", "J", "p", "|",
             "D", "3", "s", "t", "V", "2", "?", "^", "2", "S", "3", "4", "h", "*", "|", "2", "b", "2", "a", "3", "r",
             "4", "J", ".", "^", "2", "~", "g", ":", "3", "(", "4", "4", "w", "7", "C", "?", "=", "d", "L", ":", "0",
             "2", "c", "w", "6", "{", "2", "t", "k", "3", "&", "3", "h", "j", "3", "0", "3", "l", ";", "5", ".", "3",
             "%", "1", "3", "l", "9", "?", "3", "t", ">", "E", "N", "2", "@", ">", ".", "2", "I", "a", "4", "B", "7",
             "2", "{", "o", "2", "-", "+", "4", "o", "2", "}", "B", "2", "r", "3", "q", "4", "3", "9", "W", "5", "'",
             "3", "g", "J", "(", "4", "t", "2", "?", ";", "g", "3", "0", "]", "3"], chars)

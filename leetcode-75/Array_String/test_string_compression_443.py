from unittest import TestCase

from string_compression_443 import Solution


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

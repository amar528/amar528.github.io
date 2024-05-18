from unittest import TestCase
from leetcode75.dp_nd.unique_paths_62 import Solution


class TestSolution(TestCase):
    def test_unique_paths_example1(self):
        m = 3
        n = 7

        sol = Solution()
        result = sol.uniquePaths(m, n)

        self.assertEqual(28, result)

    def test_unique_paths_example2(self):
        m = 3
        n = 2

        sol = Solution()
        result = sol.uniquePaths(m, n)

        self.assertEqual(3, result)

    def test_unique_paths_example3(self):
        m = 1
        n = 2

        sol = Solution()
        result = sol.uniquePaths(m, n)

        self.assertEqual(1, result)

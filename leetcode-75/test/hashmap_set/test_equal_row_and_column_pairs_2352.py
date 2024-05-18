from unittest import TestCase

from leetcode75.hashmap_set.equal_row_and_column_pairs_2352 import Solution


class TestSolution(TestCase):
    def test_equal_pairs_example1(self):
        grid = [[3, 2, 1],
                [1, 7, 6],
                [2, 7, 7]]

        sol = Solution()
        result = sol.equalPairs(grid)

        self.assertEqual(1, result)

    def test_equal_pairs_example2(self):
        grid = [[3, 1, 2, 2],
                [1, 4, 4, 5],
                [2, 4, 2, 2],
                [2, 4, 2, 2]]

        sol = Solution()
        result = sol.equalPairs(grid)

        self.assertEqual(3, result)

    def test_equal_pairs_example3(self):
        grid = [[11, 1],
                [1, 11]]

        sol = Solution()
        result = sol.equalPairs(grid)

        self.assertEqual(2, result)

    def test_equal_pairs_example4(self):
        grid = [[13, 13],
                [13, 13]]

        sol = Solution()
        result = sol.equalPairs(grid)

        self.assertEqual(4, result)

    def test_equal_pairs_example5(self):
        grid = [[3, 3, 3, 6, 18, 3, 3, 3, 3, 3],
                [3, 3, 3, 3, 1, 3, 3, 3, 3, 3],
                [3, 3, 3, 3, 1, 3, 3, 3, 3, 3],
                [3, 3, 3, 3, 1, 3, 3, 3, 3, 3],
                [1, 1, 1, 11, 19, 1, 1, 1, 1, 1],
                [3, 3, 3, 18, 19, 3, 3, 3, 3, 3],
                [3, 3, 3, 3, 1, 3, 3, 3, 3, 3],
                [3, 3, 3, 3, 1, 3, 3, 3, 3, 3],
                [3, 3, 3, 1, 6, 3, 3, 3, 3, 3],
                [3, 3, 3, 3, 1, 3, 3, 3, 3, 3]]

        sol = Solution()
        result = sol.equalPairs(grid)

        self.assertEqual(48, result)

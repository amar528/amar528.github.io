from unittest import TestCase
from leetcode75.graphs.bfs.rotting_oranges_994 import Solution


class TestSolution(TestCase):
    def test_oranges_rotting_example1(self):
        grid = [[2, 1, 1],
                [1, 1, 0],
                [0, 1, 1]]

        sol = Solution()
        result = sol.orangesRotting(grid)

        self.assertEqual(4, result)

    def test_oranges_rotting_example2(self):
        grid = [[2, 1, 1],
                [0, 1, 1],
                [1, 0, 1]]

        sol = Solution()
        result = sol.orangesRotting(grid)

        self.assertEqual(-1, result)

    def test_oranges_rotting_example3(self):
        grid = [[0, 2]]

        sol = Solution()
        result = sol.orangesRotting(grid)

        self.assertEqual(0, result)

    def test_oranges_rotting_example4(self):
        grid = [[2, 2],
                [1, 1],
                [0, 0],
                [2, 0]]

        sol = Solution()
        result = sol.orangesRotting(grid)

        self.assertEqual(1, result)

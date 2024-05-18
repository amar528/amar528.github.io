from unittest import TestCase

from leetcode75.graphs.dfs.number_of_provinces_547_unionfind import Solution


class TestSolution(TestCase):
    def test_find_circle_num_example1(self):
        provinces = [[1, 1, 0],
                     [1, 1, 0],
                     [0, 0, 1]]

        sol = Solution()
        result = sol.findCircleNum(provinces)

        self.assertEqual(2, result)

    def test_find_circle_num_example2(self):
        provinces = [[1, 0, 0],
                     [0, 1, 0],
                     [0, 0, 1]]

        sol = Solution()
        result = sol.findCircleNum(provinces)

        self.assertEqual(3, result)

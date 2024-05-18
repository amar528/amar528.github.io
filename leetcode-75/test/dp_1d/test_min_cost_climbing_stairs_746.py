from unittest import TestCase

from leetcode75.dp_1d.min_cost_climbing_stairs_746 import Solution


class TestSolution(TestCase):
    def test_min_cost_climbing_stairs_example1(self):
        cost = [10, 15, 20]

        sol = Solution()
        result = sol.minCostClimbingStairs(cost)

        self.assertEqual(15, result)

    def test_min_cost_climbing_stairs_example2(self):
        cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

        sol = Solution()
        result = sol.minCostClimbingStairs(cost)

        self.assertEqual(6, result)

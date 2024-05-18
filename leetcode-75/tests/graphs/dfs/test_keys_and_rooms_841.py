from unittest import TestCase

from leetcode75.graphs.dfs.keys_and_rooms_841 import Solution


class TestSolution(TestCase):
    def test_can_visit_all_rooms_example1(self):
        rooms = [[1], [2], [3], []]
        sol = Solution()

        result = sol.canVisitAllRooms(rooms)
        self.assertTrue(result)

    def test_can_visit_all_rooms_example2(self):
        rooms = [[1, 3], [3, 0, 1], [2], [0]]
        sol = Solution()

        result = sol.canVisitAllRooms(rooms)
        self.assertFalse(result)

    def test_can_visit_all_rooms_example3(self):
        rooms = [[2], [], [1]]
        sol = Solution()

        result = sol.canVisitAllRooms(rooms)
        self.assertTrue(result)

from unittest import TestCase
from link_list_cycle_141 import Solution
from list_node import *


class TestSolution(TestCase):
    def test_has_cycle_example1(self):
        head = to_list_node([3, 2, 0, -4])

        sol = Solution()
        result = sol.hasCycle(head)

        self.assertFalse(result)

    def test_has_cycle_example2(self):
        head = to_list_node(
            [-21, 10, 17, 8, 4, 26, 5, 35, 33, -7, -16, 27, -12, 6, 29, -12, 5, 9, 20, 14, 14, 2, 13, -24, 21, 23, -21,
             5])

        sol = Solution()
        result = sol.hasCycle(head)

        self.assertFalse(result)

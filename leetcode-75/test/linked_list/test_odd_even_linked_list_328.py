from unittest import TestCase

from leetcode75.linked_list.listnode import *
from leetcode75.linked_list.odd_even_linked_list_328 import Solution


class TestSolution(TestCase):
    def test_odd_even_list_example1(self):
        head = build_list([1, 2, 3, 4, 5])

        sol = Solution()
        result = sol.oddEvenList(head)

        self.assertIsNotNone(result)
        output = build_arr(result)
        self.assertListEqual([1, 3, 5, 2, 4], output)

    def test_odd_even_list_example2(self):
        head = build_list([2, 1, 3, 5, 6, 4, 7])

        sol = Solution()
        result = sol.oddEvenList(head)

        self.assertIsNotNone(result)
        output = build_arr(result)
        self.assertListEqual([2, 3, 6, 7, 1, 5, 4], output)

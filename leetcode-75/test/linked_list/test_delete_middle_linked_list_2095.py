from unittest import TestCase
from leetcode75.linked_list.delete_middle_linked_list_2095 import Solution
from leetcode75.linked_list.listnode import *


class TestSolution(TestCase):
    def test_delete_middle_example1(self):
        arr = [1, 3, 4, 7, 1, 2, 6]
        head = build_list(arr)

        sol = Solution()
        result = sol.deleteMiddle(head)

        expected = build_arr(result)
        self.assertListEqual(expected, [1, 3, 4, 1, 2, 6])

    def test_delete_middle_example2(self):
        arr = [2, 1]
        head = build_list(arr)

        sol = Solution()
        result = sol.deleteMiddle(head)

        expected = build_arr(result)
        self.assertListEqual(expected, [2])

    def test_delete_middle_example3(self):
        arr = [1, 2, 3, 4]
        head = build_list(arr)

        sol = Solution()
        result = sol.deleteMiddle(head)

        expected = build_arr(result)
        self.assertListEqual(expected, [1, 2, 4])

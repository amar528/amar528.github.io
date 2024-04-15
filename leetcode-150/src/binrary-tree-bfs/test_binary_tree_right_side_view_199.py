from unittest import TestCase

from binary_tree import *
from binary_tree_right_side_view_199 import Solution


class TestSolution(TestCase):
    def test_right_side_view_example1(self):
        nodes = [1, 2, 3, None, 5, None, 4]
        root = build_tree(nodes)

        sol = Solution()
        result = sol.rightSideView(root)

        self.assertListEqual([1, 3, 4], result)

    def test_right_side_view_example2(self):
        nodes = [1, 2]
        root = build_tree(nodes)

        sol = Solution()
        result = sol.rightSideView(root)

        self.assertListEqual([1, 2], result)

    def test_right_side_view_example3(self):
        nodes = [1, 2, 3, 4]
        root = build_tree(nodes)

        sol = Solution()
        result = sol.rightSideView(root)

        self.assertListEqual([1, 3, 4], result)

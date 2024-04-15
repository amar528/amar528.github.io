from unittest import TestCase

from binary_tree import *
from mini_abs_diff_530 import Solution


class TestSolution(TestCase):
    def test_get_minimum_difference_example1(self):
        root = build_tree([4, 2, 6, 1, 3])

        sol = Solution()
        result = sol.getMinimumDifference(root)

        self.assertEqual(1, result)

    def test_get_minimum_difference_example2(self):
        root = build_tree([1, 0, 48, None, None, 12, 49])

        sol = Solution()
        result = sol.getMinimumDifference(root)

        self.assertEqual(1, result)

    def test_get_minimum_difference_example3(self):
        # root = build_tree([1, None, 3, 2])
        # self.assertIsNone(root.left)
        # self.assertIsNotNone(root.right)
        # self.assertEqual(3, root.right.val)
        # self.assertIsNotNone(root.right.left)
        # self.assertEqual(2, root.right.left)

        two = TreeNode(2)
        three = TreeNode(3, None, two)
        root = TreeNode(1, None, three)

        sol = Solution()
        result = sol.getMinimumDifference(root)

        self.assertEqual(1, result)

    def test_get_minimum_difference_example4(self):
        root = build_tree([236, 104, 701, None, 227, None, 911])

        sol = Solution()
        result = sol.getMinimumDifference(root)

        self.assertEqual(9, result)

from unittest import TestCase
from leetcode75.binary_tree.treenode import TreeNode
from leetcode75.bst.search_in_a_bst_700 import Solution


class TestSolution(TestCase):
    def test_search_bst_example1(self):
        root = TreeNode(4,
                        TreeNode(2,
                                 TreeNode(1), TreeNode(3)),
                        TreeNode(7))

        sol = Solution()
        result = sol.searchBST(root, 2)

        self.assertIsNotNone(result)
        self.assertEqual(2, result.val)

        self.assertIsNotNone(result.left)
        self.assertEqual(1, result.left.val)
        self.assertIsNotNone(result.right)
        self.assertEqual(3, result.right.val)

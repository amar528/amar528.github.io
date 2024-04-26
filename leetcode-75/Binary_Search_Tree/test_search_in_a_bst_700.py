from unittest import TestCase
from treenode import TreeNode
from search_in_a_bst_700 import Solution


class TestSolution(TestCase):
    def test_search_bst_example1(self):
        root = TreeNode(4,
                        TreeNode(2,
                                 TreeNode(1), TreeNode(3)),
                        TreeNode(7))

        sol = Solution()
        result = sol.searchBST(root, 2)

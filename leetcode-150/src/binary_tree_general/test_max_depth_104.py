from unittest import TestCase

from binary_tree_general.max_depth_104 import Solution, TreeNode


class TestSolution(TestCase):

    def test_max_depth_example1(self):
        # nodes = [3, 9, 20, None, None, 15, 7]

        fifteen = TreeNode(15)
        seven = TreeNode(7)
        nine = TreeNode(9)
        twenty = TreeNode(20, fifteen, seven)
        root = TreeNode(3, nine, twenty)

        sol = Solution()
        result = sol.maxDepth(root)

        self.assertEquals(3, result)

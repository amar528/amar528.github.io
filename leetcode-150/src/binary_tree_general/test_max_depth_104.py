from unittest import TestCase

from binary_tree_general.max_depth_104 import Solution, TreeNode


class TestSolution(TestCase):

    def build_tree(self, nodes):
        prev = None
        for num in nodes:
            if num:
                node = TreeNode(num)

    def test_max_depth_example1(self):
        nodes = [3, 9, 20, None, None, 15, 7]

        sol = Solution()
        result = sol.maxDepth(nodes)

        self.assertEquals(3, result)

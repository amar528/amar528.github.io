from unittest import TestCase

from leetcode75.binary_tree.dfs.path_sum_3_437 import Solution
from leetcode75.binary_tree.treenode import TreeNode


class TestSolution(TestCase):
    def test_dfs_example1(self):
        root = TreeNode(10,
                        TreeNode(5,
                                 TreeNode(3,
                                          TreeNode(3),
                                          TreeNode(-2)),
                                 TreeNode(2,
                                          None,
                                          TreeNode(1))),
                        TreeNode(-3,
                                 None,
                                 TreeNode(11)))

        sol = Solution()
        result = sol.pathSum(root, 8)

        self.assertEqual(3, result)

    def test_dfs_example51(self):
        root = TreeNode(5,
                        TreeNode(4,
                                 TreeNode(11,
                                          TreeNode(7),
                                          TreeNode(2)),
                                 None),
                        TreeNode(8,
                                 TreeNode(13),
                                 TreeNode(4,
                                          TreeNode(5),
                                          TreeNode(1))
                                 )
                        )

        sol = Solution()
        result = sol.pathSum(root, 22)

        self.assertEqual(3, result)

    def test_dfs_example100(self):
        root = TreeNode(1)

        sol = Solution()
        result = sol.pathSum(root, 1)

        self.assertEqual(1, result)

    def test_dfs_example103(self):
        root = TreeNode(1,
                        TreeNode(-2),
                        TreeNode(-3)
                        )

        sol = Solution()
        result = sol.pathSum(root, -1)

        self.assertEqual(1, result)

    def test_dfs_example104(self):
        root = TreeNode(1,
                        TreeNode(2)
                        )

        sol = Solution()
        result = sol.pathSum(root, 1)

        self.assertEqual(1, result)

    def test_dfs_example110(self):
        root = TreeNode(0,
                        TreeNode(1),
                        TreeNode(1)
                        )

        sol = Solution()
        result = sol.pathSum(root, 1)

        self.assertEqual(4, result)

    def test_dfs_example114(self):
        root = TreeNode(1,
                        TreeNode(0,
                                 TreeNode(1,
                                          TreeNode(0),
                                          TreeNode(1)),
                                 TreeNode(2,
                                          TreeNode(-1),
                                          TreeNode(0))),
                        TreeNode(1,
                                 TreeNode(0,
                                          TreeNode(-1),
                                          TreeNode(0)),
                                 TreeNode(-1,
                                          TreeNode(1),
                                          TreeNode(0)))
                        )

        sol = Solution()
        result = sol.pathSum(root, 2)

        self.assertEqual(13, result)

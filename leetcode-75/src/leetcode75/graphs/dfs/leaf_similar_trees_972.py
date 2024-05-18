from typing import Optional

from Binary_Tree.treenode import TreeNode


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def dfs(current):
            if not current:
                return []

            if not current.left and not current.right:
                return [current.val]

            left = []
            if current.left:
                left = dfs(current.left)

            right = []
            if current.right:
                right = dfs(current.right)

            return left + right

        root1_nodes = dfs(root1)
        root2_nodes = dfs(root2)

        return root1_nodes == root2_nodes
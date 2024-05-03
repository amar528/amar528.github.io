from Binary_Tree.treenode import TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return 0

        def dfs(current, max_in_path):

            if not current:
                return 0

            this_value = 0
            if max_in_path <= current.val:
                this_value = 1

            max_in_path = max(max_in_path, current.val)

            return this_value + dfs(current.left, max_in_path) + dfs(current.right, max_in_path)

        return dfs(root, root.val)

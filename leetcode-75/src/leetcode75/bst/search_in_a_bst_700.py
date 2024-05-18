from typing import Optional

from treenode import TreeNode


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # base case of None
        if not root:
            return None

        # base case that we found the value
        # Pre order traversal
        if root.val == val:
            return root

        # recurse left for lesser value, right for greater value
        if val < root.val and root.left:
            return self.searchBST(root.left, val)
        elif val > root.val and root.right:
            return self.searchBST(root.right, val)

import sys
from typing import Optional

from binary_tree import TreeNode


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        found_min_diff = 0

        def dfs(node: Optional[TreeNode]) -> tuple:

            if not node:
                return ([], None)

            all_vals = [node.val]

            min_so_far = sys.maxsize

            if node.left:
                left_vals, left_min = dfs(node.left)
                all_vals += left_vals
                min_so_far = min(min_so_far, left_min)

            if node.right:
                right_vals, right_min = dfs(node.right)
                all_vals += right_vals
                min_so_far = min(min_so_far, right_min)

            for v in all_vals:
                diff = abs(node.val - v)
                if 0 < diff < min_so_far:
                    min_so_far = diff

            return (all_vals, min_so_far)

        result_tuple = dfs(root)
        return result_tuple[1]

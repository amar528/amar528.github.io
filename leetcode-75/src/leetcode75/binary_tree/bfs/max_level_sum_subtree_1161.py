import collections
from typing import Optional
from Binary_Tree.treenode import TreeNode


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        queue = collections.deque([(1, root)])
        level_sums = collections.defaultdict(int)

        while queue:
            level, node = queue.popleft()

            level_sums[level] += node.val

            if node.left:
                queue.append((level + 1, node.left))

            if node.right:
                queue.append((level + 1, node.right))

        return max(level_sums, key=level_sums.get)

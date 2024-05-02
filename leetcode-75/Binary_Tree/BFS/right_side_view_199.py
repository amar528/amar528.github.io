import collections
from typing import Optional, List

from Binary_Tree.treenode import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        result = []
        q = collections.deque([root])

        while q:

            right_most = None

            # process all nodes at this level
            for _ in range(len(q)):
                current = q.popleft()

                if current:
                    right_most = current
                    q.append(current.left)
                    q.append(current.right)

            if right_most:
                result.append(right_most.val)

        return result

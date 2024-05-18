import collections
from typing import Optional

from treenode import TreeNode


class Solution:

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # sum -> frequency
        sums = collections.defaultdict(int)
        sums[0] = 1

        def dfs(node, total):
            if not node:
                return 0

            # add this node to the total
            total += node.val

            # get the count from the sums cache
            # this is the prefix sum
            prefix_sum = total - targetSum
            count = sums[prefix_sum]

            # update the frequency of this sum
            sums[total] += 1
            count += dfs(node.left, total) + dfs(node.right, total)
            # remove it as this branch has completed
            sums[total] -= 1

            return count

        # call dfs on the root node
        return dfs(root, 0)

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'TreeNode(val: {self.val})'


def val_or_none(val):
    if val or val == 0: return TreeNode(val)
    return None


def build_tree(nums: List[int]) -> Optional[TreeNode]:
    n = len(nums)

    if n == 0:
        return None

    root = TreeNode(nums[0])

    nodes = [root]
    parent = None

    for i in range(n):

        if nodes[i]:
            parent = nodes[i]

        if parent:

            left_idx = i + i + 1
            right_idx = i + i + 2

            if left_idx < n:
                left = val_or_none(nums[left_idx])
                nodes.append(left)
                parent.left = left

            if right_idx < n:
                right = val_or_none(nums[right_idx])
                nodes.append(right)
                parent.right = right

    return root

# [1, 2, 3, None, 5, None, 4]
#           1
#          /  \
#         2     3
#        / \   /  \
#       x   5 x    4

# [1, 2]
#           1
#          /
#         2

# [1, 2, 3, 4]
#           1
#          / \
#         2   3
#        /
#       4

# [4, 2, 6, 1, 3]
#        4
#       / \
#      2   6
#     / \
#    1   3

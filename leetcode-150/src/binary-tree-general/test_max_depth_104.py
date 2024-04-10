from unittest import TestCase

from max_depth_104 import Solution
from binary_tree import *


class TestSolution(TestCase):

    def test_max_depth_example1(self):
        root = build_tree([3, 9, 20, None, None, 15, 7])

        sol = Solution()
        result = sol.maxDepth(root)

        self.assertEqual(3, result)

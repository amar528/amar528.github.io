from unittest import TestCase

from binary_tree_right_side_view_199 import Solution, TreeNode


class TestSolution(TestCase):
    def test_right_side_view_example1(self):
        # nodes = [1,2,3,null,5,null,4]

        four = TreeNode(4)
        five = TreeNode(5)
        two = TreeNode(2, None, five)
        three = TreeNode(3, None, four)
        root = TreeNode(1, two, three)

        sol = Solution()
        result = sol.rightSideView(root)

        self.assertListEqual([1, 3, 4], result)

    def test_right_side_view_example2(self):
        # nodes = [1,2]

        two = TreeNode(2)
        root = TreeNode(1, two, None)

        sol = Solution()
        result = sol.rightSideView(root)

        self.assertListEqual([1, 2], result)

    def test_right_side_view_example3(self):
        # nodes = [1,2,3,4]

        four = TreeNode(4)
        two = TreeNode(2, four, None)
        three = TreeNode(3)
        root = TreeNode(1, two, three)

        sol = Solution()
        result = sol.rightSideView(root)

        self.assertListEqual([1, 3, 4], result)

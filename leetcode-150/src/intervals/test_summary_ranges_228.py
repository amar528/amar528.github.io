from unittest import TestCase

from summary_ranges_228 import Solution


class TestSolution(TestCase):
    def test_summary_ranges_example1(self):
        nums = [0, 1, 2, 4, 5, 7]

        sol = Solution()
        result = sol.summaryRanges(nums)

        self.assertListEqual(["0->2", "4->5", "7"], result)

    def test_summary_ranges_example2(self):
        nums = [0, 2, 3, 4, 6, 8, 9]

        sol = Solution()
        result = sol.summaryRanges(nums)

        self.assertListEqual(["0", "2->4", "6", "8->9"], result)



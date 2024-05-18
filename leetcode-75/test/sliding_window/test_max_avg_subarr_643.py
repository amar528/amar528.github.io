from unittest import TestCase

from leetcode75.sliding_window.max_avg_subarr_643 import Solution


class TestSolution(TestCase):
    def test_find_max_average_example1(self):
        nums = [1, 12, -5, -6, 50, 3]
        k = 4

        sol = Solution()
        result = sol.findMaxAverage(nums, k)

        self.assertEqual(12.75000, result)

    def test_find_max_average_example2(self):
        nums = [5]
        k = 1

        sol = Solution()
        result = sol.findMaxAverage(nums, k)

        self.assertEqual(5.00000, result)

    def test_find_max_average_example103(self):
        nums = [0, 1, 1, 3, 3]
        k = 4

        sol = Solution()
        result = sol.findMaxAverage(nums, k)

        self.assertEqual(2.00000, result)

    def test_find_max_average_example117(self):
        nums = [8860, -853, 6534, 4477, -4589, 8646, -6155, -5577, -1656, -5779, -2619, -8604, -1358, -8009, 4983, 7063,
                3104,
                -1560, 4080, 2763, 5616, -2375, 2848, 1394, -7173, -5225, -8244, -809, 8025, -4072, -4391, -9579, 1407,
                6700, 2421,
                -6685, 5481, -1732, -8892, -6645, 3077, 3287, -4149, 8701, -4393, -9070, -1777, 2237, -3253, -506,
                -4931, -7366,
                -8132, 5406, -6300, -275, -1908, 67, 3569, 1433, -7262, -437, 8303, 4498, -379, 3054, -6285, 4203, 6908,
                4433,
                3077, 2288, 9733, -8067, 3007, 9725, 9669, 1362, -2561, -4225, 5442, -9006, -429, 160, -9234, -4444,
                3586, -5711,
                -9506, -79, -4418, -4348, -5891]
        k = 93

        sol = Solution()
        result = sol.findMaxAverage(nums, k)

        self.assertEqual(-594.58065, result)

    def test_find_max_average_example22(self):
        nums = [0, 4, 0, 3, 2]
        k = 1

        sol = Solution()
        result = sol.findMaxAverage(nums, k)

        self.assertEqual(4.00000, result)

    def test_find_max_average_example25(self):
        nums = [4, 2, 1, 3, 3]
        k = 2

        sol = Solution()
        result = sol.findMaxAverage(nums, k)

        self.assertEqual(3.00000, result)

    def test_find_max_average_example26(self):
        nums = [7, 4, 5, 8, 8, 3, 9, 8, 7, 6]
        k = 7

        sol = Solution()
        result = sol.findMaxAverage(nums, k)

        self.assertEqual(7.00000, result)

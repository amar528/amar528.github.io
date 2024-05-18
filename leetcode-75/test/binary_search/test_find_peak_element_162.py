from unittest import TestCase

from leetcode75.binary_search.find_peak_element_162 import Solution


class TestSolution(TestCase):
    def test_find_peak_element_example1(self):
        nums = [1, 2, 3, 1]

        sol = Solution()
        result = sol.findPeakElement(nums)

        self.assertEqual(2, result)

    def test_find_peak_element_example2(self):
        nums = [1, 2, 1, 3, 5, 6, 4]

        sol = Solution()
        result = sol.findPeakElement(nums)

        self.assertEqual(5, result)

    def test_find_peak_element_example3(self):
        nums = [1]

        sol = Solution()
        result = sol.findPeakElement(nums)

        self.assertEqual(0, result)

    def test_find_peak_element_example4(self):
        nums = [1, 2]

        sol = Solution()
        result = sol.findPeakElement(nums)

        self.assertEqual(1, result)

    def test_find_peak_element_example5(self):
        nums = [1, 2, 0]

        sol = Solution()
        result = sol.findPeakElement(nums)

        self.assertEqual(1, result)

    def test_find_peak_element_example6(self):
        nums = [2, 1]

        sol = Solution()
        result = sol.findPeakElement(nums)

        self.assertEqual(0, result)

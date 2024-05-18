from unittest import TestCase

from leetcode75.hashmap_set.unique_number_occurrences_1207 import Solution


class TestSolution(TestCase):
    def test_unique_occurrences_example1(self):
        arr = [1, 2, 2, 1, 1, 3]

        sol = Solution()
        result = sol.uniqueOccurrences(arr)

        self.assertTrue(result)

    def test_unique_occurrences_example2(self):
        arr = [1, 2]

        sol = Solution()
        result = sol.uniqueOccurrences(arr)

        self.assertFalse(result)

    def test_unique_occurrences_example3(self):
        arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]

        sol = Solution()
        result = sol.uniqueOccurrences(arr)

        self.assertTrue(result)

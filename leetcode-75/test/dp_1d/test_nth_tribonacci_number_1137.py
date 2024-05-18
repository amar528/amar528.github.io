from unittest import TestCase
from leetcode75.dp_1d.nth_tribonacci_number_1137 import Solution


class TestSolution(TestCase):
    def test_tribonacci_example1(self):
        n = 4

        sol = Solution()
        result = sol.tribonacci(n)

        self.assertEqual(4, result)

    def test_tribonacci_example2(self):
        n = 25

        sol = Solution()
        result = sol.tribonacci(n)

        self.assertEqual(1389537, result)

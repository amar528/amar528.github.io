from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []

        for i in candies:
            value_to_test = extraCandies + i
            is_greater = self.test_value(value_to_test, candies)
            result.append(is_greater)

        return result

    def test_value(self, value, others):
        for i in others:
            if value < i:
                return False
        return True


sol = Solution()
print(sol.kidsWithCandies([2, 3, 5, 1, 3], 3))

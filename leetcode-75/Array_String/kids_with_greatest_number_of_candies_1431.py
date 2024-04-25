from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extra_candies: int) -> List[bool]:

        greatest = max(candies)
        result = [False] * len(candies)

        for i, kid in enumerate(candies):
            if kid + extra_candies >= greatest:
                result[i] = True

        return result

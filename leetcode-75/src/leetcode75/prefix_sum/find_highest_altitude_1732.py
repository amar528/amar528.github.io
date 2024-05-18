import sys
from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxi = 0

        pre_sum = 0
        for point in gain:
            pre_sum += point
            maxi = max(maxi, pre_sum)

        return maxi
import sys
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        n = len(nums)

        no_result = n + 1
        min_length = no_result
        total = 0
        left_idx = 0

        for i in range(n):
            total += nums[i]

            while total >= target:
                min_length = min(min_length, i + 1 - left_idx)

                total -= nums[left_idx]
                left_idx += 1

        return min_length if min_length != no_result else 0

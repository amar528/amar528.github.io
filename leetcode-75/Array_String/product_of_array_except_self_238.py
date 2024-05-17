from functools import reduce
from operator import mul
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        result = [0] * n

        # calculate prefix sum for each i (product of nums to left)
        for i in range(n):
            left_sub = nums[0:i]
            result[i] = reduce(mul, left_sub) if left_sub else 1

        # add to result: calculate postfix for each i (product of nums to right - iterate in reverse)
        for i in reversed(range(n)):
            right_sub = nums[i + 1:] if i < n - 1 else []
            result[i] *= reduce(mul, right_sub) if right_sub else 1

        return result

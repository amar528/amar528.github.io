import sys
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        presum = 0
        total = sum(nums)

        for i in range(len(nums)):
            postsum = total - presum - nums[i]

            if presum == postsum:
                return i

            presum += nums[i]

        return -1

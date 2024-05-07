from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        # cumulative xor testing all numbers
        # the odd one out will remain
        xor = 0
        for val in nums:
            xor ^= val

        return xor

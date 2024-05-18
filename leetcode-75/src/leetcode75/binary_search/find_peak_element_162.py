import sys
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        n = len(nums)

        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2

            if mid > 0 and nums[mid] < nums[mid - 1]:
                # go to left side
                right = mid - 1
            elif mid < n - 1 and nums[mid] < nums[mid + 1]:
                # go to right
                left = mid + 1
            else:
                return mid

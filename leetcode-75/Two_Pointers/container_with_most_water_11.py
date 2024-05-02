from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        n = len(height)

        if n == 2:
            if 0 in height:
                return 0
            else:
                return 1

        # the maximum volume found so far
        max_vol_found = 0

        # left and right points
        left = 0
        right = n - 1

        while left < right:
            distance = right - left

            left_height = height[left]
            right_height = height[right]

            # calculate volume with the minimum height of left and right
            vol = distance * min(left_height, right_height)

            # update the max found so far if it is greater
            max_vol_found = max(max_vol_found, vol)

            # we only move the pointer which has the smallest height
            if left_height < right_height:
                left += 1
            else:
                right -= 1

        return max_vol_found

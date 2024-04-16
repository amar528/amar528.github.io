from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        n = len(height)

        if n == 2:
            if 0 in height:
                return 0
            else:
                return 1

        max_vol_found = 0

        left = 0
        right = n - 1

        while left < right:
            distance = right - left

            left_height = height[left]
            right_height = height[right]

            vol = distance * min(left_height, right_height)
            max_vol_found = max(max_vol_found, vol)

            if left_height < right_height:
                left += 1
            else:
                right -= 1

        return max_vol_found
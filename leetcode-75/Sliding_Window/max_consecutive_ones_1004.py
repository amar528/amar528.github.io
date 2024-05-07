from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        left = longest_so_far = 0

        for right, val in enumerate(nums):

            # take k if needed
            k -= (1 - val)  # - (1-1 == 0) will have no effect if val is 1

            # if k has run out, we need to take it from the left pointer value
            # and increment the left pointer
            if k < 0:
                k += 1 - nums[left]
                left += 1

            # calculate the maximum so far
            longest_so_far = max(longest_so_far, (right - left) + 1)

        return longest_so_far

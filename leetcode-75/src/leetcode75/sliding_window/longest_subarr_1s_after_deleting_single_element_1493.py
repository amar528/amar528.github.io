from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = 0

        # keep track of the number of zeros, allowing max 1
        zero_count = 0

        # result so far is the longest sub array length
        result = 0

        while right < n:

            # add 1 to the zero count if the right index points to a 0
            zero_count += 1 if nums[right] == 0 else 0

            # move the left pointer until we only have 1 zero
            while zero_count > 1:
                zero_count -= 1 if nums[left] == 0 else 0
                left += 1

            # update the maximum sub array length so far
            result = max(result, right - left)

            right += 1

        return result

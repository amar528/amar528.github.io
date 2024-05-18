from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        # keep track of the last non-zero index found in the array
        last_non_zero_idx = 0

        for i, value in enumerate(nums):

            # When a non-zero element is found
            if value != 0:
                # Swap the i non-zero element with the element at last_non_zero_idx index
                nums[last_non_zero_idx], nums[i] = nums[i], nums[last_non_zero_idx]

                # Move the last_non_zero_idx index forward
                last_non_zero_idx += 1

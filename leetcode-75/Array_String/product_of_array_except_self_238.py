from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        result = [0] * n

        prefix_product = 1
        for i in range(n):
            prefix_product *= nums[i - 1] if i > 0 else 1
            result[i] = prefix_product

        postfix_product = 1
        for i in reversed(range(n - 1)):
            postfix_product *= nums[i + 1] if i < n else 1
            result[i] *= postfix_product

        return result

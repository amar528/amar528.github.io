from math import inf


class Solution:
    def increasingTriplet(self, nums):
        first = second = inf
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False


sol = Solution()

print(sol.increasingTriplet([1, 2, 3, 4, 5]))
print(sol.increasingTriplet([5, 4, 3, 2, 1]))
print(sol.increasingTriplet([2, 1, 5, 0, 4, 6]))
print(sol.increasingTriplet([20, 100, 10, 12, 5, 13]))
print(sol.increasingTriplet([6, 7, 1, 2]))
print(sol.increasingTriplet([0, 4, 2, 1, 0, -1, -3]))  # false
print(sol.increasingTriplet([1, 2, 1, 3]))  # true

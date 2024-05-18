from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        if not cost:
            return 0

        n = len(cost)

        if n == 1:
            return cost[0]

        dp = [1] * (n + 2)

        # top stair cost is 0
        dp[n] = 0
        dp[n + 1] = 0  # also set this to avoid out of bounds when i = n - 1 initially

        # bottom up, going backwards down the staircase from the last stair

        i = n - 1
        while i >= 0:
            # cost of reaching this step is the cost of this step at i,
            # PLUS the minimum of the 2 steps above it
            # which has been calculated previously
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])

            i -= 1

        return min(dp[0], dp[1])

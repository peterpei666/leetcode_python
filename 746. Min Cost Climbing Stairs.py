from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [10 ** 9] * n
        dp[0] = 0
        dp[1] = 0
        for i in range(n - 2):
            dp[i + 1] = min(dp[i + 1], dp[i] + cost[i])
            dp[i + 2] = min(dp[i + 2], dp[i] + cost[i])
        dp[n - 1] = min(dp[n - 1], dp[n - 2] + cost[n - 2])
        return min(dp[n - 1] + cost[n - 1], dp[n - 2] + cost[n - 2])

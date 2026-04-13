from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 3 for _ in range(2)]
        dp[0] = [0, -prices[0], - 10 ** 9]
        for i in range(1, n):
            mask = i & 1
            prev = mask ^ 1
            dp[mask][0] = max(dp[prev][0], dp[prev][2])
            dp[mask][1] = max(dp[prev][0] - prices[i], dp[prev][1])
            dp[mask][2] = dp[prev][1] + prices[i]
        return max(dp[(n - 1) & 1][0], dp[(n - 1) & 1][2])

from typing import List

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m = len(coins)
        n = len(coins[0])
        dp = [[[int(-10 ** 9)] * 3 for _ in range(n)] for _ in range(2)]
        dp[0][0][1] = 0
        dp[0][0][2] = 0
        dp[0][0][0] = coins[0][0]
        for i in range(m):
            if i:
                dp[i & 1] = [[int(-10 ** 9)] * 3 for _ in range(n)]
            for j in range(n):
                for k in range(3):
                    if i:
                        dp[i & 1][j][k] = max(dp[i & 1][j][k], dp[(i - 1) & 1][j][k] + coins[i][j])
                    if i and k:
                        dp[i & 1][j][k] = max(dp[i & 1][j][k], dp[(i - 1) & 1][j][k - 1])
                    if j:
                        dp[i & 1][j][k] = max(dp[i & 1][j][k], dp[i & 1][j - 1][k] + coins[i][j])
                    if j and k:
                        dp[i & 1][j][k] = max(dp[i & 1][j][k], dp[i & 1][j - 1][k - 1])
        return max(dp[(m - 1) & 1][-1])

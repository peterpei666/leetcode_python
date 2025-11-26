from typing import List

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        mod = 10**9 + 7
        dp = [[[0] * k for _ in range(n)] for __ in range(m)]
        dp[0][0][grid[0][0] % k] = 1
        for j in range(1, n):
            val = grid[0][j] % k
            for t in range(k):
                dp[0][j][(t + val) % k] = (dp[0][j][(t + val) % k] + dp[0][j - 1][t]) % mod
        for i in range(1, m):
            val = grid[i][0] % k
            for t in range(k):
                dp[i][0][(t + val) % k] = (dp[i][0][(t + val) % k] + dp[i - 1][0][t]) % mod
        for i in range(1, m):
            for j in range(1, n):
                val = grid[i][j] % k
                for t in range(k):
                    dp[i][j][(t + val) % k] = (dp[i][j][(t + val) % k] + dp[i - 1][j][t]) % mod
                for t in range(k):
                    dp[i][j][(t + val) % k] = (dp[i][j][(t + val) % k] + dp[i][j - 1][t]) % mod
        return dp[m - 1][n - 1][0] % mod

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [[0] * (k + 1) for _ in range(2)]
        dp[0][0] = 1
        dp[1][0] = 1
        mod = 10 ** 9 + 7
        for i in range(1, n + 1):
            dp[i & 1][0] = dp[(i - 1) & 1][0]
            for j in range(1, min(k + 1, i)):
                dp[i & 1][j] = (dp[i & 1][j - 1] + dp[(i - 1) & 1][j]) % mod
            for j in range(i, k + 1):
                dp[i & 1][j] = (dp[i & 1][j - 1] + dp[(i - 1) & 1][j] - dp[(i - 1) & 1][j - i] + mod) % mod
        return dp[n & 1][k]

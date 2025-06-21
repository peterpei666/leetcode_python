class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        dp = [[1] * n for _ in range(2)]
        mod = 10 ** 9 + 7
        for i in range(1, k + 1):
            dp[i % 2][0] = dp[(i - 1) % 2][0]
            for j in range(1, n):
                dp[i % 2][j] = (dp[i % 2][j - 1] + dp[(i - 1) % 2][j]) % mod
        return dp[k % 2][n - 1]

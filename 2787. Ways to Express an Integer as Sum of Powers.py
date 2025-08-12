class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[0] * (n + 1) for _ in range(2)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            temp = pow(i, x)
            if temp > n:
                return dp[(i - 1) % 2][n]
            dp[i % 2] = dp[(i - 1) % 2][:]
            for j in range(temp, n + 1):
                dp[i % 2][j] = (dp[i % 2][j] + dp[(i - 1) % 2][j - temp]) % mod
        return dp[n % 2][n]

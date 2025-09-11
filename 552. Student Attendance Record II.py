class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[[0] * 3 for _ in range(2)] for _ in range(2)]
        dp[0][0][0] = 1
        dp[0][0][1] = 1
        dp[0][1][0] = 1
        for i in range(1, n):
            dp[i % 2][0][0] = (dp[(i - 1) % 2][0][0] + dp[(i - 1) % 2][0][1] % mod + dp[(i - 1) % 2][0][2]) % mod
            dp[i % 2][0][1] = dp[(i - 1) % 2][0][0]
            dp[i % 2][0][2] = dp[(i - 1) % 2][0][1]
            dp[i % 2][1][0] = (dp[(i - 1) % 2][0][0] + dp[(i - 1) % 2][0][1] + dp[(i - 1) % 2][0][2] + dp[(i - 1) % 2][1][0] + dp[(i - 1) % 2][1][1] + dp[(i - 1) % 2][1][2]) % mod
            dp[i % 2][1][1] = dp[(i - 1) % 2][1][0]
            dp[i % 2][1][2] = dp[(i - 1) % 2][1][1]
        ans = 0
        for i in range(3):
            ans += dp[(n - 1) % 2][0][i] + dp[(n - 1) % 2][1][i]
        return ans % mod

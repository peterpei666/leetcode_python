class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        for i in range(1, min(zero, limit) + 1):
            dp[i][0][0] = 1
        for i in range(1, min(one, limit) + 1):
            dp[0][i][1] = 1
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                val0 = dp[i - 1][j][0] + dp[i - 1][j][1]
                val1 = dp[i][j - 1][0] + dp[i][j - 1][1]
                if i > limit:
                    val0 -= dp[i - limit - 1][j][1]
                if j > limit:
                    val1 -= dp[i][j - limit - 1][0]
                dp[i][j][0] = (val0 + mod) % mod
                dp[i][j][1] = (val1 + mod) % mod
        return sum(dp[zero][one]) % mod

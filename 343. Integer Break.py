class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0, 1, 1] + [0] * 57
        for i in range(3, n + 1):
            t = 1
            for j in range(1, i):
                t = max(t, max(j, dp[j]) * max(i - j, dp[i - j]))
            dp[i] = t
        return dp[n]

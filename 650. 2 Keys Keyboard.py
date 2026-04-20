class Solution:
    def minSteps(self, n: int) -> int:
        dp = list(range(n + 1))
        dp[1] = 0
        for i in range(2, n):
            j = 2 * i
            while j <= n:
                dp[j] = min(dp[j], dp[i] + j // i)
                j += i
        return dp[n]

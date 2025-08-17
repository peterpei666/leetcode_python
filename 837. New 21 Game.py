class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        temp = 1.0 if k else 0.0
        for i in range(1, n + 1):
            dp[i] = temp / maxPts
            if i < k:
                temp += dp[i]
            if i >= maxPts and i - maxPts < k:
                temp -= dp[i - maxPts]
        return sum(dp[k:])

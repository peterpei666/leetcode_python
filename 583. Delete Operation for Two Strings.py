class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        m, n = len(w1), len(w2)
        dp = [[0] * (n + 1) for _ in range(2)]
        for i in range(1, m + 1):
            mask = i & 1
            prev = mask ^ 1
            for j in range(1, n + 1):
                if w1[i - 1] == w2[j - 1]:
                    dp[mask][j] = dp[prev][j - 1] + 1
                else:
                    dp[mask][j] = max(dp[mask][j - 1], dp[prev][j])
        return m + n - 2 * dp[m & 1][n]

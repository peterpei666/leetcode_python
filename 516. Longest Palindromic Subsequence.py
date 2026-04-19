class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(2)]
        rev = s[::-1]
        for i in range(1, n + 1):
            mask = i & 1
            prev = mask ^ 1
            dp[mask] = [0] * (n + 1)
            for j in range(1, n + 1):
                if s[i - 1] == rev[j - 1]:
                    dp[mask][j] = 1 + dp[prev][j - 1]
                else:
                    dp[mask][j] = max(dp[prev][j], dp[mask][j - 1])
        return dp[n & 1][n]

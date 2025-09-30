class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        mod = 10 ** 9 + 7
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                if not s[i] == s[j]:
                    dp[i][j] = (dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1] + mod) % mod
                else:
                    low, high = i + 1, j - 1
                    while low <= high and not s[low] == s[i]:
                        low += 1
                    while high >= low and not s[high] == s[j]:
                        high -= 1
                    if low > high:
                        dp[i][j] = (dp[i + 1][j - 1] * 2 + 2) % mod
                    elif low == high:
                        dp[i][j] = (dp[i + 1][j - 1] * 2 + 1) % mod
                    else:
                        dp[i][j] = (dp[i + 1][j - 1] * 2 - dp[low + 1][high - 1] + mod) % mod
        return dp[0][n - 1]

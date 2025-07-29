class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[-1] * n for _ in range(m)]

        def dfs(i: int, j: int) -> bool:
            if i < 0 and j < 0:
                return True
            if j < 0:
                return False
            if i < 0:
                for k in range(j + 1):
                    if p[k] != '*':
                        return False
                return True
            if dp[i][j] != -1:
                return dp[i][j]
            if p[j] == s[i] or p[j] == '?':
                dp[i][j] = dfs(i - 1, j - 1)
            elif p[j] == '*':
                dp[i][j] = dfs(i - 1, j) or dfs(i, j - 1)
            else:
                dp[i][j] = False
            return dp[i][j]
        
        return dfs(m - 1, n - 1)

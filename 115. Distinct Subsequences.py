class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        memo = [[-1] * n for _ in range(m)]

        def dfs(i: int, j: int) -> int:
            if j == n:
                return 1
            if m - i < n - j:
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            if s[i] == t[j]:
                memo[i][j] = dfs(i + 1, j) + dfs(i + 1, j + 1)
                return memo[i][j]
            memo[i][j] = dfs(i + 1, j)
            return memo[i][j]

        return dfs(0, 0)

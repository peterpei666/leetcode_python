class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        valid = [[False] * n for _ in range(3)]
        memo = [[False] * n for _ in range(3)]
        pal = [[False] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or pal[i + 1][j - 1]):
                    pal[i][j] = True
        
        def dfs(i: int, k: int) -> bool:
            if valid[k - 1][i]:
                return memo[k - 1][i]
            if n - i == k:
                return True
            valid[k - 1][i] = True
            if k == 1:
                memo[k - 1][i] = pal[i][n - 1]
                return memo[k - 1][i]
            for j in range(i + 1, n - k + 2):
                if pal[i][j - 1] and dfs(j, k - 1):
                    memo[k - 1][i] = True
                    return memo[k - 1][i]
            memo[k - 1][i] = False
            return memo[k - 1][i]
        
        return dfs(0, 3)

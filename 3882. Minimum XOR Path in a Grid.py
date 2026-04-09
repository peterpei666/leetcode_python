class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        mp = [[[False] * 1024 for _ in range(n)] for _ in range(2)]
        mp[0][0][grid[0][0]] = True
        for j in range(1, n):
            for k in range(1024):
                if mp[0][j - 1][k]:
                    mp[0][j][k ^ grid[0][j]] = True
        for i in range(1, m):
            t = i & 1
            p = t ^ 1
            mp[t] = [[False] * 1024 for _ in range(n)]
            for k in range(1024):
                if mp[p][0][k]:
                    mp[t][0][k ^ grid[i][0]] = True
            for j in range(1, n):
                for k in range(1024):
                    if mp[t][j - 1][k] or mp[p][j][k]:
                        mp[t][j][k ^ grid[i][j]] = True
        t = (m - 1) & 1
        for k in range(1024):
            if mp[t][n - 1][k]:
                return k
        return -1

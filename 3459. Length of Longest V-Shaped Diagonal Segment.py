from typing import List

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        m ,n = len(grid), len(grid[0])
        memo = [[[[-1] * 2 for _ in range(4)] for _ in range(n)] for _ in range(m)]
        dx = [-1, -1, 1, 1]
        dy = [-1, 1, 1, -1]

        def valid(i: int, j: int) -> bool:
            return 0 <= i < m and 0 <= j < n
        
        def dfs(i: int, j: int, dir: int, change: int) -> int:
            nonlocal memo
            if not memo[i][j][dir][change] == -1:
                return memo[i][j][dir][change]
            cnt = 1
            ni = i + dx[dir]
            nj = j + dy[dir]
            if valid(ni, nj) and ((grid[i][j] == 0 and grid[ni][nj] == 2) or (grid[i][j] == 2 and grid[ni][nj] == 0)):
                cnt = max(cnt, 1 + dfs(ni, nj, dir, change))
            if change:
                ndir = (dir + 1) % 4
                ni = i + dx[ndir]
                nj = j + dy[ndir]
                if valid(ni, nj) and ((grid[i][j] == 0 and grid[ni][nj] == 2) or (grid[i][j] == 2 and grid[ni][nj] == 0)):
                    cnt = max(cnt, 1 + dfs(ni, nj, ndir, change - 1))
            memo[i][j][dir][change] = cnt
            return cnt
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans = max(ans, 1)
                    for d in range(4):
                        ni = i + dx[d]
                        nj = j + dy[d]
                        if valid(ni, nj) and grid[ni][nj] == 2:
                            ans = max(ans, 1 + dfs(ni, nj, d, 1))
        return ans

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        cnt = 0
        if grid[0][0] <= k:
            cnt += 1
        for i in range(1, m):
            grid[i][0] = grid[i][0] + grid[i - 1][0]
            if grid[i][0] <= k:
                cnt += 1
        for i in range(1, n):
            grid[0][i] = grid[0][i] + grid[0][i - 1]
            if grid[0][i] <= k:
                cnt += 1
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]+ grid[i][j] - grid[i - 1][j - 1]
                if grid[i][j] <= k:
                    cnt += 1
        return cnt

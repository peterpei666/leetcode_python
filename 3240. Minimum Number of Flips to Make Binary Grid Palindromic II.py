class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        single = 0
        double = 0
        for i in range(m // 2):
            for j in range(n // 2):
                one = grid[i][j] + grid[i][n - j - 1] + grid[m - i - 1][j] + grid[m - i - 1][n - j - 1]
                ans += min(one, 4 - one)
            if n % 2 == 1:
                one = grid[i][n // 2] + grid[m - i - 1][n // 2]
                single += (one == 1)
                double += (one == 2)
        if m % 2 == 1:
            for j in range(n // 2):
                one = grid[m // 2][j] + grid[m // 2][n - j - 1]
                single += (one == 1)
                double += (one == 2)
            if n % 2 == 1:
                ans += (grid[m // 2][n // 2] == 1)
        if double % 2 == 0 or single > 0:
            return ans + single
        return ans + 2

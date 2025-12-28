from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m - 1, -1, -1):
            if grid[i][n - 1] >= 0:
                break
            for j in range(n - 1, -1, -1):
                if grid[i][j] >= 0:
                    break
                ans += 1
        return ans

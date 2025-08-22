from typing import List

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        x1, x2, y1, y2 = -1, -1, -1, -1
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    if x1 == -1:
                        x1 = i
                        y1 = j
                    x1 = min(x1, i)
                    x2 = max(x2, i)
                    y1 = min(y1, j)
                    y2 = max(y2, j)
        return (x2 - x1 + 1) * (y2 - y1 + 1) if not x1 == -1 else 0

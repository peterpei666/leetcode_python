from typing import List

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def count(grid: List[List[int]], l: int, r: int, u: int, d: int) -> int:
            x1, x2 = -1, -1
            y1, y2 = -1, -1
            for i in range(l, r + 1):
                for j in range(u, d + 1):
                    if grid[i][j]:
                        if x1 == -1:
                            x1 = i
                            y1 = j
                        x1 = min(x1, i)
                        x2 = max(x2, i)
                        y1 = min(y1, j)
                        y2 = max(y2, j)
            return (x2 - x1 + 1) * (y2 - y1 + 1) if not x1 == -1 else 0
        
        def solve(grid: List[List[int]]):
            m, n = len(grid), len(grid[0])
            ans = m * n
            for i in range(m - 1):
                for j in range(n - 1):
                    ans = min(ans, count(grid, 0, i, 0, n - 1) + count(grid, i + 1, m - 1, 0, j) + count(grid, i + 1, m - 1, j + 1, n - 1))
                    ans = min(ans, count(grid, 0, i, 0, j) + count(grid, 0, i, j + 1, n - 1) + count(grid, i + 1, m - 1, 0, n - 1))
            for i in range(m - 2):
                for j in range(i + 1, m - 1):
                    ans = min(ans, count(grid, 0, i, 0, n - 1) + count(grid, i + 1, j, 0, n - 1) + count(grid, j + 1, m - 1, 0, n - 1))
            return ans

        if not grid or not grid[0]:
            return 0
        trans = [[grid[i][j] for i in range(m)] for j in range(n)]
        return min(solve(grid), solve(trans))

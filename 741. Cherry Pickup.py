from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        memo = [[[None] * n for _ in range(n)] for _ in range(n)]

        def dfs(r1: int, c1: int, c2: int) -> int:
            r2 = r1 + c1 - c2
            if n == r1 or n == r2 or n == c1 or n == c2 or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')
            elif r1 == n - 1 and c1 == n - 1:
                return grid[r1][c1]
            elif memo[r1][c1][c2] is not None:
                return memo[r1][c1][c2]
            else:
                ans = grid[r1][c1]
                if not c1 == c2:
                    ans += grid[r2][c2]
                ans += max(dfs(r1, c1 + 1, c2 + 1), dfs(r1 + 1, c1, c2 + 1), dfs(r1, c1 + 1, c2), dfs(r1 + 1, c1, c2))
                memo[r1][c1][c2] = ans
                return ans
        
        return max(0, dfs(0, 0, 0))

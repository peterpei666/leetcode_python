from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        memo = [[0] * n for _ in range(m)]
        dir = [[-1, 0], [0, -1], [0, 1], [1, 0]]

        def dfs(i: int, j: int) -> int:
            nonlocal memo
            if memo[i][j]:
                return memo[i][j]
            memo[i][j] = 1
            for d in range(4):
                x = i + dir[d][0]
                y = j + dir[d][1]
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    memo[i][j] = max(memo[i][j], dfs(x, y) + 1)
            return memo[i][j]
        
        ans = 1
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
        return ans

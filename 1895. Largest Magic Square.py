from typing import List

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        mat = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                mat[i + 1][j + 1] = grid[i][j] + mat[i + 1][j] + mat[i][j + 1] - mat[i][j]
        for sz in range(min(m, n), 1, -1):
            for i in range(m - sz + 1):
                for j in range(n - sz + 1):
                    temp = mat[i + 1][j + sz] + mat[i][j] - mat[i + 1][j] - mat[i][j + sz]
                    if sum(grid[i + k][j + k] for k in range(sz)) == temp and sum(grid[i + k][j + sz - k - 1] for k in range(sz)) == temp and all(mat[i + k + 1][j + sz] - mat[i + k][j + sz] - mat[i + k + 1][j] + mat[i + k][j] == temp for k in range(sz)) and all(mat[i + sz][j + k + 1] - mat[i][j + k + 1] - mat[i + sz][j + k] + mat[i][j + k] == temp for k in range(sz)):
                        return sz
        return 1

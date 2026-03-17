from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j]:
                    matrix[i][j] = matrix[i - 1][j] + 1
        ans = 0
        for i in range(m):
            matrix[i].sort(reverse=True)
            for j in range(n):
                if not matrix[i][j]:
                    break
                ans = max(ans, matrix[i][j] * (j + 1))
        return ans

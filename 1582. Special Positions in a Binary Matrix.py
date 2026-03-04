from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row = [sum(mat[i]) for i in range(m)]
        col = [sum(mat[k][j] for k in range(m)) for j in range(n)]
        return sum(1 for i in range(m) for j in range(n) if mat[i][j] == 1 and row[i] == 1 and col[j] == 1)

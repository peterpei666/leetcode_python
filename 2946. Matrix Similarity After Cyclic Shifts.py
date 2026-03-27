from typing import List

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        for i in range(m):
            temp = [0] * n
            for j in range(n):
                temp[((j - k) % n + n) % n] = mat[i][j]
            if not temp == mat[i]:
                return False
        return True

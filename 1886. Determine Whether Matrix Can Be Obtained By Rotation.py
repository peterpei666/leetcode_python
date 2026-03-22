from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        flag = [True] * 4
        n = len(mat)
        for i in range(n):
            for j in range(n):
                if not mat[i][j] == target[i][j]:
                    flag[0] = False
                if not mat[i][j] == target[j][n - i - 1]:
                    flag[1] = False
                if not mat[i][j] == target[n - i - 1][n - j - 1]:
                    flag[2] = False
                if not mat[i][j] == target[n - j - 1][i]:
                    flag[3] = False
        return flag[0] | flag[1] | flag[2] | flag[3]

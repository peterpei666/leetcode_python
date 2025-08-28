from typing import List

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        for i in range(n):
            temp = []
            for j in range(n - i):
                temp.append(grid[i + j][j])
            temp.sort(reverse=True)
            for j in range(n - i):
                grid[i + j][j] = temp[j]
        for i in range(1, n):
            temp = []
            for j in range(n - i):
                temp.append(grid[j][i + j])
            temp.sort()
            for j in range(n - i):
                grid[j][i + j] = temp[j]
        return grid

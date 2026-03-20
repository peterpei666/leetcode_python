from typing import List

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                temp = []
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        temp.append(grid[x][y])
                temp.sort()
                t = temp[-1] - temp[0]
                for sz in range(1, len(temp)):
                    if temp[sz] != temp[sz - 1]:
                        t = min(t, temp[sz] - temp[sz - 1])
                ans[i][j] = t
        return ans

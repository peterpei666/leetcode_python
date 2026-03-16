from typing import List
from heapq import heappush, heappop

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        pre1 = [[0] * (n + 2) for _ in range(m + 1)]
        pre2 = [[0] * (n + 2) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                pre1[i + 1][j + 1] = pre1[i][j] + grid[i][j]
                pre2[i + 1][j + 1] = pre2[i][j + 2] + grid[i][j]
        mp = set()
        pq = []
        for i in range(m):
            for j in range(n):
                if not grid[i][j] in mp:
                    heappush(pq, grid[i][j])
                    mp.add(grid[i][j])
                    if len(pq) > 3:
                        heappop(pq)
                for k in range(i + 2, m, 2):
                    x1 = (i + k) // 2
                    y1 = j - (k - i) // 2
                    x2 = (i + k) // 2
                    y2 = j + (k - i) // 2
                    if y1 < 0 or y2 >= n:
                        break
                    temp = pre2[x1 + 1][y1 + 1] - pre2[i][j + 2] + (pre1[x2 + 1][y2 + 1] - pre1[i][j]) + (pre1[k + 1][j + 1] - pre1[x1][y1]) + (pre2[k + 1][j + 1] - pre2[x2][y2 + 2]) - (grid[i][j] + grid[k][j] + grid[x1][y1] + grid[x2][y2])
                    if not temp in mp:
                        heappush(pq, temp)
                        mp.add(temp)
                        if len(pq) > 3:
                            heappop(pq)
        pq.sort(reverse=True)
        return pq

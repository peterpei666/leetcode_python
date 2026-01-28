from heapq import heappush, heappop
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        INF = float('inf')
        dis = [[[INF] * n for _ in range(m)] for _ in range(k + 1)]
        dis[0][0][0] = 0
        pq = [(0, 0, 0, 0)]
        cells = []
        for i in range(m):
            for j in range(n):
                cells.append((grid[i][j], i, j))
        cells.sort()
        ptr = [0] * (k + 1)
        while pq:
            cost, t, x, y = heappop(pq)
            if cost != dis[t][x][y]:
                continue
            if x + 1 < m:
                nc = cost + grid[x + 1][y]
                if nc < dis[t][x + 1][y]:
                    dis[t][x + 1][y] = nc
                    heappush(pq, (nc, t, x + 1, y))
            if y + 1 < n:
                nc = cost + grid[x][y + 1]
                if nc < dis[t][x][y + 1]:
                    dis[t][x][y + 1] = nc
                    heappush(pq, (nc, t, x, y + 1))
            if t < k:
                p = ptr[t]
                while p < len(cells):
                    v, nx, ny = cells[p]
                    if v > grid[x][y]:
                        break
                    if cost < dis[t + 1][nx][ny]:
                        dis[t + 1][nx][ny] = cost
                        heappush(pq, (cost, t + 1, nx, ny))
                    p += 1
                ptr[t] = p
        return min(dis[t][m - 1][n - 1] for t in range(k + 1))

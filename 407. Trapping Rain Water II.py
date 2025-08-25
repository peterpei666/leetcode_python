from typing import List
from heapq import heappush, heappop

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        dir = [-1, 0, 0, -1, 0, 1, 1, 0]
        pq = []
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            heappush(pq, (heightMap[i][0], i, 0))
            heappush(pq, (heightMap[i][n - 1], i, n - 1))
            visited[i][0] = True
            visited[i][n - 1] = True
        for i in range(1, n - 1):
            heappush(pq, (heightMap[0][i], 0, i))
            heappush(pq, (heightMap[m - 1][i], m - 1, i))
            visited[0][i] = True
            visited[m - 1][i] = True
        ans = 0
        while pq:
            top = heappop(pq)
            for d in range(4):
                nx = top[1] + dir[d * 2]
                ny = top[2] + dir[d * 2 + 1]
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    ans += max(0, top[0] - heightMap[nx][ny])
                    heappush(pq, (max(top[0], heightMap[nx][ny]), nx, ny))
                    visited[nx][ny] = True
        return ans

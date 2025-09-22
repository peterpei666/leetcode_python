from typing import List
from collections import deque
import heapq

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        mp = dict()
        pq = []
        m, n = len(forest), len(forest[0])
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    heapq.heappush(pq, forest[i][j])
                    mp[forest[i][j]] = (i, j)
        dir = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        def bfs(x1: int, y1: int, x2: int, y2: int) -> int:
            q = deque()
            visited = [[False] * n for _ in range(m)]
            visited[x1][y1] = True
            q.append((0, x1, y1))
            while q:
                step, x, y = q.popleft()
                if x == x2 and y == y2:
                    return step
                for d in range(4):
                    nx = x + dir[d][0]
                    ny = y + dir[d][1]
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and forest[nx][ny] > 0:
                        visited[nx][ny] = True
                        q.append((step + 1, nx, ny))
            return -1
        
        ans = 0
        x, y = 0, 0
        while pq:
            nx, ny = mp[pq[0]]
            heapq.heappop(pq)
            dist = bfs(x, y, nx, ny)
            if dist == -1:
                return -1
            ans += dist
            x, y = nx, ny
        return ans

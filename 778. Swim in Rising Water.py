from typing import List
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        pq = [(grid[0][0], 0, 0)]
        n = len(grid)
        memo = [[float('inf')] * n for _ in range(n)]
        memo[0][0] = grid[0][0]
        dir = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        while pq:
            h, x, y = heapq.heappop(pq)
            if x == y == n - 1:
                break
            for d in range(4):
                nx = x + dir[d][0]
                ny = y + dir[d][1]
                if 0 <= nx < n and 0 <= ny < n:
                    temp = max(h, grid[nx][ny])
                    if temp < memo[nx][ny]:
                        memo[nx][ny] = temp
                        heapq.heappush(pq, (temp, nx, ny))
        return memo[-1][-1]

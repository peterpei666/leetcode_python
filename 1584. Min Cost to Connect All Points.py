from typing import List
from heapq import heappush, heappop

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n
        cnt = 0
        pq = [(0, 0)]
        ans = 0
        while pq and cnt < n:
            cost, node = pq[0]
            heappop(pq)
            if visited[node]:
                continue
            ans += cost
            visited[node] = True
            cnt += 1
            for i in range(n):
                if not visited[i]:
                    heappush(pq, (abs(points[i][0] - points[node][0]) + abs(points[i][1] - points[node][1]), i))
        return ans

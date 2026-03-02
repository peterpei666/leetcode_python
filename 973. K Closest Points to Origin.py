from typing import List
from math import sqrt
from heapq import heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        mp = {}
        for i in range(len(points)):
            mp[i] = sqrt(points[i][0] ** 2 + points[i][1] ** 2)
        pq = []
        for idx, dist in mp.items():
            heappush(pq, (-dist, idx))
            if len(pq) > k:
                heappop(pq)
        ans = []
        while pq:
            _, idx = heappop(pq)
            ans.append(points[idx])
        return ans

from typing import List
from heapq import heappush, heappop

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        mp = [(capital[i], profits[i]) for i in range(n)]
        mp.sort()
        pq = []
        i = 0
        while k:
            while i < n and mp[i][0] <= w:
                heappush(pq, -mp[i][1])
                i += 1
            if not pq:
                break
            w -= pq[0]
            heappop(pq)
            k -= 1
        return w

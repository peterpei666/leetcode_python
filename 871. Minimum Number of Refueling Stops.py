from typing import List
from heapq import heappush, heappop

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        cur = startFuel
        pos = 0
        pq = []
        for p, f in stations:
            if p <= cur:
                heappush(pq, -f)
                pos += 1
            else:
                break
        n = len(stations)
        ans = 0
        while pq:
            if cur >= target:
                break
            cur += -heappop(pq)
            ans += 1
            for i in range(pos, n):
                if stations[i][0] <= cur:
                    heappush(pq, -stations[i][1])
                    pos += 1
                else:
                    break
        return ans if cur >= target else -1

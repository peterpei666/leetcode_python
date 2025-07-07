import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        m = max(end for _, end in events)
        events.sort()
        pq = []
        ans = 0
        for i in range(1, m + 1):
            while events and events[0][0] == i:
                heapq.heappush(pq, events.pop(0)[1])
            while pq and pq[0] < i:
                heapq.heappop(pq)
            if pq:
                heapq.heappop(pq)
                ans += 1
        return ans

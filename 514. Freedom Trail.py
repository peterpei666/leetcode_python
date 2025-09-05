import heapq

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        m, n = len(key), len(ring)
        mp = [[] for _ in range(26)]
        for i in range(n):
            mp[ord(ring[i]) - ord('a')].append(i)
        pq = [(0, 0, 0)]
        dist = [[float('inf')] * n for _ in range(m + 1)]
        dist[0][0] = 0
        while pq:
            step, i, j = pq[0]
            heapq.heappop(pq)
            if i == m:
                return step
            if step > dist[i][j]:
                continue
            for p in mp[ord(key[i]) - ord('a')]:
                temp = min(abs(p - j), n - abs(p - j))
                if temp + step + 1 < dist[i + 1][p]:
                    dist[i + 1][p] = temp + step + 1
                    heapq.heappush(pq, (step + 1 + temp, i + 1, p))
        return -1

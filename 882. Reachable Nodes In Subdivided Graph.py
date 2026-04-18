from typing import List
import heapq

class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = {i: [] for i in range(n)}
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        dist = [-1] * n
        dist[0] = maxMoves
        pq = [(-maxMoves, 0)]
        while pq:
            moves, node = heapq.heappop(pq)
            moves = -moves
            if dist[node] > moves:
                continue
            for nxt, cost in graph[node]:
                remain = moves - cost - 1
                if remain > dist[nxt]:
                    dist[nxt] = remain
                    heapq.heappush(pq, (-remain, nxt))
        ans = sum(1 for d in dist if d >= 0)
        for u, v, w in edges:
            a = 0 if dist[u] == -1 else dist[u]
            b = 0 if dist[v] == -1 else dist[v]
            ans += min(w, a + b)
        return ans

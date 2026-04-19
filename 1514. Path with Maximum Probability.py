from typing import List
from heapq import heappush, heappop
from math import log, exp

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        m = len(succProb)
        graph = [[] for _ in range(n)]
        for i in range(m):
            if succProb[i] <= 0.00001:
                continue
            graph[edges[i][0]].append((edges[i][1], -log(succProb[i])))
            graph[edges[i][1]].append((edges[i][0], -log(succProb[i])))
        pq = [(0.0, start_node)]
        dis = [float('inf')] * n
        dis[start_node] = 0.0
        while pq:
            cur, node = pq[0]
            heappop(pq)
            if node == end_node:
                return exp(-cur)
            for next, cost in graph[node]:
                temp = cur + cost
                if temp < dis[next]:
                    dis[next] = temp
                    heappush(pq, (temp, next))
        return 0.0

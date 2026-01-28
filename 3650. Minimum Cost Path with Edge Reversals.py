from collections import defaultdict
import heapq

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, cost in edges:
            graph[u].append((v, cost))
            graph[v].append((u, cost * 2))
        pq = [(0, 0)]
        cost = [float('inf')] * n
        cost[0] = 0
        while pq:
            curr_cost, node = heapq.heappop(pq)
            if node == n - 1:
                break
            if curr_cost > cost[node]:
                continue
            for next_node, edge_cost in graph[node]:
                new_cost = cost[node] + edge_cost
                if new_cost < cost[next_node]:
                    cost[next_node] = new_cost
                    heapq.heappush(pq, (new_cost, next_node))
        return cost[n - 1] if cost[n - 1] != float('inf') else -1

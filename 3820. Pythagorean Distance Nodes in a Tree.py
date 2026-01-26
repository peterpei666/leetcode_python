from typing import List
from collections import deque

class Solution:
    def specialNodes(self, n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def bfs(start):
            dis = [-1] * n
            dis[start] = 0
            q = deque([start])
            while q:
                node = q.popleft()
                for next_node in graph[node]:
                    if dis[next_node] == -1:
                        dis[next_node] = dis[node] + 1
                        q.append(next_node)
            return dis
        
        def valid(a, b, c):
            return (a*a + b*b == c*c) or (b*b + c*c == a*a) or (a*a + c*c == b*b)
        
        dis1, dis2, dis3 = bfs(x), bfs(y), bfs(z)
        return sum(valid(dis1[i], dis2[i], dis3[i]) for i in range(n))

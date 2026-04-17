from typing import List
from collections import deque

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        for u, v in dislikes:
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)
        color = [-1] * n
        for start in range(n):
            if color[start] == -1:
                q = deque([start])
                color[start] = 0
                while q:
                    node = q.popleft()
                    for next_node in graph[node]:
                        if color[next_node] == -1:
                            color[next_node] = 1 - color[node]
                            q.append(next_node)
                        elif color[next_node] == color[node]:
                            return False
        return True

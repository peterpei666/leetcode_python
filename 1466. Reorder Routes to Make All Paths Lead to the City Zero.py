from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for e in connections:
            graph[e[1]].append((e[0], 0))
            graph[e[0]].append((e[1], 1))
        
        def dfs(p: int, u: int) -> int:
            ans = 0
            for v, c in graph[u]:
                if not p == v:
                    ans += c + dfs(u, v)
            return ans
        
        return dfs(-1, 0)

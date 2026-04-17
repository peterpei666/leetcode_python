from typing import List

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        cnt = [1] * n
        dis = [0] * n
        
        def dfs1(p: int, u: int) -> None:
            for v in graph[u]:
                if not p == v:
                    dfs1(u, v)
                    cnt[u] += cnt[v]
                    dis[u] += dis[v] + cnt[v]
            
        def dfs2(p: int, u: int) -> None:
            for v in graph[u]:
                if not p == v:
                    dis[v] = dis[u] + n - cnt[v] * 2
                    dfs2(u, v)
        
        dfs1(-1, 0)
        dfs2(-1, 0)
        return dis

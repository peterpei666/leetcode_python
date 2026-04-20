from typing import List
from collections import defaultdict

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        dfn = [-1] * n
        low = [-1] * n
        timer = 0
        ans = []
        stk = [(0, -1, 0)]
        while stk:
            u, p, idx = stk[-1]
            if idx == 0:
                if not dfn[u] == -1:
                    stk.pop()
                    continue
                dfn[u] = timer
                low[u] = timer
                timer += 1
            if idx < len(graph[u]):
                v = graph[u][idx]
                stk[-1] = (u, p, idx + 1)
                if v == p:
                    continue
                if dfn[v] == -1:
                    stk.append((v, u, 0))
                else:
                    low[u] = min(low[u], dfn[v])
            else:
                stk.pop()
                if not p == -1:
                    low[p] = min(low[p], low[u])
                    if low[u] > dfn[p]:
                        ans.append([p, u])
        return ans

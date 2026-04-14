from typing import List, DefaultDict
    
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = DefaultDict(list)
        for i in range(len(equations)):
            u, v = equations[i]
            graph[u].append((v, values[i]))
            graph[v].append((u, 1 / values[i]))
        ans = []
        for u, v in queries:
            visited = set()

            def dfs(node, cur, target):
                if node == target:
                    return cur
                for next, val in graph[node]:
                    if not next in visited:
                        visited.add(next)
                        temp = dfs(next, cur * val, target)
                        if not temp == -1.0:
                            return temp
                return -1.0

            if not u in graph or not v in graph:
                ans.append(-1.0)
            else:
                ans.append(dfs(u, 1.0, v))
        return ans

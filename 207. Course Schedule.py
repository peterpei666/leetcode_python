from typing import List

class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        for pre in prerequisites:
            graph[pre[1]].append(pre[0])
        visited = [False] * n
        path = [False] * n

        def dfs(node: int) -> bool:
            nonlocal visited, path
            if visited[node]:
                return True
            if path[node]:
                return False
            path[node] = True
            for next in graph[node]:
                if not dfs(next):
                    return False
            visited[node] = True
            path[node] = False
            return True
        
        return not any(not dfs(i) for i in range(n))

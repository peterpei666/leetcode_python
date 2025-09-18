from typing import List

class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(n)]
        for pre in prerequisites:
            graph[pre[1]].append(pre[0])
        visited = [False] * n

        def dfs(node: int, target: int) -> bool:
            nonlocal visited
            if node == target:
                return True
            visited[node] = True
            for next in graph[node]:
                if not visited[next]:
                    if dfs(next, target):
                        return True
        
        q = len(queries)
        ans = [False] * q
        for i in range(q):
            visited = [False] * n
            if dfs(queries[i][1], queries[i][0]):
                ans[i] = True
        return ans

from typing import List

class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for pre in prerequisites:
            graph[pre[1]].append(pre[0])
        visited = [False] * n
        path = [False] * n
        ans = []

        def dfs(node: int) -> bool:
            nonlocal visited, path, ans
            if path[node]:
                return False
            if visited[node]:
                return True
            visited[node] = True
            path[node] = True
            for next in graph[node]:
                if not dfs(next):
                    return False
            path[node] = False
            ans.append(node)
            return True
        
        for i in range(n):
            if not dfs(i):
                return []
        return ans[::-1]

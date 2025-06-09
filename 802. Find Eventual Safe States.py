class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visited = [False] * n
        safe = [False] * n
        def dfs(node):
            if visited[node]:
                return safe[node]
            visited[node] = True
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            safe[node] = True
            return True
        for i in range(n):
            if not visited[i]:
                dfs(i)
        return [i for i in range(n) if safe[i]]

class Solution:
    def minIncrease(self, n: int, edges: List[List[int]], cost: List[int]) -> int:
        graph = [[] for _ in range(n)]
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        def dfs(node: int, p: int):
            if len(graph[node]) == 1 and node:
                return [cost[node], 0]
            cnt = 0
            m = 0
            temp = []
            for c in graph[node]:
                if c != p:
                    t = dfs(c, node)
                    temp.append(t[0])
                    cnt += t[1]
                    m = max(m, t[0])
            for c in temp:
                if c < m:
                    cnt += 1
            return [cost[node] + m, cnt]
        return dfs(0, -1)[1]

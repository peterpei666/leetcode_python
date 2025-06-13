class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(len(edges) + 2)]
        self.ans = 0
        for u in edges:
            graph[u[0]].append(u[1])
            graph[u[1]].append(u[0])
        def dfs(node: int, parent: int,cur: int) -> None:
            self.ans = max(self.ans, cur)
            for neighbor in graph[node]:
                if neighbor != parent:
                    dfs(neighbor, node, cur + 1)
        dfs(1, -1, 0)
        temp = 2
        ret = 1
        ans = self.ans - 1
        while ans:
            if ans & 1:
                ret *= temp
                ret %= 10 ** 9 + 7
            ans >>= 1
            temp *= temp
            temp %= 10 ** 9 + 7
        return ret

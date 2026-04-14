from typing import List

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = [[] for _ in range(n)]
        for u, v in richer:
            graph[v].append(u)
        ans = [-1] * n

        def dfs(cur: int) -> int:
            if not ans[cur] == -1:
                return ans[cur]
            ans[cur] = cur
            for next in graph[cur]:
                t = dfs(next)
                if quiet[ans[cur]] > quiet[t]:
                    ans[cur] = t
            return ans[cur]

        for i in range(n):
            dfs(i)
        return ans

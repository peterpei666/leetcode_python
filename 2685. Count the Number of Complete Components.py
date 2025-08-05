from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[i] for i in range(n)]
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        mp = defaultdict(int)
        for i in range(n):
            graph[i].sort()
            mp[tuple(graph[i])] += 1
        cnt = 0
        for key in mp:
            if len(list(key)) == mp[key]:
                cnt += 1
        return cnt

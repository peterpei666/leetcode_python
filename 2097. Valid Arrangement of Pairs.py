from typing import List
from collections import defaultdict

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)
        mp = defaultdict(list)
        for p in pairs:
            in_degree[p[1]] += 1
            out_degree[p[0]] += 1
            mp[p[0]].append(p[1])
        start = pairs[0][0]
        for i in mp:
            if out_degree[i] == in_degree[i] + 1:
                start = i
                break
        ans = []

        def dfs(mp, ans, p):
            while mp[p]:
                next_node = mp[p].pop()
                dfs(mp, ans, next_node)
                ans.append([p, next_node])
                
        dfs(mp, ans, start)
        ans.reverse()
        return ans

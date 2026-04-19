from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        degree = [False] * (len(edges) + 2)
        for u, v in edges:
            if degree[u]:
                return u
            degree[u] = True
            if degree[v]:
                return v
            degree[v] = True
        return -1

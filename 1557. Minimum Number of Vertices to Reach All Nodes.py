from typing import List

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        in_degree = [0] * n
        for _, v in edges:
            in_degree[v] += 1
        return [i for i in range(n) if not in_degree[i]]

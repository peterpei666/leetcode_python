from typing import List

class DSU:
    def __init__(self, n: int) -> None:
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.parity = [0] * n

    def find(self, x: int) -> tuple[int, int]:
        if self.parent[x] == x:
            return (x, 0)
        p, o = self.find(self.parent[x])
        self.parent[x] = p
        self.parity[x] ^= o
        return (self.parent[x], self.parity[x])
    
    def unite(self, x: int, y: int, w: int) -> bool:
        px, ox = self.find(x)
        py, oy = self.find(y)
        if px == py:
            return (ox ^ oy) == w
        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
            self.parity[py] = ox ^ oy ^ w
        elif self.rank[px] < self.rank[py]:
            self.parent[px] = py
            self.parity[px] = ox ^ oy ^ w
        else:
            self.parent[py] = px
            self.parity[py] = ox ^ oy ^ w
            self.rank[px] += 1
        return True

class Solution:
    def numberOfEdgesAdded(self, n: int, edges: List[List[int]]) -> int:
        ans = 0
        dsu = DSU(n)
        for u, v, w in edges:
            if dsu.unite(u, v, w):
                ans += 1
        return ans

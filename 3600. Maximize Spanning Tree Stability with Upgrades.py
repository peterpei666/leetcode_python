from typing import List

class DSU:
    def __init__(self, n: int) -> None:
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.count = n

    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def unite(self, x: int, y: int) -> bool:
        rootX = self.find(x)
        rootY = self.find(y)
        if not rootX == rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            self.count -= 1
            return True
        return False
    
class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        def check(x: int) -> bool:
            dsu = DSU(n)
            for u, v, s, must in edges:
                if must:
                    if s < x:
                        return False
                    if not dsu.unite(u, v):
                        return False
            for u, v, s, must in edges:
                if not must and s >= x:
                    dsu.unite(u, v)
            used = 0
            for u, v, s, must in edges:
                if not must and s < x and 2 * s >= x:
                    if dsu.unite(u, v):
                        used += 1
                        if used > k:
                            return False
            return dsu.count == 1
        
        dsu = DSU(n)
        for u, v, _, must in edges:
                if must and not dsu.unite(u, v):
                    return -1
        l, r = 1, 200000
        ans = -1
        while l <= r:
            mid = l + (r - l) // 2
            if check(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans    

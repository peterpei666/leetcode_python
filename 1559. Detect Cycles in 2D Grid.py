from typing import List

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            self.count -= 1
            return True
        return False

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def get_count(self) -> int:
        return self.count
    
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        r = len(grid)
        c = len(grid[0])
        dsu = DSU(r * c)
        for i in range(r - 1):
            ridx = i * c;
            for j in range(c - 1):
                cur = ridx + j
                alpha = grid[i][j]
                if grid[i + 1][j] == alpha and not dsu.unite(cur + c, cur):
                    return True
                if grid[i][j + 1] == alpha and not dsu.unite(cur + 1, cur):
                    return True
            cur = i * c + c - 1
            alpha = grid[i][c - 1]
            if grid[i + 1][c - 1] == alpha and not dsu.unite(cur + c, cur):
                return True
        ridx = (r - 1) * c
        for j in range(c - 1):
            cur = ridx + j
            alpha = grid[r - 1][j]
            if grid[r - 1][j + 1] == alpha and not dsu.unite(cur + 1, cur):
                return True
        return False

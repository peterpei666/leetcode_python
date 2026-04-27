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
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        dsu = DSU(m * n)
        for i in range(m):
            for j in range(n):
                if i and (grid[i][j] == 2 or grid[i][j] == 5 or grid[i][j] == 6) and (grid[i - 1][j] == 2 or grid[i - 1][j] == 3 or grid[i - 1][j] == 4):
                    dsu.unite(i * n + j , (i - 1) * n + j)
                if j and (grid[i][j] == 1 or grid[i][j] == 3 or grid[i][j] == 5) and (grid[i][j - 1] == 1 or grid[i][j - 1] == 4 or grid[i][j - 1] == 6):
                    dsu.unite(i * n + j, i * n + j - 1)
        return dsu.connected(0, m * n - 1)
                

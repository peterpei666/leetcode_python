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
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        dsu = DSU(n)
        row = [-1] * 10001
        col = [-1] * 10001
        for i in range(n):
            if row[stones[i][0]] == -1:
                row[stones[i][0]] = i
            else:
                dsu.unite(i, row[stones[i][0]])
            if col[stones[i][1]] == -1:
                col[stones[i][1]] = i
            else:
                dsu.unite(i, col[stones[i][1]])
        return n - dsu.get_count()

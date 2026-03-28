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
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        dsu = DSU(n)
        for i in range(n):
            if not lcp[i][i] == n - i:
                return ''
            for j in range(i + 1, n):
                if lcp[i][j]:
                    dsu.unite(i, j)
        if dsu.count > 26:
            return ''
        s = ['0'] * n
        cur = 0
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(n):
            parent = dsu.find(i)
            if s[parent] == '0':
                s[parent] = alphabet[cur]
                cur += 1
            s[i] = s[parent]
        for i in range(n):
            for j in range(i):
                x = lcp[i][j]
                if not x == lcp[j][i] or x + i > n:
                    return ''
                y = lcp[i + 1][j + 1] if i + 1 < n else 0
                y = y + 1 if s[i] == s[j] else 0
                if not x == y:
                    return ''
        return ''.join(s)

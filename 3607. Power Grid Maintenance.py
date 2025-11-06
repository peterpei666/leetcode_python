from typing import List
from collections import defaultdict
from sortedcontainers import SortedSet

class DSU:
    def __init__(self, n: int) -> None:
        self.parent = [i for i in range(n)]
        self.rank = [i for i in range(n)]
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
    
    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
    
    def get_count(self) -> int:
        return self.count
    

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        mp = DSU(c + 1)
        for con in connections:
            mp.unite(con[0], con[1])
        temp = defaultdict(SortedSet)
        for i in range(1, c + 1):
            temp[mp.find(i)].add(i)
        ans = []
        for q in queries:
            if q[0] == 1:
                if not temp[mp.find(q[1])]:
                    ans.append(-1)
                elif q[1] in temp[mp.find(q[1])]:
                    ans.append(q[1])
                else:
                    ans.append(temp[mp.find(q[1])][0])
            else:
                if q[1] in temp[mp.find(q[1])]:
                    temp[mp.find(q[1])].remove(q[1])
        return ans

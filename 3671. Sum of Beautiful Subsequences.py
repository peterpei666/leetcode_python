from typing import List
from collections import defaultdict

class Fenwick:
    def __init__ (self, n: int):
        self.n = n + 1
        self.memo = [0] * self.n

    def sum(self, i: int) -> int:
        ans = 0
        while i > 0:
            ans += self.memo[i]
            i -= i & -i
        return ans
    
    def add(self, i: int, x: int) -> None:
        while i < self.n:
            self.memo[i] += x
            i += i & -i

class Solution:
    def totalBeauty(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        m = max(nums) + 1
        mp = defaultdict(list)
        n = len(nums)
        f = [0] * m
        for i in range(n):
            mp[nums[i]].append(i)
        for d in range(1, m):
            temp = []
            for v in range(d, m, d):
                if v in mp:
                    temp += mp[v]
            if len(temp) <= 1:
                f[d] = len(temp)
                continue
            temp.sort()
            rank = dict()
            sz = len(temp)
            for r in range(sz):
                rank[temp[r]] = r + 1
            fen = Fenwick(sz)
            for v in range(d, m, d):
                if v in mp:
                    for p in reversed(mp[v]):
                        r = rank[p]
                        add = 1 + fen.sum(r - 1)
                        f[d] = (f[d] + add) % mod
                        fen.add(r, add % mod)
        for d in range(m - 1, 0, -1):
            for e in range(2 * d, m, d):
                f[d] = (f[d] - f[e] + mod) % mod
        ans = 0
        for d in range(1, m):
            ans = (ans + d * f[d]) % mod
        return ans

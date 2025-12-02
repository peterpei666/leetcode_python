from typing import List
from collections import defaultdict

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        mp = defaultdict(int)
        for p in points:
            mp[p[1]] += 1
        total = 0
        for _, n in mp.items():
            total += n * (n - 1) // 2
        ans = 0
        mod = 10 ** 9 + 7
        for _, n in mp.items():
            ans += (n * (n - 1) // 2) * (total - n * (n - 1) // 2) % mod
        if ans & 1:
            return (ans + mod) // 2 % mod
        return ans // 2 % mod

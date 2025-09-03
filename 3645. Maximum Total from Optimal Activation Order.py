from typing import List
from collections import defaultdict

class Solution:
    def maxTotal(self, value: List[int], limit: List[int]) -> int:
        mp = defaultdict(list)
        n = len(value)
        for i in range(n):
            mp[limit[i]].append(value[i])
        ans = 0
        for lim, pq in mp.items():
            pq.sort(reverse=True)
            ans += sum(pq[:min(len(pq), lim)])
        return ans

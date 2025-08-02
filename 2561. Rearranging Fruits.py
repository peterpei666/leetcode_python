from typing import List
from collections import defaultdict

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        freq = defaultdict(int)
        m = float('inf')
        for i in basket1:
            freq[i] += 1
            m = min(m, i)
        for i in basket2:
            freq[i] -= 1
            m = min(m, i)
        merge = []
        for k, c in freq.items():
            if c % 2:
                return -1
            merge.extend([k] * (abs(c) // 2))
        if not merge:
            return 0
        merge.sort()
        return sum(min(2 * m, merge[i]) for i in range(len(merge) // 2))

from collections import defaultdict
from typing import List

class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
        mp = defaultdict(int)
        for w in words:
            if len(w) >= k:
                mp[w[:k]] += 1
        return sum(1 for _, n in mp.items() if n >= 2)

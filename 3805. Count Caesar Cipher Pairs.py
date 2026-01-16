from typing import List
from collections import defaultdict

class Solution:
    def countPairs(self, words: List[str]) -> int:

        def key(s: str) -> str:
            a = ord(s[0]) - ord('a')
            return ''.join(chr((ord(c) - ord('a') - a + 26) % 26 + ord('a')) for c in s)
        
        mp = defaultdict(int)
        for w in words:
            mp[key(w)] += 1
        return sum(n * (n - 1) // 2 for n in mp.values())

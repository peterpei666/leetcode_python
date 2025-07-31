from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        mp = defaultdict(int)

        def valid() -> bool:
            for c in mp:
                if mp[c] > 0:
                    return False
            return True
        
        for c in t:
            mp[c] += 1
        l, r = 0, 0
        minlen = m + 1
        start = 0
        while r < m:
            if s[r] in mp:
                mp[s[r]] -= 1
            r += 1
            while valid():
                if r - l < minlen:
                    minlen = r - l
                    start = l
                if s[l] in mp:
                    mp[s[l]] += 1
                l += 1
        return "" if minlen == m + 1 else s[start:start + minlen]

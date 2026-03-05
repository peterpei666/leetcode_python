from typing import List

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        ans = []
        n = len(pattern)
        for s in queries:
            t = True
            idx = 0
            for c in s:
                if idx < n and pattern[idx] == c:
                        idx += 1
                elif ord(c) >= ord('A') and ord(c) <= ord('Z'):
                    t = False
                    break
            t = t and idx == n
            ans.append(t)
        return ans

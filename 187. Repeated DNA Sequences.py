from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []
        val = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        t = 0xFFFFF
        mask = 0
        for i in range(9):
            mask = (mask << 2) | val[s[i]]
        n = len(s)
        mp = dict()
        for i in range(9, n):
            mask = ((mask << 2) & t) | val[s[i]]
            if not mask in mp:
                mp[mask] = (1, i - 9)
            else:
                temp = mp[mask]
                mp[mask] = (temp[0] + 1, temp[1])
        return [s[idx:idx+10] for cnt, idx in mp.values() if cnt > 1]

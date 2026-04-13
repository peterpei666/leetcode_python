from typing import DefaultDict

class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        cnt0 = s.count('0')
        cnt1 = n - cnt0
        cur, ans = 0, 0
        mp = DefaultDict(list)
        mp[0].append(-1)
        for i in range(n):
            cur += 1 if s[i] == '1' else -1
            for k in [cur - 2, cur, cur + 2]:
                if not k in mp:
                    continue
                for l in mp[k]:
                    sz = i - l
                    dif = cur - k
                    c1 = (sz + dif) // 2
                    c0 = sz - c1
                    if dif == 0 or (dif == 2 and cnt0 > c0) or (dif == -2 and cnt1 > c1):
                        ans = max(ans, sz)
            if len(mp[cur]) < 2:
                mp[cur].append(i)
        return ans

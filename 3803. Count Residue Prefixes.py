class Solution:
    def residuePrefixes(self, s: str) -> int:
        n = len(s)
        mask = 0
        ans = 0
        cnt = 0
        for i in range(n):
            if cnt >= 3:
                break
            if (mask & (1 << (ord(s[i]) - ord('a')))) == 0:
                mask |= 1 << (ord(s[i]) - ord('a'))
                cnt += 1
            if (i + 1) % 3 == cnt:
                ans += 1
        return ans

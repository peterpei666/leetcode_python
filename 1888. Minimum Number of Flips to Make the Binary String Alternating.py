class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        cur0 = sum((ord(s[i]) - ord('0')) ^ (i & 1) for i in range(n))
        cur1 = sum((ord(s[i]) - ord('0')) ^ (i & 1) ^ 1 for i in range(n))
        ans = min(cur0, cur1)
        for i in range(n, 2 * n):
            cur0 += (ord(s[i % n]) - ord('0')) ^ (i & 1)
            cur1 += (ord(s[i % n]) - ord('0')) ^ (i & 1) ^ 1
            cur0 -= (ord(s[i % n]) - ord('0')) ^ ((i - n) & 1)
            cur1 -= (ord(s[i % n]) - ord('0')) ^ ((i - n) & 1) ^ 1
            ans = min(ans, min(cur0, cur1))
        return ans

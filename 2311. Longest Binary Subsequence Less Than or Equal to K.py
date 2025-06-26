class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        bit = 0
        temp = k
        while temp:
            bit += 1
            temp >>= 1
        cnt, cur = 0, 0
        n = len(s)
        for i in range(n):
            c = s[n - 1 - i]
            if c == '1':
                if i < bit and cur + (1 << i) <= k:
                    cur += 1 << i
                    cnt += 1
            else:
                cnt += 1
        return cnt

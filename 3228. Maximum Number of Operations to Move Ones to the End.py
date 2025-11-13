class Solution:
    def maxOperations(self, s: str) -> int:
        cnt, ans = 0, 0
        n = len(s)
        for i in range(n):
            if s[i] == '1':
                cnt += 1
            if s[i] == '0' and (i + 1 >= n or s[i + 1] == '1'):
                ans += cnt
        return ans

class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = ""
        ans += s[0]
        n, cnt = len(s), 1
        for i in range(1, n):
            if s[i] != s[i - 1]:
                cnt = 1
            else:
                cnt += 1
            if cnt <= 2:
                ans += s[i]
        return ans

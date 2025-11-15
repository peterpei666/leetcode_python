class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        pre = [-1] + [0] * n
        for i in range(n):
            if i == 0 or (i > 0 and s[i - 1] == '0'):
                pre[i + 1] = i
            else:
                pre[i + 1] = pre[i]
        ans = 0
        for i in range(1, n + 1):
            cnt = 1 if s[i - 1] == '0' else 0
            j = i
            while j > 0 and cnt * cnt <= n:
                cnt1 = i - pre[j] - cnt
                if cnt * cnt <= cnt1:
                    ans += min(j - pre[j], cnt1 - cnt * cnt + 1)
                cnt += 1
                j = pre[j]
        return ans 

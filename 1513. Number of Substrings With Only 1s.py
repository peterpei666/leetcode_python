class Solution:
    def numSub(self, s: str) -> int:
        ans, cnt = 0, 0
        mod = 10 ** 9 + 7
        for c in s:
            if c == '0':
                ans = (ans + cnt * (cnt + 1) // 2) % mod
                cnt = 0
            else:
                cnt += 1
        return (ans + cnt * (cnt + 1) // 2) % mod

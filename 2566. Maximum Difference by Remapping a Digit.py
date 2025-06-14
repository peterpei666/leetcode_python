class Solution:
    def minMaxDifference(self, num: int) -> int:
        l = float('inf')
        r = float('-inf')
        cnt = [0] * 10
        t = 1
        temp = num
        while temp:
            cnt[temp % 10] += t
            t *= 10
            temp //= 10
        for i in range(10):
            l = min(l, num - cnt[i] * (i - 0))
            r = max(r, num + cnt[i] * (9 - i))
        return r - l

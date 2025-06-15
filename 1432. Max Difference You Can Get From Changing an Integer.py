class Solution:
    def maxDiff(self, num: int) -> int:
        cnt = [0] * 10
        temp = num
        t = 1
        top = 0
        while temp:
            cnt[temp % 10] += t
            if 0 < temp < 10:
                top = temp
            temp //= 10
            t *= 10
        m1 = float('-inf')
        m2 = float('inf')
        for i in range(10):
            m1 = max(m1, num + cnt[i] * (9 - i))
            if i == top:
                m2 = min(m2, num - cnt[i] * (i - 1))
            else:
                m2 = min(m2, num - cnt[i] * i)
        return m1 - m2

class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        cnt = [0] * 10
        while n:
            cnt[n % 10] += 1
            n //= 10
        p = -1
        for i in range(10):
            if cnt[i] == 0:
                continue
            if p == -1 or cnt[i] < cnt[p]:
                p = i
        return p

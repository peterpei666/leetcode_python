class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        n0 = s.count('0')
        n1 = n - n0
        if n0 == 0:
            return 0
        for i in range(1, n + 1):
            p = i * k
            if (p - n0) % 2:
                continue
            if i % 2:
                if n0 <= p <= n0 * i + n1 * (i - 1):
                    return i
            else:
                if n0 <= p <= n0 * (i - 1) + n1 * i:
                    return i
        return -1

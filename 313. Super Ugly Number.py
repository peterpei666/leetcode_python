from typing import List

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        m = len(primes)
        ugly = [1] + [0] * (n - 1)
        idx, next = [0] * m, primes[:]
        for i in range(1, n):
            t = min(next)
            ugly[i] = t
            for j in range(m):
                if next[j] == t:
                    idx[j] += 1
                    next[j] = ugly[idx[j]] * primes[j]
        return ugly[-1]

from typing import List
from math import sqrt

class Solution:
    prime = [2]
    def largestPrime(self, n: int) -> int:
        def isPrime(x: int) -> bool:
            for p in Solution.prime:
                if p > sqrt(x):
                    break
                if x % p == 0:
                    return False
            return True
        
        if len(Solution.prime) == 1:
            for p in range(3, 500001, 2):
                if isPrime(p):
                    Solution.prime.append(p)
        total, ans = 0, 0
        for p in Solution.prime:
            total += p
            if total > n:
                break
            if isPrime(total):
                ans = total
        return ans

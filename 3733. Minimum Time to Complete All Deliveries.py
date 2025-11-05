from typing import List
from math import gcd

class Solution:
    def minimumTime(self, a: List[int], b: List[int]) -> int:
        t = (b[0] * b[1]) // gcd(b[0], b[1])
        l = a[0] + a[1]
        r = 1 << 35
        while l < r:
            mid = (l + r) // 2
            t4 = mid // t
            t2 = mid // b[1] - t4
            t3 = mid // b[0] - t4
            t1 = mid - t2 - t3 - t4
            if (t1 < max(0, a[0] - t2) + max(0, a[1] - t3)):
                l = mid + 1
            else:
                r = mid
        return l

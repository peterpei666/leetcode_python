from math import sqrt
from typing import List

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def get(x: int, t: int) -> int:
            return (int(sqrt(8 * (x / t) + 1)) - 1) // 2
        
        def check(x: int) -> bool:
            cur = 0
            for i in workerTimes:
                cur += get(x, i)
                if cur >= mountainHeight:
                    return True
            return False
        
        l, r = 0, 10 ** 18
        ans = -1
        while l <= r:
            mid = l + (r - l) // 2
            if check(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans

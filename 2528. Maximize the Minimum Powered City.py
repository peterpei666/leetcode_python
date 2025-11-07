from typing import List

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        diff = [0] * (n + 1)
        for i in range(n):
            diff[max(0, i - r)] += stations[i]
            diff[min(n, i + r + 1)] -= stations[i]
        
        def check(target: int) -> bool:
            curDiff = diff[:]
            cur, remain = 0, k
            for i in range(n):
                cur += curDiff[i]
                if cur < target:
                    add = target - cur
                    if add > remain:
                        return False
                    remain -= add
                    cur += add
                    pos = i + 2 * r + 1
                    if pos < n:
                        curDiff[pos] -= add
            return True
        
        low, high = 0, sum(stations) + k
        while low < high:
            mid = (low + high + 1) // 2
            if (check(mid)):
                low = mid
            else:
                high = mid - 1
        return low

from typing import List
from bisect import bisect_left

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        pos = []
        for x, y in points:
            if y == 0:
                pos.append(x)
            elif x == side:
                pos.append(side + y)
            elif y == side:
                pos.append(3 * side - x)
            else:
                pos.append(4 * side - y)
        pos.sort()
        n = len(pos)

        def valid(d: int) -> bool:
            for i in range(n):
                ptr = i
                cnt = 1
                while cnt < k:
                    target = pos[ptr] + d
                    j = bisect_left(pos, target)
                    if j == n:
                        break
                    ptr = j
                    cnt += 1
                    if d + pos[ptr] > pos[i] + 4 * side:
                        cnt = 0
                        break
                if cnt == k:
                    return True
            return False
        
        l, r = 0, side
        ans = 0
        while l <= r:
            mid = (l + r) // 2
            if valid(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

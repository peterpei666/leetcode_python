from typing import List
from bisect import bisect_left, insort

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        mp = []
        l = 0
        for r, x in enumerate(nums):
            low = x - valueDiff
            pos = bisect_left(mp, low)
            if pos < len(mp) and abs(mp[pos] - x) <= valueDiff:
                return True
            insort(mp, x)
            if r - l >= indexDiff:
                del mp[bisect_left(mp, nums[l])]
                l += 1
        return False

from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mp = [False] * 101
        l, r = 101, 0
        for i in nums:
            l = min(l, i)
            r = max(r, i)
            mp[i] = True
        return [i for i in range(l, r) if not mp[i]]

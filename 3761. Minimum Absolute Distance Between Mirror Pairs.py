from typing import List

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def rev(x: int) -> int:
            return int(str(x)[::-1])
        
        mp = dict()
        ans = 10 ** 9
        for i, x in enumerate(nums):
            if x in mp:
                ans = min(ans, i - mp[x])
            mp[rev(x)] = i
        return -1 if ans == 10 ** 9 else ans

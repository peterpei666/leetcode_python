from typing import List, DefaultDict
from bisect import bisect_left

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        mp = DefaultDict(list)
        for i, x in enumerate(nums):
            mp[x].append(i)
        n = len(nums)

        def min_dis(a: int, b: int) -> int:
            if a > b:
                a, b = b, a
            return min(b - a, a + n - b)
        
        ans = []
        for q in queries:
            target = nums[q]
            k = len(mp[target])
            if k == 1:
                ans.append(-1)
                continue
            idx = bisect_left(mp[target], q)
            ans.append(min(min_dis(mp[target][(idx - 1 + k) % k], q), min_dis(q, mp[target][(idx + 1 + k) % k])))
        return ans

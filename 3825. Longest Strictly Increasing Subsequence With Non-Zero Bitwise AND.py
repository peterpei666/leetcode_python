from typing import List
from bisect import bisect_left

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        def lis(nums: List[int]) -> int:
            res = []
            for i in nums:
                if not res or res[-1] < i:
                    res.append(i)
                else:
                    res[bisect_left(res, i)] = i
            return len(res)
        
        ans = 0
        for i in range(31):
            sub = []
            for k in nums:
                if k & (1 << i):
                    sub.append(k)
            ans = max(ans, lis(sub))
        return ans

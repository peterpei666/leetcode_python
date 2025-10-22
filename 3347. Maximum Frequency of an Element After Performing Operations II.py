from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        def check(n: int) -> int:
            l = bisect_left(nums, n)
            r = bisect_right(nums, n)
            ll = bisect_left(nums, n - k)
            rr = bisect_right(nums, n + k)
            return min(numOperations, (rr - r) + (l - ll)) + (r - l)
        
        nums.sort()
        ans = 1
        for i in nums:
            ans = max(check(i), ans)
            ans = max(check(i - k), ans)
            ans = max(check(i + k), ans)
        return ans

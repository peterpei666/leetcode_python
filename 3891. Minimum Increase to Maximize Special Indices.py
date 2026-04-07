from typing import List

class Solution:
    def minIncrease(self, nums: List[int]) -> int:
        def get(i: int) -> int:
            return max(0, max(nums[i - 1], nums[i + 1]) + 1 - nums[i])
        
        n = len(nums)
        if n & 1:
            ans = 0
            return sum(get(i) for i in range(1, n, 2))
        cur = 0
        for i in range(2, n - 1, 2):
            cur += get(i)
        ans = cur
        for i in range(1, n - 2, 2):
            cur += get(i) - get(i + 1)
            ans = min(ans, cur)
        return ans

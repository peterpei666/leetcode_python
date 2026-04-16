from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        cur = sum(i * nums[i] for i in range(n))
        ans = cur
        for i in range(n - 1, -1, -1):
            cur = cur + total - n * nums[i]
            ans = max(ans, cur)
        return ans

from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            nums[i] = abs(nums[i])
        nums.sort(reverse=True)
        ans = 0
        for i in range((n + 1) // 2):
            ans += nums[i] * nums[i]
        for i in range((n + 1) // 2, n):
            ans -= nums[i] * nums[i]
        return ans

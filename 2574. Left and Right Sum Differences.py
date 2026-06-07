from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total = sum(nums)
        left = 0
        ans = [0] * n
        for i in range(n):
            ans[i] = abs(total - 2 * left - nums[i])
            left += nums[i]
        return ans

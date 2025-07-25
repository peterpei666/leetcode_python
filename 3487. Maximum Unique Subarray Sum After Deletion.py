from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        if nums[0] <= 0:
            return nums[0]
        ans = nums[0]
        n = len(nums)
        for i in range(1, n):
            if nums[i] <= 0:
                break
            if nums[i] != nums[i - 1]:
                ans += nums[i]
        return ans

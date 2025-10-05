from typing import List

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            ans ^= i
        if ans:
            return len(nums)
        if any(nums[i] > 0 for i in range(len(nums))):
            return len(nums) - 1
        return 0

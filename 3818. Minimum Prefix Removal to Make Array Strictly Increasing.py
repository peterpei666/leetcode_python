from typing import List

class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        n = len(nums) - 1
        while n > 0 and nums[n] > nums[n - 1]:
            n -= 1
        return n

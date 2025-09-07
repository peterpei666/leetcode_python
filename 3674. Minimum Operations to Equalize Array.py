from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                return 1
        return 0

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return [[nums[i] for i in range(len(nums)) if (1 << i) & mask] for mask in range(1 << len(nums))]

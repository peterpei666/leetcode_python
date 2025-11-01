from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        return [list(s) for s in set(tuple(sorted([nums[i] for i in range(len(nums)) if (1 << i) & mask])) for mask in range(1 << len(nums)))]

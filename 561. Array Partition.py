from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(min(nums[i], nums[i + 1]) for i in range(0, len(nums), 2))

from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        return nums[0] == 1 and all(nums[i + 1] == nums[i] + 1 for i in range(len(nums) - 2)) and nums[-1] == len(nums) - 1

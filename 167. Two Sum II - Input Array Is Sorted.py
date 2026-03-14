from typing import List
from bisect import bisect_left

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(len(nums)):
            if 2 * nums[i] > target:
                break
            it = bisect_left(nums, target - nums[i], i + 1)
            if not it == len(nums) and nums[it] + nums[i] == target:
                return [i + 1, it + 1]
        return [-1, -1]

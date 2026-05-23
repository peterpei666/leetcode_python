from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        return (nums[0] < nums[-1]) + sum(nums[i - 1] > nums[i] for i in range(1, len(nums))) <= 1

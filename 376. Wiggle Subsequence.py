from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        p, v = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                p = v + 1
            elif nums[i] < nums[i - 1]:
                v = p + 1
        return max(p, v)

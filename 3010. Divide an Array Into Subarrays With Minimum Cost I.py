from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        m1 = float('inf')
        m2 = float('inf')
        for i in range(1, len(nums)):
            if nums[i] <= m1:
                m2 = m1
                m1 = nums[i]
            elif nums[i] < m2:
                m2 = nums[i]
        return nums[0] + m1 + m2

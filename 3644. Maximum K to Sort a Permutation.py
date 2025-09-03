from typing import List

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        ans = -1
        for i in range(len(nums)):
            if not nums[i] == i:
                ans &= nums[i]
        return ans if not ans == -1 else 0

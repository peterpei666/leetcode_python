from typing import List

class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums.sort(reverse=True)
        ans = []
        ans.append(nums[0])
        if k == 1:
            return ans
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                ans.append(nums[i])
                if len(ans) == k:
                    break
        return ans

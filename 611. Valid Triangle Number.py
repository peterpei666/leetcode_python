from typing import List
import bisect

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                ans += max(bisect.bisect_left(nums, nums[i] + nums[j], j + 1) - bisect.bisect_right(nums, nums[j] - nums[i], j + 1), 0)
        return ans

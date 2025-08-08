from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[l] == nums[r] and nums[l] == nums[mid]:
                l += 1
                r -= 1
                continue
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]

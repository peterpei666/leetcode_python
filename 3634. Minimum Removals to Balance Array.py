from typing import List

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        l, r = 0, n - 1
        while r >= 0 and nums[l] * k < nums[r]:
            r -= 1
        ans = r - l + 1
        l += 1
        while r < n - 1:
            while r < n and nums[r] <= nums[l] * k:
                r += 1
            ans = max(ans, r - l)
            l += 1
        return n - ans

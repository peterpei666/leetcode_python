from typing import List

class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        n = len(nums)
        suf = nums[n - 1]
        ans = 0
        for i in range(n - 2, -1, -1):
            if nums[i] * (n - 1 - i) > suf:
                ans += 1
            suf += nums[i]
        return ans

from typing import List

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        i, sz = 0, len(nums)
        ans = 0
        miss = 1
        while miss <= n:
            if i < sz and miss >= nums[i]:
                miss += nums[i]
                i += 1
            else:
                miss <<= 1
                ans += 1
        return ans

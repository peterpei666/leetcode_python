from typing import List

class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        ans[0] = nums[0]
        for i in range(1, n):
            ans[i] = max(ans[i - 1], nums[i])
        suf = [0] * n
        suf[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suf[i] = min(suf[i + 1], nums[i])
        for i in range(n - 2, -1, -1):
            if ans[i] > suf[i + 1]:
                ans[i] = ans[i + 1]
        return ans

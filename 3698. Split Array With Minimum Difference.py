from typing import List

class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)
        left = [False] * n
        right = [False] * n
        left[0] = True
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                break
            left[i] = True
        right[n - 1] = True
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                break
            right[i] = True
        total = sum(nums)
        pre = 0
        ans = float('inf')
        for i in range(n - 1):
            if not left[i]:
                break
            pre += nums[i]
            if right[i + 1]:
                ans = min(ans, abs(pre - (total - pre)))
        if ans == float('inf'):
            ans = -1
        return ans

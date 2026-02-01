from typing import List

class Solution:
    def longestAlternating(self, nums: List[int]) -> int:
        n = len(nums)
        lu = [1] * n
        ld = [1] * n
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                lu[i] = ld[i - 1] + 1
                ld[i] = 1
            elif nums[i - 1] > nums[i]:
                ld[i] = lu[i - 1] + 1
                lu[i] = 1
            else:
                lu[i] = 1
                ld[i] = 1
        ru = [1] * n
        rd = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                ru[i] = rd[i + 1] + 1
                rd[i] = 1
            elif nums[i] > nums[i + 1]:
                rd[i] = ru[i + 1] + 1
                ru[i] = 1
            else:
                ru[i] = 1
                rd[i] = 1
        ans = max(max(lu), max(ld))
        for i in range(1, n - 1):
            if nums[i - 1] < nums[i + 1]:
                ans = max(ans, ld[i - 1] + rd[i + 1])
            elif nums[i - 1] > nums[i + 1]:
                ans = max(ans, lu[i - 1] + ru[i + 1])
        return ans

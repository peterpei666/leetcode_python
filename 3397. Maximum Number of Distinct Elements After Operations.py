from typing import List

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        temp = float('-inf')
        ans = 0
        for i in sorted(nums):
            if temp < i + k:
                temp = max(temp + 1, i - k)
                ans += 1
        return ans

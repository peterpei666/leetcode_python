from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        temp = 0
        for i in nums:
            temp += i
            ans = max(ans, temp)
            temp = max(0, temp)
        return ans

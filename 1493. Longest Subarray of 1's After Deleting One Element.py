from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        prev, temp = -1, 0
        ans = 0
        i, n = 0, len(nums)
        while i < n:
            while i < n and nums[i] == 1:
                temp += 1
                i += 1
            ans = max(ans, prev + temp)
            if i < n and nums[i] == 0:
                if temp == 0:
                    prev = 0
                else:
                    prev = temp
                    temp = 0
            i += 1
        return ans

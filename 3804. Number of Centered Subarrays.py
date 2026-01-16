from typing import List

class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            mp = set()
            total = 0
            for j in range(i, n):
                mp.add(nums[j])
                total += nums[j]
                if total in mp:
                    ans += 1
        return ans

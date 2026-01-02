from typing import List

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        cnt = [0] * (max(nums) + 1)
        for i in nums:
            cnt[i] += 1
        n = len(nums) // 2
        for i, k in enumerate(cnt):
            if k == n:
                return i
        return -1

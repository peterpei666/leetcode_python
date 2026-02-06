from typing import List

class Solution:
    def minimumK(self, nums: List[int]) -> int:
        l, r = 0, 100000
        while l < r:
            mid = (r - l) // 2 + l
            if (mid == 0):
                break
            cost = sum((i + mid - 1) // mid for i in nums)
            if cost > mid * mid:
                l = mid + 1
            else:
                r = mid
        return 1 if not l else l

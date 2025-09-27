from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        l, r = 0, nums[-1] - nums[0]
        while l < r:
            mid = (l + r) // 2
            cnt = 0
            j = 0
            for i in range(n):
                while j < n and nums[j] - nums[i] <= mid:
                    j += 1
                cnt += j - i - 1
            if (cnt < k):
                l = mid + 1
            else:
                r = mid
        return l    

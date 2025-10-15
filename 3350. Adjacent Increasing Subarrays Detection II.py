from typing import List

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        mp = [0] * n
        mp[0] = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                mp[i] = mp[i - 1] + 1
            else:
                mp[i] = 1
        l, r = 1, n // 2
        ans = 1
        while l <= r:
            mid = (l + r) // 2
            valid = False
            for i in range(n - 2 * mid + 1):
                if mp[i + mid - 1] - mp[i] == mid - 1 and mp[i + 2 * mid - 1] - mp[i + mid] == mid - 1:
                    valid = True
                    break
            if valid:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

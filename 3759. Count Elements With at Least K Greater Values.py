from typing import List

class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        i = 0
        n = len(nums)
        while i < n:
            j = i
            while j + 1 < n and nums[j + 1] == nums[i]:
                j += 1
            if n - j - 1 >= k:
                ans += j - i + 1
            i = j + 1
        return ans

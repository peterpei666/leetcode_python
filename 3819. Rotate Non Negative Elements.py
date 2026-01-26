from typing import List

class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        pos = [nums[i] for i in range(n) if nums[i] >= 0]
        if not pos:
            return nums
        sz = len(pos)
        j = 0
        for i in range(n):
            if nums[i] >= 0:
                nums[i] = pos[(j + k) % sz]
                j += 1
        return nums

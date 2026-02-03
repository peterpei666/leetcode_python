from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        cnt = 1
        l = 0
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                return False
            if cnt & 1:
                if nums[i] > nums[i + 1]:
                    if l == 0:
                        return False
                    cnt += 1
                    l = 0
                l += 1
            else:
                if nums[i] < nums[i + 1]:
                    if l == 0:
                        return False
                    cnt += 1
                    l = 0
                l += 1
        return cnt == 3 and l > 0

from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[i] == 2:
                nums[i] = -1
            else:
                for j in range(31):
                    if (nums[i] & (1 << j)) == 0:
                        nums[i] -= 1 << (j - 1)
                        break
        return nums

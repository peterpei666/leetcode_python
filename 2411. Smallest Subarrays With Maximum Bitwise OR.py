from typing import List

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        target = [0] * n
        target[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            target[i] = nums[i] | target[i + 1]
        bit = [-1] * 32
        ans = [0] * n
        temp, j = nums[0], 1
        for k in range(32):
            if nums[0] < (1 << k):
                break
            if nums[0] & (1 << k):
                bit[k] = 0
        for i in range(n):
            while (j < n and temp < target[i]) or j <= i:
                temp |= nums[j]
                for k in range(32):
                    if nums[j] < (1 << k):
                        break
                    if nums[j] & (1 << k):
                        bit[k] = j
                j += 1
            ans[i] = j - i
            for k in range(32):
                if bit[k] == i:
                    temp -= 1 << k
        return ans

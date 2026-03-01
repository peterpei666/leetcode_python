from typing import List
from collections import defaultdict

class Solution:
    def countSubarrays(self, nums: list[int], k: int, m: int) -> int:
        mp1 = defaultdict(int)
        mp2 = defaultdict(int)
        unique1 = 0
        unique2 = 0
        valid = 0
        n = len(nums)
        l1 = 0
        l2 = 0
        ans = 0
        for i in range(n):
            mp1[nums[i]] += 1
            if mp1[nums[i]] == 1:
                unique1 += 1
            while unique1 > k:
                mp1[nums[l1]] -= 1
                if mp1[nums[l1]] == 0:
                    unique1 -= 1
                l1 += 1
            mp2[nums[i]] += 1
            if mp2[nums[i]] == 1:
                unique2 += 1
            if mp2[nums[i]] == m:
                valid += 1
            while l2 <= i:
                if mp2[nums[l2]] > m:
                    mp2[nums[l2]] -= 1
                    l2 += 1
                elif unique2 > k:
                    if mp2[nums[l2]] == m:
                        valid -= 1
                    mp2[nums[l2]] -= 1
                    if mp2[nums[l2]] == 0:
                        unique2 -= 1
                    l2 += 1
                else:
                    break
            if unique1 == k and unique2 == k and valid == k:
                ans += l2 - l1 + 1
        return ans

from typing import List

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        mp = [False] * len(nums)
        ans = []
        for i in nums:
            if mp[i]:
                ans.append(i)
            else:
                mp[i] = True
        return ans

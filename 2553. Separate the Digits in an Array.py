from typing import List

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums[::-1]:
            while i:
                ans.append(i % 10)
                i //= 10
        return ans[::-1]

from typing import List

class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            temp = num
            while ans and ans[-1] == temp:
                temp *= 2
                ans.pop()
            ans.append(temp)
        return ans

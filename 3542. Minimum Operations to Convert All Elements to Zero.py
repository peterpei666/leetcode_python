from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def check(l: int, r: int) -> int:
            ans = 0
            stk = []
            for i in range(l, r):
                while stk and stk[-1] > nums[i]:
                    stk.pop()
                    ans += 1
                while stk and stk[-1] == nums[i]:
                    stk.pop()
                stk.append(nums[i])
            return ans + len(stk)
        
        ans, l = 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                ans += check(l, i)
                l = i + 1
        return ans + check(l, len(nums))

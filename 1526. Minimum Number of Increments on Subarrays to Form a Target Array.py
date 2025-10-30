from typing import List

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans = 0
        stk = []
        for i in target:
            if stk and stk[-1] >= i:
                ans += stk[-1] - i
            while stk and stk[-1] >= i:
                stk.pop()
            stk.append(i)
        return ans + stk[-1]

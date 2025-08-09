from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        suf = prices[-1]
        ans = 0
        for i in range(len(prices) - 1, -1, -1):
            suf = max(suf, prices[i])
            ans = max(ans, suf - prices[i])
        return ans

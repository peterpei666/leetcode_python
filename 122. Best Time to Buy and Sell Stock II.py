from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur, ans = prices[0], 0
        for p in prices:
            if p > cur:
                ans += p - cur
            cur = p
        return ans

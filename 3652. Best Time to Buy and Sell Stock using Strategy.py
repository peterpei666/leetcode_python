from typing import List

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        ans = 0
        for i in range(n):
            ans += prices[i] * strategy[i]
        temp = 0
        for i in range(k // 2, k):
            temp += prices[i]
        for i in range(k, n):
            temp += prices[i] * strategy[i]
        ans = max(ans, temp)
        for i in range(n - k):
            temp = temp + prices[i] * strategy[i] - prices[i + k // 2] + prices[i + k] * (1 - strategy[i + k])
            ans = max(ans, temp)
        return ans

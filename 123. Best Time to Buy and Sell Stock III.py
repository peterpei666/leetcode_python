from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l = [0] * n
        temp = prices[0]
        for i in range(1, n, 1):
            temp = min(temp, prices[i])
            l[i] = max(l[i - 1], prices[i] - temp)
        r = [0] * n
        temp = prices[-1]
        for i in range(n - 2, -1, -1):
            temp = max(temp, prices[i])
            r[i] = max(r[i + 1], temp - prices[i])
        ans = 0
        for i in range(n):
            ans = max(ans, l[i] + r[i])
        return ans

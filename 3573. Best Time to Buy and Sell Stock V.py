from typing import List

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        res = [0] * (k + 1)
        bought = [float('-inf')] * k
        sold = [0] * k
        for i in range(len(prices)):
            for j in range(k, 0 , -1):
                res[j] = max(res[j], bought[j - 1] + prices[i], sold[j - 1] - prices[i])
                bought[j - 1] = max(bought[j - 1], res[j - 1] - prices[i])
                sold[j - 1] = max(sold[j - 1], res[j - 1] + prices[i])
        return max(res)

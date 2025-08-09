from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        buy = [[0] * n for _ in range(k + 1)]
        profit = [[0] * n for _ in range(k + 1)]
        for i in range(n):
            for t in range(1, k + 1):
                if i > 0:
                    buy[t][i] = max(buy[t][i - 1], profit[t - 1][i - 1] - prices[i])
                else:
                    buy[t][i] = -prices[i]
                if i > 0:
                    profit[t][i] = max(profit[t][i - 1], buy[t][i] + prices[i])
        return profit[-1][-1]

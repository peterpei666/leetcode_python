from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount
        for coin in coins:
            for j in range(coin, amount + 1):
                if dp[j] > 10 ** 10:
                    break
                dp[j] += dp[j - coin]
        return dp[amount]

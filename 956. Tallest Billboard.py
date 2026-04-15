from typing import List

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        n, T = len(rods), sum(rods)
        dp = [-10 ** 9] * (T + 1)
        dp[rods[0]] = rods[0]
        dp[0] = 0
        for i in range(1, n):
            next = dp[:]
            for d in range(T - rods[i]):
                next[d] = max(next[d], dp[d + rods[i]] + rods[i])
                next[d] = max(next[d], dp[abs(d - rods[i])] + rods[i])
            dp = next
        return dp[0] // 2 if dp[0] > 0 else 0

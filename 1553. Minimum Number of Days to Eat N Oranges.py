from collections import defaultdict

class Solution:
    dp = defaultdict(int)

    def __init__(self):
        self.dp[0] = 0
        self.dp[1] = 1
        
    def minDays(self, n: int) -> int:
        if n in self.dp:
            return self.dp[n]
        self.dp[n] = 1 + min(n % 2 + self.minDays(n // 2), n % 3 + self.minDays(n // 3))
        return self.dp[n]

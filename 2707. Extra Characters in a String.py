from typing import List

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        mp = set(dictionary)
        dp = [i for i in range(51)]
        n = len(s)
        for i in range(1, n + 1):
            for j in range(i):
                if s[j:i] in mp:
                    dp[i] = min(dp[i], dp[j])
                    for k in range(i + 1, n + 1):
                        dp[k] = min(dp[k], dp[k - 1] + 1)
        return dp[n]

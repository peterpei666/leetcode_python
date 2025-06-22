class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        n = len(numWays)
        target = [1] + numWays[:]
        dp = [0] * (n + 1)
        ret = []
        dp[0] = 1
        for i in range(1, n + 1):
            if target[i] == dp[i]:
                continue
            if target[i] == dp[i] + 1:
                ret.append(i)
                for j in range(i, n + 1):
                    dp[j] = dp[j] + dp[j - i]
            else:
                return []
        return ret

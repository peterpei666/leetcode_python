class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [False] * n
        dp[0] = True
        cnt = 0
        for i in range(n):
            if i > maxJump:
                cnt -= dp[i - maxJump - 1]
            if i >= minJump:
                cnt += dp[i - minJump]
            if cnt > 0 and s[i] == '0':
                dp[i] = True
        return dp[-1]

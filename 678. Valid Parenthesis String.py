class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        dp = [[False] * 101 for _ in range(2)]
        if s[0] == '(':
            dp[0][1] = True
        elif s[0] == ')':
            return False
        else:
            dp[0][0] = True
            dp[0][1] = True
        for i in range(1, n):
            mask = i & 1
            prev = mask ^ 1
            if s[i] == '(':
                dp[mask][1:] = dp[prev][:-1]
                dp[mask][0] = False
            elif s[i] == ')':
                dp[mask][:-1] = dp[prev][1:]
                dp[mask][100] = False
            else:
                dp[mask] = dp[prev][:]
                dp[mask][1] |= dp[prev][0]
                for j in range(1, 100):
                    dp[mask][j - 1] |= dp[prev][j]
                    dp[mask][j + 1] |= dp[prev][j]
        return dp[(n - 1) & 1][0]

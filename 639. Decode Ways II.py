class Solution:
    def numDecodings(self, s: str) -> int:
        def one(c: str) -> int:
            if c == '*':
                return 9
            if c == '0':
                return 0
            return 1
        
        def two(c1: str, c2: str) -> int:
            if c1 == '*':
                if c2 == '*':
                    return 15
                if ord(c2) <= ord('6'):
                    return 2
                return 1
            if c1 == '1':
                return 9 if c2 == '*' else 1
            if c1 == '2':
                if c2 == '*':
                    return 6
                return 1 if ord(c2) <= ord('6') else 0
            return 0
        
        mod = 10 ** 9 + 7
        dp = [0] * 3
        n = len(s)
        dp[(n - 1) % 3] = one(s[n - 1])
        if n > 1:
            dp[(n - 2) % 3] = one(s[n - 2]) * dp[(n - 1) % 3] + two(s[n - 2], s[n - 1])
            for i in range(n - 3, -1, -1):
                dp[i % 3] = (one(s[i]) * dp[(i + 1) % 3] + two(s[i], s[i + 1]) * dp[(i + 2) % 3]) % mod
        return dp[0]

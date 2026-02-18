class Solution:
    def almostPalindromic(self, s: str) -> int:
        n = len(s)
        dp = [[-1] * (n + 1) for _ in range(n + 1)]
        
        def find(l: int, r: int) -> int:
            if l >= r:
                return 0
            if dp[l][r] != -1:
                return dp[l][r]
            if s[l] == s[r]:
                dp[l][r] = find(l + 1, r - 1)
            else:
                dp[l][r] = 1 + min(find(l + 1, r), find(l, r - 1))
            return dp[l][r]
        
        ans = 1
        for i in range(n):
            for j in range(i + ans, n):
                if find(i, j) <= 1:
                    ans = j - i + 1
        return ans

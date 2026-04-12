class Solution:
    def dis(self, a, b):
        return abs(a % 6 - b % 6) + abs(a // 6 - b // 6)
    
    def minimumDistance(self, word):
        n = len(word)
        dp = [[[0 for _ in range(26)] for _ in range(26)] for _ in range(2)]
        for i in range(n):
            mask = i & 1
            next_mask = mask ^ 1
            t = ord(word[i]) - ord('A')
            dp[next_mask] = [[float('inf') for _ in range(26)] for _ in range(26)]
            for a in range(26):
                for b in range(26):
                    dp[next_mask][a][t] = min(dp[next_mask][a][t], dp[mask][a][b] + self.dis(b, t))
                    dp[next_mask][t][b] = min(dp[next_mask][t][b], dp[mask][a][b] + self.dis(a, t))
        ans = float('inf')
        mask = n & 1
        for a in range(26):
            for b in range(26):
                ans = min(ans, dp[mask][a][b])
        return ans

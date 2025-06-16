class Solution:
    def getmask(x: int) -> int:
        mask = 0
        for i in range(3):
            mask |= 1 << (3 * i + x % 3)
            x //= 3
        return mask
    
    def valid(mask: int) -> bool:
        return not ((mask & (mask>>3)) or (mask & (mask<<3)))
    
    def valid_pair(mask1: int, mask2: int) -> bool:
        return not (mask1 & mask2)
    
    def numOfWays(self, n: int) -> int:
        mod = 10**9 + 7
        masks = [0] * 27
        for i in range(27):
            masks[i] = Solution.getmask(i)
            if not Solution.valid(masks[i]):
                masks[i] = 0
        adj = [0] * 27
        for i in range(27):
            if masks[i]:
                for j in range(27):
                    if masks[j] and Solution.valid_pair(masks[i], masks[j]):
                        adj[i] |= 1 << j
        dp = [[0] * 27 for _ in range(n + 1)] * 2
        for i in range(27):
            if masks[i]:
                dp[0][i] = 1
        for i in range(1, n):
            for j in range(27):
                dp[i % 2][j] = 0
                for k in range(27):
                    if adj[k] & (1 << j):
                        dp[i % 2][j] = (dp[i % 2][j] + dp[(i - 1) % 2][k]) % mod
        ans = 0
        for i in range(27):
            ans = (ans + dp[(n - 1) % 2][i]) % mod
        return ans
                
        

class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        n = len(nums)
        dp = [[[-1] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]
        def dfs(i, r1, r2):
            if i == n:
                return 0
            if dp[i][r1][r2] != -1:
                return dp[i][r1][r2]
            res = nums[i] + dfs(i + 1, r1, r2)
            if r1 > 0:
                res = min(res, (nums[i] + 1) // 2 + dfs(i + 1, r1 - 1, r2))
            if r2 > 0 and nums[i] >= k:
                res = min(res, nums[i] - k + dfs(i + 1, r1, r2 - 1))
            if r1 > 0 and r2 > 0 and (nums[i] + 1) // 2 >= k:
                res = min(res, (nums[i] + 1) // 2 - k + dfs(i + 1, r1 - 1, r2 - 1))
            if r1 > 0 and r2 > 0 and nums[i] >= k:
                res = min(res, (nums[i] - k + 1) // 2 + dfs(i + 1, r1 - 1, r2 - 1))
            dp[i][r1][r2] = res
            return res
        
        return dfs(0, op1, op2)

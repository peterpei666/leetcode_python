class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]
        for num in nums:
            num %= k
            for i in range(k):
                dp[i][num] = dp[num][i] + 1
        return max([max(dp[i]) for i in range(k)])

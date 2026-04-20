from typing import List

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(2)]
        ans = 0
        for i in range(m - 1, -1, -1):
            mask = i & 1
            prev = mask ^ 1
            dp[mask] = [0] * (n + 1)
            for j in range(n - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[mask][j] = dp[prev][j + 1] + 1
                else:
                    dp[mask][j] = 0
            ans = max(ans, max(dp[mask]))
        return ans

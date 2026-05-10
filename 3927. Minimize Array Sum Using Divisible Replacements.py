from collections import Counter

class Solution:
    def minArraySum(self, nums: list[int]) -> int:
        m = max(nums)
        cnt = [0] * (m + 1)
        for x in nums:
            cnt[x] += 1
        ans = 0
        for x in range(m + 1):
            if cnt[x]:
                for t in range(x, m + 1, x):
                    if cnt[t]:
                        ans += cnt[t] * x
                        cnt[t] = 0
        return ans

from typing import List

class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        nums.sort()
        n = len(nums)
        sum = [False] * (k + 1)
        sum[0] = True
        ans = [False] * n
        for x in range(1, n + 1):
            i = 0
            while i < n and nums[i] < x:
                for j in range(k, nums[i] - 1, -1):
                    if sum[j - nums[i]]:
                        sum[j] = True
                i += 1
            bigger = n - i
            for j in range(bigger + 1):
                if j * x > k:
                    break
                if sum[k - j * x]:
                    ans[x - 1] = True
                    break
        return ans

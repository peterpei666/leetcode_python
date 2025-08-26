from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = max(nums)
        pre = [0] * n
        pre[0] = nums[0]
        for i in range(1, n):
            pre[i] = pre[i - 1] + nums[i]
        r = pre[-1]
        while l < r:
            mid = (l + r) // 2
            cnt, prev = 1, 0
            for i in range(n):
                if pre[i] - prev > mid:
                    cnt += 1
                    prev = pre[i - 1]
            if cnt > k:
                l = mid + 1
            else:
                r = mid
        return l

from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = 0
        for i in nums:
            if i == 1:
                cnt += 1
        if cnt:
            return len(nums) - cnt
        ans = float('inf')
        n = len(nums)
        for i in range(n):
            cur = nums[i]
            j = i + 1
            while j < n and not cur == 1:
                cur = gcd(cur, nums[j])
                j += 1
            if cur == 1:
                ans = min(ans, j - i)
        if ans == float('inf'):
            return -1
        return n + int(ans) - 2

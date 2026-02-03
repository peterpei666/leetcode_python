from typing import List

class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float('-inf')
        i = 0
        while i < n:
            j = i + 1
            res = 0
            while j < n and nums[j - 1] < nums[j]:
                j += 1
            p = j - 1
            if p == i:
                i += 1
                continue
            res += nums[p] + nums[p - 1]
            while j < n and nums[j - 1] > nums[j]:
                res += nums[j]
                j += 1
            q = j - 1
            if q == p or q == n - 1 or (j < n and nums[j] <= nums[q]):
                i = q + 1
                continue
            res += nums[q + 1]
            max_sum = 0
            sum_val = 0
            k = q + 2
            while k < n and nums[k] > nums[k - 1]:
                sum_val += nums[k]
                max_sum = max(max_sum, sum_val)
                k += 1
            res += max_sum
            max_sum = 0
            sum_val = 0
            k = p - 2
            while k >= i:
                sum_val += nums[k]
                max_sum = max(max_sum, sum_val)
                k -= 1
            res += max_sum
            ans = max(ans, res)
            i = q
        return ans

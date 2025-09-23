from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        sum = [0] * (n - k + 1)
        left = [0] * (n - k + 1)
        right = [0] * (n - k + 1)
        temp = 0
        for i in range(k):
            temp += nums[i]
        sum[0] = temp
        for i in range(k, n):
            temp = temp + nums[i] - nums[i - k]
            sum[i - k + 1] = temp
        for i in range(1, n - k + 1):
            if sum[i] > sum[left[i - 1]]:
                left[i] = i
            else:
                left[i] = left[i - 1]
        right[-1] = n - k
        for i in range(n - k - 1, -1, -1):
            if sum[i] >= sum[right[i + 1]]:
                right[i] = i
            else:
                right[i] = right[i + 1]
        temp = 0
        ans = []
        for i in range(k, n - 2 * k + 1):
            if sum[left[i - k]] + sum[i] + sum[right[i + k]] > temp:
                temp = sum[left[i - k]] + sum[i] + sum[right[i + k]]
                ans = [left[i - k], i, right[i + k]]
        return ans

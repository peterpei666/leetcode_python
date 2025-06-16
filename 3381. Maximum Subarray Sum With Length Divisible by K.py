class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0] * k
        sum = 0
        for i in range(k):
            sum += nums[i]
            prefix[i] = sum
        ans = sum
        prefix[-1] = min(prefix[-1], 0)
        for i in range(k, len(nums)):
            sum += nums[i]
            ans = max(ans, sum - prefix[i % k])
            prefix[i % k] = min(sum, prefix[i % k])
        return ans

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = min(prefix[i - 1], nums[i])
        suffix = [0] * n
        suffix[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix[i] = min(suffix[i + 1], nums[i])
        ans = float('inf')
        for i in range(n):
            if nums[i] > prefix[i] and nums[i] > suffix[i]:
                ans = min(ans, nums[i] + prefix[i] + suffix[i])
        return ans if ans != float('inf') else -1

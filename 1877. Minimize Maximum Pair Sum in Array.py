class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        nums.sort()
        ans = 0
        while l < r:
            ans = max(ans, nums[l] + nums[r])
            l += 1
            r -= 1
        return ans

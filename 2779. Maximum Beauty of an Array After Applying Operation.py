class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, j = 0, 0
        ans = 0
        n = len(nums)
        for i in range(n):
            while j < n and nums[j] <= nums[i] + 2 * k:
                j += 1
            ans = max(ans, j - i)
            if j == n:
                break
        return ans

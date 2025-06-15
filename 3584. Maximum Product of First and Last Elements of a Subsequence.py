class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        n = len(nums)
        surmin = [0] * n
        surmax = [0] * n
        surmin[-1] = nums[-1]
        surmax[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            surmin[i] = min(surmin[i + 1], nums[i])
            surmax[i] = max(surmax[i + 1], nums[i])
        ans = float('-inf')
        for i in range(n):
            if i + m - 1 < n:
                ans = max(ans, nums[i] * surmin[i + m - 1])
                ans = max(ans, nums[i] * surmax[i + m - 1])
        return ans

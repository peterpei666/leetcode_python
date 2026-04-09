class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 1000
        for i in range(n):
            if not nums[i] == 1:
                continue
            for j in range(n):
                if nums[j] == 2:
                    ans = min(ans, abs(i - j))
        return -1 if ans == 1000 else ans

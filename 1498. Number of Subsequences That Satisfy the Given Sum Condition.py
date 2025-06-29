class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        mod = 10 ** 9 + 7
        power = [1] * n
        for i in range(1, n):
            power[i] = power[i - 1] * 2 % mod
        l, r = 0, n - 1
        ans = 0
        while l <= r:
            if nums[l] + nums[r] <= target:
                ans = (ans + power[r - l]) % mod
                l += 1
            else:
                r -= 1
        return ans

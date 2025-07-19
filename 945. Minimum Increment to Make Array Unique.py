class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        sum, cur = 0, nums[0]
        for i in range(1, n):
            if nums[i] < cur + 1:
                sum += cur + 1 - nums[i]
                cur += 1
            else:
                cur = nums[i]
        return sum

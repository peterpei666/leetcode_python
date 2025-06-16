class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        if not nums:
            return -1
        min_num = nums[0]
        max_diff = -1
        for num in nums[1:]:
            if num > min_num:
                max_diff = max(max_diff, num - min_num)
            else:
                min_num = num
        return max_diff

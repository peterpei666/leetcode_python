class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        list = [False] * (n + 1)
        list[0] = True
        for i in range(2, n + 1):
            if nums[i - 1] == nums[i - 2] and list[i - 2]:
                list[i] = True
            if i > 2 and nums[i - 1] == nums[i - 2] == nums[i - 3] and list[i - 3]:
                list[i] = True
            if i > 2 and nums[i - 1] == nums[i - 2] + 1 == nums[i - 3] + 2 and list[i - 3]:
                list[i] = True
        return list[n]

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        temp1 = nums[-1]
        temp2 = nums[0]
        l = -1
        r = -2
        for i in range(n):
            temp1 = min(temp1, nums[n - 1 - i])
            if nums[n - 1 - i] > temp1:
                l = n - 1 - i
            temp2 = max(temp2, nums[i])
            if nums[i] < temp2:
                r = i
        return r - l + 1 

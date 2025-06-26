class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        m = len(nums)
        n = len(nums[0])
        for i in range(m):
            nums[i].sort()
        sum = 0
        for i in range(n):
            temp = 0
            for j in range(m):
                temp = max(temp, nums[j][i])
            sum += temp
        return sum

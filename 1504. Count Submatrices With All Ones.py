class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = []
        for i in range(0, n, 3):
            if nums[i + 2] - nums[i] > k:
                result.clear()
                return result
            else:
                result.append([nums[i], nums[i + 1], nums[i + 2]])
        return result

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        total = sum(nums)
        temp = 0
        ans = 0
        for i in range(len(nums)):
            temp += nums[i]
            if nums[i] == 0:
                if abs(total - 2 * temp) == 1:
                    ans += 1
                elif total == 2 * temp:
                    ans += 2
        return ans

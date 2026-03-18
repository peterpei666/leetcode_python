from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        def make_range(l: int, r: int) -> str:
            return str(l) if l == r else str(l) + '->' + str(r)
        
        if not nums:
            return []
        ans = []
        l, r = nums[0], nums[0]
        for i in range(1, len(nums)):
            if not nums[i] == r + 1:
                ans.append(make_range(l, r))
                l = nums[i]
                r = nums[i]
            else:
                r += 1
        ans.append(make_range(l, r))
        return ans

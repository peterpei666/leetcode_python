from typing import List

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for l in range(n):
            mp = set()
            odd_cnt = 0
            even_cnt = 0
            for r in range(l, n):
                if nums[r] & 1:
                    if nums[r] not in mp:
                        odd_cnt += 1
                        mp.add(nums[r])
                else:
                    if nums[r] not in mp:
                        even_cnt += 1
                        mp.add(nums[r])
                if odd_cnt == even_cnt:
                    ans = max(ans, r - l + 1)
        return ans

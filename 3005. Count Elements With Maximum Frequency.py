from typing import List

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt = [0] * 101
        for x in nums:
            cnt[x] += 1
        temp = max(cnt)
        return sum(x if x == temp else 0 for x in cnt)

from typing import List

class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        freq = [0] * 100001
        cnt = [0] * 100001
        for i in nums:
            freq[i] += 1
        for i in range(1, 100001):
            cnt[freq[i]] += 1
        for i in nums:
            if cnt[freq[i]] == 1:
                return i
        return -1

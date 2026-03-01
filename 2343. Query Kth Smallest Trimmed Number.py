from typing import List

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        m = len(nums[0])
        n = len(nums)
        memo = []
        mp = [(nums[i], i) for i in range(n)]
        for i in range(1, m + 1):
            mp.sort(key=lambda x: x[0][m - i])
            memo.append([idx for _, idx in mp])
        return [memo[i - 1][k - 1] for k, i in queries]

from collections import defaultdict

class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        mp = defaultdict(list[int])
        for i in range(len(nums)):
            mp[nums[i]].append(i)
        ans = 0
        for key in mp:
            idx = mp[key]
            j = 0
            n = len(idx)
            for i in range(n):
                while j < n and idx[j] - idx[i] - j + i <= k:
                    j += 1
                    ans = max(ans, j - i)
        return ans

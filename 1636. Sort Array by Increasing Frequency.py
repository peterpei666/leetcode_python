from collections import defaultdict

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        mp = defaultdict(int)
        for i in nums:
            mp[i] += 1
        return sorted(nums, key=lambda x: (mp[x], -x))

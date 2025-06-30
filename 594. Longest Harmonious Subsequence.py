from collections import defaultdict

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        for i in nums:
            mp[i] += 1
        ans = 0
        for key in mp:
            if key + 1 in mp:
                ans = max(ans, mp[key] + mp[key + 1])
        return ans

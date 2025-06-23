from collections import defaultdict

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        mp = defaultdict(int)
        for interval in intervals:
            mp[interval[0]] += 1
            mp[interval[1] + 1] -= 1
        ans = 0
        temp = 0
        for key in sorted(mp.keys()):
            temp += mp[key]
            ans = max(ans, temp)
        return ans

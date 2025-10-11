from collections import defaultdict
from typing import List

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        mp = defaultdict(int)
        for p in power:
            mp[p] += 1
        vec = [(float('-inf'), 0)]
        for p, cnt in mp.items():
            vec.append((p, cnt))
        vec.sort()
        n = len(vec)
        dp = [0] * n
        temp = 0
        j = 1
        for i in range(1, n):
            while j < i and vec[j][0] < vec[i][0] - 2:
                temp = max(temp, dp[j])
                j += 1
            dp[i] = temp + vec[i][0] * vec[i][1]
        ans = 0
        return max(dp)

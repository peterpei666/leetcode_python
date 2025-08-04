from typing import List
from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        mp = defaultdict(int)
        ans = 0
        l = 0
        for r in range(len(fruits)):
            mp[fruits[r]] += 1
            while len(mp) > 2:
                mp[fruits[l]] -= 1
                if mp[fruits[l]] == 0:
                    del mp[fruits[l]]
                l += 1
            ans = max(ans, r - l + 1)
        return ans

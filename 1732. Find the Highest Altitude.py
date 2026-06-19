from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans, cur = 0, 0
        for i in gain:
            cur += i
            ans = max(ans, cur)
        return ans

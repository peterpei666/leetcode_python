from typing import List
import bisect

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        m, n = len(potions), len(spells)
        ans = [0] * n
        potions.sort()
        for i in range(n):
            if success % spells[i]:
                target = success // spells[i] + 1
            else:
                target = success // spells[i]
            if target > potions[-1]:
                ans[i] = 0
                continue
            ans[i] = m - bisect.bisect_left(potions, target)
        return ans

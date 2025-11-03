from typing import List

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        ans = 0
        i = 0
        while i < n:
            c = colors[i]
            total, t = neededTime[i], neededTime[i]
            i += 1
            while i < n and colors[i] == c:
                total += neededTime[i]
                t = max(t, neededTime[i])
                i += 1
            ans += total - t
        return ans

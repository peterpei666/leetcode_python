from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        if not colors[0] == colors[n - 1]:
            return n - 1
        c = colors[0]
        for i in range(1, n - 1):
            if not colors[i] == c or not colors[n - 1 - i] == c:
                return n - 1 - i
        return -1

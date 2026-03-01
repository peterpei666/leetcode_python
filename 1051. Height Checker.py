from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        temp = sorted(heights[:])
        return sum(1 for i in range(len(heights)) if not temp[i] == heights[i])

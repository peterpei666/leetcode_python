from typing import List

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        total = sum(apple)
        ans = 0
        while total > 0:
            total -= capacity[ans]
            ans += 1
        return ans

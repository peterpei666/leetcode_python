from typing import List

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort(reverse=True)
        extra = sum(batteries[n:])
        for i in range(n - 1, 0, -1):
            if extra >= (batteries[i - 1] - batteries[i]) * (n - i):
                extra -= (batteries[i - 1] - batteries[i]) * (n - i)
            else:
                return batteries[i] + extra // (n - i)
        return batteries[0] + extra // n

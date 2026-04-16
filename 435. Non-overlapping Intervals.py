from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda x : x[1])
        cnt = 0
        cur = intervals[0][1]
        for i in range(1, n):
            l, r = intervals[i]
            if l < cur:
                cnt += 1
            else:
                cur = r
        return cnt

from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: (interval[1], -interval[0]))
        temp = []
        for interval in intervals:
            cnt = 0
            for i in temp:
                if interval[0] <= i <= interval[1]:
                    cnt += 1
                    if cnt == 2:
                        break
            for i in range(interval[1], -1, -1):
                if cnt == 2:
                    break
                cnt += 1
                temp.append(i)
        return len(temp)

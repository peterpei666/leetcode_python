from typing import List

class SummaryRanges:
    def __init__(self):
        self.mp = [False] * 10001
        self.l = 10001
        self.r = 0

    def addNum(self, value: int) -> None:
        self.mp[value] = True
        self.l = min(self.l, value)
        self.r = max(self.r, value)

    def getIntervals(self) -> List[List[int]]:
        ans = []
        i = self.l
        while i <= self.r:
            if self.mp[i]:
                temp = [i]
                while i <= self.r and self.mp[i]:
                    i += 1
                temp += [i - 1]
                ans.append(temp)
            i += 1
        return ans

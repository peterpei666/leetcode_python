from typing import List

class Solution:
    def __init__(self):
        self.ans = [[] for _ in range(11)]
        bit = [bin(x).count("1") for x in range(60)]
        for i in range(11):
            for h in range(12):
                rem = i - bit[h]
                if rem >= 0:
                    for m in range(10):
                        if rem == bit[m]:
                            self.ans[i].append(str(h) + ":0" + str(m))
                    for m in range(10, 60):
                        if rem == bit[m]:
                            self.ans[i].append(str(h) + ":" + str(m))

    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        return self.ans[turnedOn]

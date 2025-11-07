from typing import List

class Solution:
    def getRow(self, n: int) -> List[int]:
        ans = []
        for i in range(1, n + 2):
            temp = [0] * i
            temp[0] = 1
            temp[i - 1] = 1
            for j in range(1, i - 1):
                temp[j] = ans[j - 1] + ans[j]
            ans = temp[:]
        return ans

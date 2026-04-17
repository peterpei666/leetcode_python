from typing import List

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
        ptn = [i - 1 if i & 1 else i + 1 for i in range(n)]
        pos = [0] * n
        for i in range(n):
            pos[row[i]] = i
        ans = 0
        for i in range(n):
            j = ptn[pos[ptn[row[i]]]]
            while not i == j:
                row[i], row[j] = row[j], row[i]
                pos[row[i]], pos[row[j]] = pos[row[j]], pos[row[i]]
                ans += 1
                j = ptn[pos[ptn[row[i]]]]
        return ans

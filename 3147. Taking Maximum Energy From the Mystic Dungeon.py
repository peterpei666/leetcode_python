from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        ans = float('-inf')
        for i in range(n - k, n):
            temp = 0
            for j in range(i, -1, -k):
                temp += energy[j]
                ans = max(ans, temp)
        return ans

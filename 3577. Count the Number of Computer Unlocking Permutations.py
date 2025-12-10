from typing import List

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)
        ans = 1
        mod = 10 ** 9 + 7
        for i in range(1, n):
            if complexity[i] <= complexity[0]:
                return 0
            ans = (ans * i) % mod
        return ans

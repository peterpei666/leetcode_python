import itertools

class Solution:
    def findMinimumTime(self, strength: List[int], k: int) -> int:
        permu = list(itertools.permutations(strength))
        ans = float('inf')
        for p in permu:
            t = 0
            temp = 1
            for i in p:
                t += (i + temp - 1) // temp
                temp += k
            ans = min(ans, t)
        return ans

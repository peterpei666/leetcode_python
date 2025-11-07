from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        r, ans = 0, 0
        for i in range(len(gas)):
            r += gas[i] - cost[i]
            if r < 0:
                ans = i + 1
                r = 0
        return ans

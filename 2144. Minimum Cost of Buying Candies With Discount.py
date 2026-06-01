from typing import List

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        return sum(cost[i] if not i % 3 == 2 else 0 for i in range(len(cost)))

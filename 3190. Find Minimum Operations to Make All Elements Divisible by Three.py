from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(1 if not i % 3 == 0 else 0 for i in nums)

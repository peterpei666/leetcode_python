from typing import List
import random
from collections import defaultdict

class Solution:
    def __init__(self, nums: List[int]):
        self.mp = defaultdict(list)
        random.seed(47)
        for i in range(len(nums)):
            self.mp[nums[i]].append(i)

    def pick(self, target: int) -> int:
        n = len(self.mp[target])
        return self.mp[target][random.randint(0, n - 1)]

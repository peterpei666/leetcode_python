from typing import List
from collections import defaultdict
from random import randint

class RandomizedCollection:
    def __init__(self):
        self.nums = []
        self.pos = []
        self.mp = defaultdict(list)

    def insert(self, val: int) -> bool:
        ans = not self.mp[val]
        self.nums.append(val)
        self.mp[val].append(len(self.nums) - 1)
        self.pos.append(len(self.mp[val]) - 1)
        return ans

    def remove(self, val: int) -> bool:
        if not self.mp[val]:
            return False
        target = self.mp[val][-1]
        self.mp[val].pop()
        last = len(self.nums) - 1
        if not target == last:
            val = self.nums[last]
            self.nums[target] = val
            idx = self.pos[last]
            self.mp[val][idx] = target
            self.pos[target] = idx
        self.nums.pop()
        self.pos.pop()
        return True
    
    def getRandom(self) -> int:
        return self.nums[randint(0, len(self.nums) - 1)]

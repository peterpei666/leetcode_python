from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        find = set()
        for i in nums:
            if i in find:
                return True
            find.add(i)
        return False

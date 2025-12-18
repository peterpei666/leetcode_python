from typing import List

class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        def func(x: int) -> int:
            b = []
            while x:
                b.append(x & 1)
                x >>= 1
            ans = 0
            for d in b:
                ans = (ans << 1) + d
            return ans

        nums.sort(key=lambda x: (func(x), x))
        return nums

from typing import List

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        tree = [0] * 2005
        MAX = 2002

        def update(x: int) -> None:
            while x < MAX:
                tree[x] += 1
                x += x & -x
        
        def query(x: int) -> int:
            ans = 0
            while x > 0:
                ans += tree[x]
                x -= x & -x
            return ans
        
        update(1001)
        ans = 0
        cur = 0
        for i in nums:
            if i == target:
                cur += 1
            else:
                cur -= 1
            ans += query(cur - 1 + 1001)
            update(cur + 1001)
        return ans

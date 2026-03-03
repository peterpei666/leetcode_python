from typing import List

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        tree = [0] * 50005
        MAX = 50001

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
        
        n = len(nums1)
        ans = 0
        for i in range(n):
            t = nums1[i] - nums2[i] + 20001
            ans += query(t + diff)
            update(t)
        return ans

from typing import List

class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        ans = n
        mp = dict()
        mp[tuple(nums1)] = 0
        
        def dfs(temp: List[int], cur: int) -> None:
            nonlocal ans
            if temp == nums2:
                ans = min(ans, cur)
                return
            if cur >= ans:
                return
            for l in range(n):
                for r in range(l, n):
                    sub = temp[l:r+1]
                    rest = temp[:l] + temp[r+1:]
                    for i in range(len(rest) + 1):
                        next = rest[:i] + sub + rest[i:]
                        if not tuple(next) in mp or mp[tuple(next)] > cur + 1:
                            mp[tuple(next)] = cur + 1
                            dfs(next, cur + 1)
            
        dfs(nums1, 0)
        return ans

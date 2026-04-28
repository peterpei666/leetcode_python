from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []
        for row in grid:
            arr += row
        arr.sort()
        n = len(arr)
        tar = arr[n // 2]
        ans = 0
        for i in arr:
            if not i % x == tar % x:
                return -1
            ans += abs(tar - i) // x
        return ans

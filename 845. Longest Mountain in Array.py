from typing import List

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        pre = [0] * n
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                pre[i] = pre[i - 1] + 1
        suf = [0] * n
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                suf[i] = suf[i + 1] + 1
        ans = 0
        for i in range(1, n - 1):
            if pre[i] and suf[i]:
                ans = max(ans, pre[i] + suf[i] + 1)
        return ans

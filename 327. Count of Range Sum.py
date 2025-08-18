from typing import List

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        ans = 0

        def merge(l: int, mid: int, r: int) -> None:
            nonlocal pre
            temp = pre[l:r + 1]
            i, j = l, mid + 1
            idx = l
            while i <= mid and j <= r:
                if temp[i - l] < temp[j - l]:
                    pre[idx] = temp[i - l]
                    i += 1
                else:
                    pre[idx] = temp[j - l]
                    j += 1
                idx += 1
            while i <= mid:
                pre[idx] = temp[i - l]
                i += 1
                idx += 1
        
        def merge_sort(l: int, r: int) -> None:
            nonlocal ans
            if l >= r:
                return
            mid = (l + r) // 2
            merge_sort(l, mid)
            merge_sort(mid + 1, r)
            i, j = mid + 1, mid + 1
            for k in range(l, mid + 1):
                while i <= r and pre[i] - pre[k] < lower:
                    i += 1
                while j <= r and pre[j] - pre[k] <= upper:
                    j += 1
                ans += j - i
            merge(l, mid, r)

        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]
        merge_sort(0, n)
        return ans

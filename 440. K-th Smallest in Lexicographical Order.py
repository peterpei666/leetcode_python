class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count(n: int, pre1: int, pre2: int) -> int:
            step = 0
            while pre1 <= n:
                step += min(n + 1, pre2) - pre1
                pre1 *= 10
                pre2 *= 10
            return step
        cur = 1
        k -= 1
        while k > 0:
            step = count(n, cur, cur + 1)
            if step <= k:
                k -= step
                cur += 1
            else:
                k -= 1
                cur *= 10
        return cur

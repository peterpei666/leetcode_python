class Solution:
    def minXor(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def valid(limit: int) -> bool:
            memo = [0] * (n + 1)
            for i in range(n):
                temp = 0
                for j in range(i, n):
                    temp ^= nums[j]
                    if temp <= limit:
                        memo[i] |= 1 << (j + 1)
            cur = 1
            for m in range(k):
                next = 0
                for i in range(n + 1):
                    if cur & (1 << i):
                        next |= memo[i]
                if next == 0:
                    return False
                cur = next
            return True if cur & (1 << n) else False

        l, r = 0, 0
        for i in nums:
            r |= i
        while l < r:
            mid = (r - l) // 2 + l
            if valid(mid):
                r = mid
            else:
                l = mid + 1
        return l

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, 10 ** 9
        while l < r:
            mid = (r - l) // 2 + l
            if sum((p + mid - 1) // mid for p in piles) > h:
                l = mid + 1
            else:
                r = mid
        return l

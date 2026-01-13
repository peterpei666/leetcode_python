from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total = sum(sq[2] ** 2 for sq in squares)
        l, r = 0.0, 10.0 ** 10
        while r - l > 0.00001:
            mid = (l + r) / 2
            if sum(sq[2] * max(0, min(mid - sq[1], sq[2])) for sq in squares) >= total / 2:
                r = mid
            else:
                l = mid
        return r

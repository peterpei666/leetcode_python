from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        neg = 0
        min_abs = float('inf')
        for r in matrix:
            for val in r:
                if val < 0:
                    neg += 1
                total += abs(val)
                min_abs = min(min_abs, abs(val))
        if neg % 2 == 1:
            return total - 2 * min_abs
        return total

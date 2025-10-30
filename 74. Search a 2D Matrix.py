from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m - 1
        while l < r:
            mid = (l + r + 1) // 2
            if matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid
        k = l
        l, r = 0, n - 1
        while l < r:
            mid = (l + r + 1) // 2
            if matrix[k][mid] > target:
                r = mid - 1
            else:
                l = mid
        return matrix[k][l] == target

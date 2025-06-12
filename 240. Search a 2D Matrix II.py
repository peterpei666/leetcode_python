import bisect

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            bisect_index = bisect.bisect_left(matrix[i], target)
            if bisect_index < cols and matrix[i][bisect_index] == target:
                return True
        return False

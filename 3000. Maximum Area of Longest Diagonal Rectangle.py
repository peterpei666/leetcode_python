from typing import List

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        n = len(dimensions)
        ans = dimensions[0][0] * dimensions[0][1]
        dia = dimensions[0][0] * dimensions[0][0] + dimensions[0][1] * dimensions[0][1]
        for i in range(1, n):
            temp = dimensions[i][0] * dimensions[i][0] + dimensions[i][1] * dimensions[i][1]
            if dia == temp:
                ans = max(ans, dimensions[i][0] * dimensions[i][1])
            elif dia < temp:
                dia = temp
                ans = dimensions[i][0] * dimensions[i][1]
        return ans

from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        c = len(matrix[0])
        height = [0] * (c + 1)
        ans = 0
        for row in matrix:
            for i in range(c):
                if row[i] == '1':
                    height[i] += 1
                else:
                    height[i] = 0
            stk = [-1]
            for i in range(c + 1):
                while stk[-1] != -1 and height[i] <= height[stk[-1]]:
                    h = height[stk.pop()]
                    w = i - stk[-1] - 1
                    ans = max(ans, w * h)
                stk.append(i)
        return ans

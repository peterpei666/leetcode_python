class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        return [sum(mp) for mp in matrix]

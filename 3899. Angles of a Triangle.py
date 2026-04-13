from math import acos, pi

class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:
        a, b, c = sides
        if not (a + b > c and a + c > b and b + c > a):
            return []
        a1 = acos((a * a + b * b - c * c) / (2 * a * b)) / pi * 180
        a2 = acos((c * c + b * b - a * a) / (2 * c * b)) / pi * 180
        a3 = acos((a * a + c * c - b * b) / (2 * a * c)) / pi * 180
        return sorted([a1, a2, a3])

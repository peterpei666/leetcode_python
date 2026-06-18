class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        a = hour * 30 + minutes / 2
        b = minutes * 6
        return min(abs(a - b), 360 - abs(a - b))

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if not low & 1:
            low += 1
        return (high - low + 2) // 2

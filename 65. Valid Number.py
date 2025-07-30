class Solution:
    def isNumber(self, s: str) -> bool:
        for char in "abcdfghijklmnopqrstuvwxyz":
            if char in s:
                return False
        try:
            s = float(s)
        except:
            return False
        return True

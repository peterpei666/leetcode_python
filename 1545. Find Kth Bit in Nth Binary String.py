class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        k = k - 1
        while len(s) <= k:
            s = s + "1" + "".join("0" if c == "1" else "1" for c in reversed(s))
        return s[k]

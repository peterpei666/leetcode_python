from typing import List

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i, n = 0, len(bits)
        ans = True
        while i < n:
            if bits[i]:
                i += 2
                ans = False
            else:
                i += 1
                ans = True
        return ans

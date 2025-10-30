from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        add = True
        n = len(digits) - 1
        while n >= 0 and add:
            digits[n] += 1
            add = digits[n] >= 10
            digits[n] %= 10
            n -= 1
        return [1] + digits if add else digits

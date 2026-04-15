from math import perm

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        return sum(9 * perm(9, i) for i in range(n)) + 1

from typing import List

class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        ans = []
        temp = 1
        while n:
            if n % 10:
                ans.append(n % 10 * temp)
            n //= 10
            temp *= 10
        return ans[::-1]

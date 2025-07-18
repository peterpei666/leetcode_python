from math import gcd

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        g = gcd(p, q)
        p = (p // g) % 2
        q = (q // g) % 2
        if p and q:
            return 1
        elif p:
            return 0
        else:
            return 2

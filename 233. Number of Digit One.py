from math import log10, ceil

class Solution:
    def countDigitOne(self, n: int) -> int:
        return sum((n // (10 ** (i+1))) * (10 ** i) + min(max(n % (10 ** (i+1)) - 10 ** i + 1, 0), 10 ** i) for i in range(len(str(n))))

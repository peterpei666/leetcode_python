import re

class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        match = re.fullmatch(r"([-]?\d+)\+([-]?\d+)i", num1)
        r1, i1 = int(match.group(1)), int(match.group(2))
        match = re.fullmatch(r"([-]?\d+)\+([-]?\d+)i", num2)
        r2, i2 = int(match.group(1)), int(match.group(2))
        r = r1 * r2 - i1 * i2
        i = r1 * i2 + r2 * i1
        return str(r) + '+' + str(i) + 'i'

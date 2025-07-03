import math

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        cnt = 0
        while k != 1:
            temp = int(math.log2(k))
            if k == 1 << temp:
                temp -= 1
            k -= 1 << temp
            cnt += operations[temp]
        return chr(ord('a') + cnt % 26)

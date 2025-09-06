from typing import List

class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        temp = sum(machines)
        n = len(machines)
        if temp % n:
            return -1
        temp //= n
        ans = 0
        balance = 0
        for i in machines:
            dif = i - temp
            balance += dif
            ans = max(ans, abs(balance), dif)
        return ans

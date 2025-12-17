from typing import List

class Solution:
    def minMoves(self, balance: List[int]) -> int:
        n = len(balance)
        total, idx = sum(balance), -1
        for i in range(n):
            if balance[i] < 0:
                idx = i
        if idx == -1:
            return 0
        if total < 0:
            return -1
        ans, total = 0, balance[idx]
        balance[idx] = 0
        for i in range(1, n):
            temp = 0
            if idx - 1 >= 0:
                temp += balance[idx - i]
                balance[idx - i] = 0
            else:
                temp += balance[n + idx - i]
                balance[n + idx - i] = 0
            if idx + i < n:
                temp += balance[idx + i]
                balance[idx + i] = 0
            else:
                temp += balance[idx + i - n]
                balance[idx + i - n] = 0
            if temp + total <= 0:
                ans += i * temp
                total += temp
            else:
                ans += i * -total
                total = 0
        return ans

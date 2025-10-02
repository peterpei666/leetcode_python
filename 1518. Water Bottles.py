class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        cnt, rem = 0, 0
        while numBottles:
            cnt += numBottles
            rem += numBottles
            numBottles = rem // numExchange
            rem %= numExchange
        return cnt

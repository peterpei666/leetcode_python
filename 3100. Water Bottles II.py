class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        cnt, empty = numBottles, numBottles
        while empty >= numExchange:
            empty -= numExchange
            cnt += 1
            empty += 1
            numExchange += 1
        return cnt

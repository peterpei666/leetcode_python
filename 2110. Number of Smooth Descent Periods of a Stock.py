class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        ans = 1
        j = 0
        for i in range(1, n):
            if prices[i] != prices[i - 1] - 1:
                j = i
            ans += i - j + 1
        return ans

from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        l, r = 0, 0
        temp, ans = 0, 0
        n = len(fruits)

        def step() -> int:
            if fruits[r][0] <= startPos:
                return startPos - fruits[l][0]
            elif fruits[l][0] >= startPos:
                return fruits[r][0] - startPos
            else:
                return min(abs(fruits[l][0] - startPos), abs(fruits[r][0] - startPos)) + fruits[r][0] - fruits[l][0]
            
        while r < n:
            temp += fruits[r][1]
            while l <= r and step() > k:
                temp -= fruits[l][1]
                l += 1
            ans = max(ans, temp)
            r += 1
        return ans

from typing import List

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        memo = dict()
        n = len(boxes)

        def dp(l: int, r: int, k: int) -> int:
            if l > r:
                return 0
            if (l, r, k) in memo:
                return memo[(l, r, k)]
            lt, kt = l, k
            while lt + 1 <= r and boxes[lt] == boxes[lt + 1]:
                lt += 1
                kt += 1
            ans = dp(lt + 1, r, 0) + (kt + 1) ** 2
            for m in range(lt + 1, r + 1):
                if boxes[lt] == boxes[m]:
                    ans = max(ans, dp(m, r, kt + 1) + dp(lt + 1, m - 1, 0))
            memo[(l, r, k)] = ans
            return ans
        
        return dp(0, n - 1, 0)

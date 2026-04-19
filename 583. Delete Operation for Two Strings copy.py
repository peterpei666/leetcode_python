from typing import List

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)
        memo = {tuple([0] * n) : 0}
        
        def dfs(cur: List[int]) -> int:
            if tuple(cur) in memo:
                return memo[tuple(cur)]
            ans = sum(cur[i] * price[i] for i in range(n))
            for sp in special:
                if all(cur[i] >= sp[i] for i in range(n)):
                    ans = min(ans, dfs([cur[i] - sp[i] for i in range(n)]) + sp[n])
            memo[tuple(cur)] = ans
            return ans
        
        return dfs(needs)

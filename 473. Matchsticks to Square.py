from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total & 3:
            return False
        target = total >> 2
        if max(matchsticks) > target:
            return False
        memo = {(target, target, target, target) : True}
        
        def dfs(key, idx) -> bool:
            if key in memo:
                return memo[key]
            temp = list(key)
            for i in range(4):
                if temp[i] + matchsticks[idx] <= target:
                    next = temp[:]
                    next[i] += matchsticks[idx]
                    for j in range(i - 1, -1, -1):
                        if next[j] < next[j + 1]:
                            next[j], next[j + 1] = next[j + 1], next[j]
                        else:
                            break
                    if dfs(tuple(next), idx + 1):
                        memo[key] = True
                        return True
            memo[key] = False
            return False
        
        return dfs((0, 0, 0, 0), 0)

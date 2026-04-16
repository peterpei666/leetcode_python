class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= 0:
            return True
        if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
            return False
        valid = [False] * (1 << maxChoosableInteger)
        win = [False] * (1 << maxChoosableInteger)

        def dfs(mask: int, target: int) -> bool:
            if valid[mask]:
                return win[mask]
            valid[mask] = True
            for i in range(maxChoosableInteger):
                bit = 1 << i
                if not mask & bit and (i + 1 >= target or not dfs(mask | bit, target - i - 1)):
                    win[mask] = True
                    return True
            return False
        
        return dfs(0, desiredTotal)

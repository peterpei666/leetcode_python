from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        arr = [1] + nums + [1]
        n = len(arr)
        memo = [[-1] * (n - 1) for _ in range(n - 1)]

        def dfs(i: int, j: int) -> int:
            if i > j:
                return 0
            if not memo[i][j] == -1:
                return memo[i][j]
            if i == j:
                temp = arr[i]
                if i - 1 >= 0:
                    temp *= arr[i - 1]
                if i + 1 < n:
                    temp *= arr[i + 1]
                memo[i][j] = temp
                return temp
            ans = 0
            for k in range(i, j + 1):
                temp = arr[k]
                if i - 1 >= 0:
                    temp *= arr[i - 1]
                if j + 1 < n:
                    temp *= arr[j + 1]
                temp += dfs(i, k - 1) + dfs(k + 1, j)
                ans = max(ans, temp)
            memo[i][j] = ans
            return ans
        
        return dfs(1, n - 2)

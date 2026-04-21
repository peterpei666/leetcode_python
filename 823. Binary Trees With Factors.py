from typing import List

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        n = len(arr)
        mod = 10 ** 9 + 7
        arr.sort()
        dp = dict()
        for i in arr:
            dp[i] = 1
        for k in range(1, n):
            for i in range(k):
                if arr[k] % arr[i] == 0:
                    j = arr[k] // arr[i]
                    if j in dp:
                        dp[arr[k]] = (dp[arr[k]] + dp[arr[i]] * dp[j]) % mod
        return sum(val for _ , val in dp.items()) % mod

class Solution:
    def __init__(self) -> None:
        self.nums = [[] for _ in range(51)]
        for i in range(5001):
            t, cur = 0, i
            while cur:
                t += cur % 10
                cur //= 10
            self.nums[t].append(i)

    def countArrays(self, digitSum: list[int]) -> int:
        n = len(digitSum)
        mod = 10 ** 9 + 7
        prefix = [0] * 5001
        for i in self.nums[digitSum[0]]:
            prefix[i] = 1
        for k in range(1, 5001):
            prefix[k] = (prefix[k] + prefix[k - 1]) % mod
        for i in range(1, n):
            dp = [0] * 5001
            for cur in self.nums[digitSum[i]]:
                dp[cur] = prefix[cur]
            prefix = dp[:]
            for k in range(1, 5001):
                prefix[k] = (prefix[k] + prefix[k - 1]) % mod
        return prefix[5000]

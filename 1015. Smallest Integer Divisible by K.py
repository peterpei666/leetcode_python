class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0:
            return -1
        temp, ans = 1 % k, 1
        while temp and ans <= k:
            temp = (temp * 10 + 1) % k
            ans += 1
        return -1 if ans == k + 1 else ans

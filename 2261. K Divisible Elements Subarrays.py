from typing import List

class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        mp = set()
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + (nums[i] % p == 0)
        for i in range(n):
            s = ''
            for j in range(i, n):
                if pre[j + 1] - pre[i] > k:
                    break
                s += str(nums[j]) + '#'
                mp.add(s)
        return len(mp)

class Solution:
    def countGoodSubarrays(self, nums: list[int]) -> int:
        n = len(nums)
        L, R = [0] * n, [n - 1] * n
        bit = [-1] * 31
        for i in range(n):
            for b in range(31):
                if nums[i] & (1 << b):
                    bit[b] = i
                else:
                    L[i] = max(L[i], bit[b] + 1)
        bit = [n] * 31
        for i in range(n - 1, -1, -1):
            for b in range(31):
                if nums[i] & (1 << b):
                    bit[b] = i
                else:
                    R[i] = min(R[i], bit[b] - 1)
        mp = dict()
        ans = 0
        for i in range(n):
            l, r = L[i], R[i]
            if nums[i] in mp:
                l = max(l, mp[nums[i]] + 1)
            mp[nums[i]] = i
            ans += (i - l + 1) * (r - i + 1)
        return ans

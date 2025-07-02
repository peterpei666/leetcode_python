class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mp = [0] * k
        mp[0] = 1
        ans = 0
        cur = 0
        for num in nums:
            cur = (cur + num) % k
            if cur < 0:
                cur += k
            ans += mp[cur]
            mp[cur] += 1
        return ans

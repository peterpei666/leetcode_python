class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        sum = 0
        for i in range(n):
            sum = (sum + nums[i]) % p
        if sum == 0:
            return 0
        mp = dict()
        mp[0] = -1
        cur = 0
        ans = n
        for i in range(n):
            cur = (cur + nums[i]) % p
            temp = (cur - sum + p) % p
            if temp in mp:
                ans = min(ans, i - mp[temp])
            mp[cur] = i
        return ans if ans != n else -1

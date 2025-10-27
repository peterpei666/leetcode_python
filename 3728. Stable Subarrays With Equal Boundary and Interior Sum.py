from typing import List
from collections import defaultdict

class Solution:
    def countStableSubarrays(self, arr: List[int]) -> int:
        mp = defaultdict(int)
        temp = [(arr[0], arr[0]), (arr[1], arr[0] + arr[1]), (0, 0)]
        cur = arr[0] + arr[1]
        ans = 0
        for i in range(2, len(arr)):
            mp[temp[(i - 2) % 3]] += 1
            if (arr[i], cur - arr[i]) in mp:
                ans += mp[(arr[i], cur - arr[i])]
            cur += arr[i]
            temp[i % 3] = (arr[i], cur)
        return ans

from collections import defaultdict
from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        for n in nums:
            cnt[n] += 1
        ans = 0
        if 1 in cnt:
            if cnt[1] % 2 == 1:
                ans = cnt[1]
            else:
                ans = cnt[1] - 1
        def dfs(cur, x) -> int:
            if x not in cnt:
                return cur - 1
            if cnt[x] == 1:
                return cur + 1
            else:
                if x > 10 ** 5:
                    return cur + 1
                else:
                    return dfs(cur + 2, x * x)
        cnt.pop(1, None)
        for i in cnt:
            ans = max(ans, dfs(0, i))
        return ans

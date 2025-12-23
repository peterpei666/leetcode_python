from typing import List

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n = len(events)
        dp = [[-1, -1] for _ in range(n)]

        def dfs(idx: int, cnt: int) -> int:
            if cnt == 2 or idx >= n:
                return 0
            if dp[idx][cnt] == -1:
                end = events[idx][1]
                l, r = idx + 1, n - 1
                while l < r:
                    mid = (r - l) // 2 + l
                    if events[mid][0] > end:
                        r = mid
                    else:
                        l = mid + 1
                include = events[idx][2] + (dfs(l, cnt + 1) if l < n and events[l][0] > end else 0)
                exclude = dfs(idx + 1, cnt)
                dp[idx][cnt] = max(include, exclude)
            return dp[idx][cnt]

        return dfs(0, 0)

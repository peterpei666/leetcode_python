import bisect

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        
        l = 0
        ans = 0
        r = len(removable)
        while l <= r:
            mid = (l + r + 1) // 2
            removed = [False] * len(s)
            for i in range(mid):
                removed[removable[i]] = True
            table = [[] for _ in range(26)]
            for i in range(len(s)):
                if removed[i] == False:
                    table[ord(s[i]) - ord('a')].append(i)
            j = -1
            flag = True
            for c in p:
                idx = bisect.bisect_right(table[ord(c) - ord('a')], j)
                if idx == len(table[ord(c) - ord('a')]):
                    flag = False
                    break
                j = table[ord(c) - ord('a')][idx]
            if flag:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

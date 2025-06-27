from collections import Counter, deque

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        letters = sorted([c for c, cnt in Counter(s).items() if cnt >= k], reverse=True)
        ans = ""
        q = deque(letters)
        while q:
            cur = q.popleft()
            if len(cur) > len(ans):
                ans = cur
            for c in letters:
                next = cur + c
                it = iter(s)
                if all(ch in it for ch in next * k):
                    q.append(next)
        return ans

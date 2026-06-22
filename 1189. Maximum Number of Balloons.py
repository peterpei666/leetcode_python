from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = defaultdict(int)
        for c in text:
            cnt[c] += 1
        ans = 100000
        ans = min(ans, cnt['b'])
        ans = min(ans, cnt['a'])
        ans = min(ans, cnt['l'] // 2)
        ans = min(ans, cnt['o'] // 2)
        ans = min(ans, cnt['n'])
        return ans

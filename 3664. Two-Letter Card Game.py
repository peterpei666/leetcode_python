from typing import List

class Solution:
    def score(self, cards: List[str], x: str) -> int:
        cnt = [[0] * 10 for _ in range(10)]
        for s in cards:
            cnt[ord(s[0]) - ord('a')][ord(s[1]) - ord('a')] += 1
        a1, a2 = 0, 0
        sum1, sum2 = 0, 0
        for i in range(10):
            if i == ord(x) - ord('a'):
                continue
            a1 = max(a1, cnt[i][ord(x) - ord('a')])
            a2 = max(a2, cnt[ord(x) - ord('a')][i])
            sum1 += cnt[i][ord(x) - ord('a')]
            sum2 += cnt[ord(x) - ord('a')][i]
        ans = 0
        for k1 in range(cnt[ord(x) - ord('a')][ord(x) - ord('a')] + 1):
            k2 = cnt[ord(x) - ord('a')][ord(x) - ord('a')] - k1
            max1 = max(a1, k1)
            total1 = sum1 + k1
            if max1 > total1 // 2:
                temp1 = total1 - max1
            else:
                temp1 = total1 // 2
            max2 = max(a2, k2)
            total2 = sum2 + k2
            if max2 > total2 // 2:
                temp2 = total2 - max2
            else:
                temp2 = total2 // 2
            ans = max(ans, temp1 + temp2)
        return ans

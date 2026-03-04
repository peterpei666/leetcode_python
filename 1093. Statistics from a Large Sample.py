from typing import List

class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        ans = [255.0, 0, 0, 0, 0]
        total = 0
        for i in range(256):
            total += count[i]
        m1 = (total + 1) // 2
        m2 = (total + 2) // 2
        cnt = 0
        for i in range(256):
            if count[i]:
                ans[0] = min(int(ans[0]), i)
                ans[1] = i
            ans[2] += i * 1.0 * count[i] / total
            if cnt < m1 and cnt + count[i] >= m1:
                ans[3] += i * 0.5
            if cnt < m2 and cnt + count[i] >= m2:
                ans[3] += i * 0.5
            ans[4] = i if count[i] > count[int(ans[4])] else ans[4]
            cnt += count[i]
        return ans

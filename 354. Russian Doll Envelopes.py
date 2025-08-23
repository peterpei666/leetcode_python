class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        ans = []
        for _, h in envelopes:
            it = bisect_left(ans, h)
            if it == len(ans):
                ans.append(h)
            else:
                ans[it] = h
        return len(ans)

class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        INT_MAX = 0x3FFFFFFF
        bmin1 = [INT_MAX] * (n + 1)
        bmin2 = [INT_MAX] * (n + 1)
        for pair in conflictingPairs:
            a = min(pair)
            b = max(pair)
            if bmin1[a] > b:
                bmin2[a] = bmin1[a]
                bmin1[a] = b
            elif bmin2[a] > b:
                bmin2[a] = b
        ans = 0
        b1, b2 = n, INT_MAX
        delcount = [0] * (n + 1)
        for i in range(n, 0, -1):
            if bmin1[b1] > bmin1[i]:
                b2 = min(b2, bmin1[b1])
                b1 = i
            else:
                b2 = min(b2, bmin1[i])
            ans += min(bmin1[b1], n + 1) - i
            delcount[b1] += min(b2, bmin2[b1], n + 1) - min(bmin1[b1], n + 1)
        return ans + max(delcount)

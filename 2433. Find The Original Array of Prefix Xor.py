class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n = len(pref)
        ret = [0] * n
        ret[0] = pref[0]
        for i in range(1, n):
            ret[i] = pref[i] ^ pref[i - 1]
        return ret

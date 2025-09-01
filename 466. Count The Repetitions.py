class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1 == 0:
            return 0
        l1 = len(s1)
        l2 = len(s2)
        countr, indexr = [0] * (l2 + 1), [0] * (l2 + 1)
        cnt, idx = 0, 0
        for i in range(n1):
            for j in range(l1):
                if s1[j] == s2[idx]:
                    idx += 1
                if idx == l2:
                    idx = 0
                    cnt += 1
            countr[i] = cnt
            indexr[i] = idx
            for k in range(i):
                if indexr[k] == idx:
                    prev = countr[k]
                    patt = (countr[i] - countr[k]) * ((n1 - k - 1) // (i - k))
                    rem = countr[k + (n1 - k - 1) % (i - k)] - countr[k]
                    return (prev + patt + rem) // n2
        return countr[n1 - 1] // n2

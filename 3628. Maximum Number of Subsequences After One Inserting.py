class Solution:
    def numOfSubsequences(self, s: str) -> int:
        t = 0
        for c in s:
            if c == 'T':
                t += 1
        temp1, temp2, temp3 = 0, 0, 0
        k, l = 0, 0
        for c in s:
            k = max(k, l * t)
            if c == 'L':
                l += 1
            elif c == 'C':
                temp1 += (l + 1) * t
                temp2 += l * t
                temp3 += l * (t + 1)
            elif c == 'T':
                t -= 1
        return max(temp1, temp2 + k, temp3)

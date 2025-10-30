class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m, n = len(a) - 1, len(b) - 1
        add = 0
        s = ''
        while m >= 0 or n >= 0:
            temp = add
            if m >= 0:
                temp += ord(a[m]) - ord('0')
                m -= 1
            if n >= 0:
                temp += ord(b[n]) - ord('0')
                n -= 1
            add = temp // 2
            if temp & 1:
                s += '1'
            else:
                s += '0'
        if add:
            s += '1'
        return s[::-1]

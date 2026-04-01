class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)
        ans = ['?'] * (m + n - 1)
        for i in range(m):
            if str1[i] == 'F':
                continue
            for j in range(n):
                if not ans[i + j] == '?' and not ans[i + j] == str2[j]:
                    return ''
                ans[i + j] = str2[j]
        old = ans
        ans = ['a' if c == '?' else c for c in old]
        for i in range(m):
            if str1[i] == 'T' or not ''.join(ans[i:i+n]) == str2:
                continue
            valid = False
            for j in range(i + n - 1, i - 1, -1):
                if old[j] == '?':
                    ans[j] = 'b'
                    valid = True
                    break
            if not valid:
                return ''
        return ''.join(ans)

class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        temp = []
        n = len(s)
        cnt, l = 0, 0
        for r in range(n):
            if s[r] == '1':
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                temp.append('1' + self.makeLargestSpecial(s[l+1:r]) + '0')
                l = r + 1
        temp.sort(reverse=True)
        return ''.join(temp)

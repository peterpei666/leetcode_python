class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ans = ''
        while columnNumber:
            columnNumber -= 1
            ans = ans + s[columnNumber % 26]
            columnNumber //= 26
        return ans[::-1]

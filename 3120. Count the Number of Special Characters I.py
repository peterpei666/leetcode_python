class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        upper, lower = 0, 0
        for i in range(len(word)):
            if ord(word[i]) >= ord('A') and ord(word[i]) <= ord('Z'):
                upper |= 1 << (ord(word[i]) - ord('A'))
            if ord(word[i]) >= ord('a') and ord(word[i]) <= ord('z'):
                lower |= 1 << (ord(word[i]) - ord('a'))
        return (upper & lower).bit_count()

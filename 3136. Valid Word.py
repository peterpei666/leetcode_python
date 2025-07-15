class Solution:
    def isValid(self, word: str) -> bool:
        n = len(word)
        if n < 3:
            return False
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        v, c = False, False
        for i in range(n):
            if ord('0') <= ord(word[i]) <= ord('9'):
                continue
            if ord('a') <= ord(word[i]) <= ord('z') or ord('A') <= ord(word[i]) <= ord('Z'):
                if word[i] in vowel:
                    v = True
                else:
                    c = True
            else:
                return False
        return v and c

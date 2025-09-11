class Solution:
    def sortVowels(self, s: str) -> str:
        v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowel = []
        for c in s:
            if c in v:
                vowel.append(c)
        vowel.sort()
        ans = ""
        i = 0
        for c in s:
            if c in v:
                ans += vowel[i]
                i += 1
            else:
                ans += c
        return ans

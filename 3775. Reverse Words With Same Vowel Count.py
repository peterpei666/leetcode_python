class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        vowel = ['a', 'e', 'i', 'o', 'u']

        def count(w: str) -> int:
            cnt = 0
            for c in w:
                if c in vowel:
                    cnt += 1
            return cnt
        
        t = count(words[0])
        for i in range(1, len(words)):
            if t == count(words[i]):
                words[i] = words[i][::-1]
        return ' '.join(words)
